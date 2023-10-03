from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    descriptions = models.TextField(**NULLABLE, verbose_name='описание')
    #created_at = models.DateField(**NULLABLE, verbose_name='дата создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    descriptions = models.TextField(**NULLABLE, verbose_name='описание')
    picture = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_of_creation = models.DateField(**NULLABLE, verbose_name='дата создания')
    last_modified_date = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.PositiveIntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=50, verbose_name='название версии')
    sign = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'версия {self.number} продукта {self.product.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
