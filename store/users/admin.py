from django.contrib import admin
from products.admin import BasketAdmin
from users.models import EmailVerification, User


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


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'user',
        'expiration',
    )
    fields = (
        'code',
        'user',
        'expirations',
        'created'
    )
    readonly_fields = ('created',)
