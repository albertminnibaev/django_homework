from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Record(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.CharField(**NULLABLE, max_length=250, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='Содержание')
    preview = models.ImageField(upload_to='records/', **NULLABLE, verbose_name='изображение')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    sign = models.BooleanField(default=True, verbose_name='признак публикации')
    quantity = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} ({self.quantity} просмотров)'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
