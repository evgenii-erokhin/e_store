from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    users_images = models.ImageField(
        'Изображение пользователя',
        upload_to='users_image/',
        blank=True,
        null=True
    )
    is_verified_email = models.BooleanField(
        'Подтвердил ли пользователь свой email',
        default=False
    )
    email = models.EmailField(
        'Адресс электронной почты',
        unique=True,
        blank=False
        )


class EmailVerification(models.Model):
    code = models.UUIDField(
        'Код подтверждения email',
        unique=True
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    created = models.DateTimeField(
        'Время создания кода верификации',
        auto_now_add=True
    )
    expiration = models.DateTimeField(
        'Время истечения срока действия кода верификации'
    )

    class Meta:
        verbose_name = 'Код верификации имейла'
        verbose_name_plural = 'Код верификации имейла'

    def __str__(self):
        return f'Email verification object for {self.user.username}'

    def send_verification_mail(self):
        link = reverse('users:email_verifications', kwargs={
            'email': self.user.email,
            'code': self.code
            })
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учётной записи для {self.user.username}'
        message = 'Для подтвержения учётной записи {} пройдите по ссылке: {}'.format(
            self.user.email,
            verification_link
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )
