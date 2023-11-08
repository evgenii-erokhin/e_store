from django.db import models


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
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.name
