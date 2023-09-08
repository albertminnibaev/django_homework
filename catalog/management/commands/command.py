from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        #Category.objects.all().delete()

        Category.objects.raw('TRUNCATE TABLE category RESTART IDENTITY;')

        category_list = [
            {'name': 'фрукты', 'descriptions': 'вкусные'},
            {'name': 'овощи', 'descriptions': 'полезные'},
            {'name': 'ягода', 'descriptions': 'сладкаие'},
            {'name': 'орехи', 'descriptions': 'питательные'}
        ]

        for category_item in category_list:
            Category.objects.create(**category_item)

        product_list = [
            {'name': 'апельсин', 'descriptions': 'оранжевый', 'category': 1, 'price': 100},
            {'name': 'огурец', 'descriptions': 'зеленый', 'category': 2, 'price': 30},
            {'name': 'малина', 'descriptions': 'любят дети', 'category': 3, 'price': 200},
            {'name': 'миндаль', 'descriptions': 'вкусный', 'category': 4, 'price': 300}
        ]

        for product_item in product_list:
            Product.objects.create(**product_item)
