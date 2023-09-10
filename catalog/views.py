from django.shortcuts import render

from catalog.models import Category, Product
from django.core.management import BaseCommand


def index(request):
    context = {
        "object_list": Category.objects.all()[:3],
        "title": 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        "object_list": Category.objects.all(),
        "title": 'Категории продуктов'
    }
    return render(request, 'catalog/categories.html', context)


def products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        "object_list": Product.objects.filter(category=pk),
        "title": f'Продукты категории {category_item.name}'
    }
    return render(request, 'catalog/product.html', context)


def contact(request):
    data = []
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data.append({
            'name': name,
            'phone': phone,
            'message': message
        })
        print(f'You have new message from {name}({phone}): {message}')
        print(data)
    context = {
        "title": 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def add_product(request):
    data = []
    if request.method == 'POST':
        name = request.POST.get('name')
        descriptions = request.POST.get('descriptions')
        picture = request.POST.get('picture')
        category = request.POST.get('category')
        price = request.POST.get('price')
        date_of_creation = request.POST.get('date_of_creation')
        last_modified_date = request.POST.get('last_modified_date')
        data.append({
            'name': name,
            'descriptions': descriptions,
            'picture': picture,
            'category': Category.objects.get(pk=category),
            'price': price,
            'date_of_creation': date_of_creation,
            'last_modified_date': last_modified_date
        })

    context = {
        "title": 'Добавить продукт'
    }

    class Add(BaseCommand):

        def handle(self, *args, **options):

            for product_item in data:
                Product.objects.create(**product_item)
    Add().handle()

    return render(request, 'catalog/add_product.html', context)


# def home(request):
#     item_1 = {'name': 'апельсин', 'descriptions': 'оранжевый', 'category': 1, 'price': 100}
#     item_2 = {'name': 'огурец', 'descriptions': 'зеленый', 'category': 2, 'price': 30}
#     item_3 = {'name': 'малина', 'descriptions': 'любят дети', 'category': 3, 'price': 200}
#     item_4 = {'name': 'миндаль', 'descriptions': 'вкусный', 'category': 4, 'price': 300}
#
#     data = {'item_1': item_1, 'item_2': item_2, 'item_3': item_3, 'item_4': item_4}
#     return render(request, 'catalog/home.html', context=data)
