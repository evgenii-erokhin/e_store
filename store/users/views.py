from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse, reverse_lazy

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request,
#                 'Поздравляем! Вы успешно зарегестрировались'
#             )
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(
#             instance=request.user,
#             data=request.POST,
#             files=request.FILES
#         )
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)

#     baskets = Basket.objects.filter(user=request.user)

#     context = {
#         'form': form,
#         'baskets': baskets,
#         }
#     return render(request, 'users/profile.html', context)
