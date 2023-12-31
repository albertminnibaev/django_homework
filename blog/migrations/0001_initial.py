# Generated by Django 4.2.5 on 2023-09-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=250, verbose_name='человекопонятный URL')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Заголовок')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='Records/', verbose_name='изображение')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='дата создания')),
                ('sign', models.BooleanField(verbose_name='признак публикации')),
                ('quantity', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
            },
        ),
    ]
