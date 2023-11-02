from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=256,
    )
    description = models.TextField(
        'Описание категории',
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
        upload_to='media/images',
    )
    description = models.TextField(
        'Описание товара',
    )
    short_description = models.CharField(
        'Краткое описание товара',
        max_length=64,
    )
    price = models.PositiveIntegerField(
        'Стоимомть товара'
    )
    quantity = models.PositiveIntegerField(
        'Количество товара на складе'
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
