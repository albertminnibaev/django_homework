from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView

from catalog.forms import ProductForm, VersionForm, ProductFormStaff
from catalog.models import Category, Product, Version
from catalog.services import get_categories_cache


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        "title": 'Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["object_list"] = get_categories_cache()[:3]
        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        "title": 'Категории продуктов'
    }


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('pk'), owner=self.request.user)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data["category_pk"] = category_item.pk
        context_data["title"] = f'Продукты категории {category_item.name}'
        context_data['version'] = Version.objects.all()

        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    #fields = ('name', 'descriptions', 'picture', 'category', 'price', 'date_of_creation', 'last_modified_date')
    success_url = reverse_lazy('catalog:categories')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    #form_class = ProductForm
    #fields = ('name', 'descriptions', 'picture', 'category', 'price', 'last_modified_date')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category.pk])

    def get_form_class(self):
        if self.request.user.is_staff and not self.request.user.is_superuser:
            # если пользователь is_staff и не суперюзер, то выводится форма с полями описание, категория и
            # признак публикации
            return ProductFormStaff
        else:
            return ProductForm


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category.pk])


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


class VersionListView(ListView):
    model = Version

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(product=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data["product_pk"] = product.pk
        context_data["title"] = f'Версии продукта {product.name}'

        return context_data


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('catalog:version', args=[self.object.product.pk])


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('catalog:version', args=[self.object.product.pk])


class VersionDetailView(DetailView):
    model = Version


class VersionDeleteView(DeleteView):
    model = Version



# def index(request):
#     context = {
#         "object_list": Category.objects.all()[:3],
#         "title": 'Главная'
#     }
#     return render(request, 'catalog/index.html', context)

# def categories(request):
#     context = {
#         "object_list": Category.objects.all(),
#         "title": 'Категории продуктов'
#     }
#     return render(request, 'catalog/category_list.html', context)

# def products(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         "object_list": Product.objects.filter(category=pk),
#         "title": f'Продукты категории {category_item.name}'
#     }
#     return render(request, 'catalog/product_list.html', context)

# def home(request):
#     item_1 = {'name': 'апельсин', 'descriptions': 'оранжевый', 'category': 1, 'price': 100}
#     item_2 = {'name': 'огурец', 'descriptions': 'зеленый', 'category': 2, 'price': 30}
#     item_3 = {'name': 'малина', 'descriptions': 'любят дети', 'category': 3, 'price': 200}
#     item_4 = {'name': 'миндаль', 'descriptions': 'вкусный', 'category': 4, 'price': 300}
#
#     data = {'item_1': item_1, 'item_2': item_2, 'item_3': item_3, 'item_4': item_4}
#     return render(request, 'catalog/home.html', context=data)

# def add_product(request):
#     data = []
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         descriptions = request.POST.get('descriptions')
#         picture = request.POST.get('picture')
#         category = request.POST.get('category')
#         price = request.POST.get('price')
#         date_of_creation = request.POST.get('date_of_creation')
#         last_modified_date = request.POST.get('last_modified_date')
#         data.append({
#             'name': name,
#             'descriptions': descriptions,
#             'picture': picture,
#             'category': Category.objects.get(pk=category),
#             'price': price,
#             'date_of_creation': date_of_creation,
#             'last_modified_date': last_modified_date
#         })
#
#     context = {
#         "title": 'Добавить продукт'
#     }
#
#     class Add(BaseCommand):
#
#         def handle(self, *args, **options):
#
#             for product_item in data:
#                 Product.objects.create(**product_item)
#     Add().handle()
#
#     return render(request, 'catalog/add_product.html', context)
