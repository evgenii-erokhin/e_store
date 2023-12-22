from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import login, logout, UserRegistrationView, UserProfileView


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/',
         login_required(UserProfileView.as_view()),
         name='profile'
         ),
]
