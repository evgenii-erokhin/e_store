from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=256,
        unique=True,
    )
    description = models.TextField(
        'Описание категории',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        'Название продукта',
        max_length=256,
    )
    image = models.ImageField(
        'Изображение товара',
        upload_to='images',
    )
    description = models.TextField(
        'Описание товара',
    )
    price = models.DecimalField(
        'Стоимомть товара',
        max_digits=6,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        'Количество товара на складе',
        default=0,
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='Категория товара'
    )

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    products = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    quantity = models.PositiveIntegerField(
        'Количество товара',
        default=0,
    )
    created_timestamp = models.DateTimeField(
        'Время создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Корзина товаров'
        verbose_name_plural = 'Корзина товаров'

    def __str__(self):
        return f'В корзине {self.quantity} товаров'

    def sum(self):
        return self.products.price * self.quantity

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)
