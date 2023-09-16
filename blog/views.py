from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Record


class RecordCreateView(CreateView):
    model = Record
    fields = ('title', 'slug', 'content', 'preview', 'created_at', 'sign', 'quantity')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.save()

        return super().form_valid(form)


class RecordUpdateView(UpdateView):
    model = Record
    fields = ('title', 'slug', 'content', 'preview', 'created_at', 'sign', 'quantity')
    #success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class RecordListView(ListView):
    model = Record

    extra_context = {
        "title": 'Статьи блога'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign=True)
        return queryset


class RecordDetailView(DetailView):
    model = Record

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.quantity += 1
        self.object.save()
        return self.object


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('blog:list')
