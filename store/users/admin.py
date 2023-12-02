from django.contrib import admin
from products.admin import BasketAdmin
from users.models import User


@admin.register(User)
class UserAdnin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'username',
    )
    inlines = (
        BasketAdmin,
    )
