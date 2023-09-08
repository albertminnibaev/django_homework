from django.shortcuts import render


def home(request):
    item_1 = {'name': 'апельсин', 'descriptions': 'оранжевый', 'category': 1, 'price': 100}
    item_2 = {'name': 'огурец', 'descriptions': 'зеленый', 'category': 2, 'price': 30}
    item_3 = {'name': 'малина', 'descriptions': 'любят дети', 'category': 3, 'price': 200}
    item_4 = {'name': 'миндаль', 'descriptions': 'вкусный', 'category': 4, 'price': 300}

    data = {'item_1': item_1, 'item_2': item_2, 'item_3': item_3, 'item_4': item_4}
    return render(request, 'catalog/home.html', context=data)


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
    return render(request, 'catalog/contacts.html')

