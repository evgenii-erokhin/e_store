# Generated by Django 3.2 on 2023-11-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Изображение товара'),
        ),
    ]