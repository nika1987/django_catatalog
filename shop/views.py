from audioop import reverse

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from slugify import slugify

from .models import Product, Category, BlogPost


class ProductListView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/test.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.views_count += 1
        self.object.save()
        return self.object


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category.html'
    context_object_name = 'category'


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description')
    success_url = reverse_lazy('shop:test')

    def form_validate(self, form):
        new_product = form.save()
        new_product.slug = slugify(new_product.name)
        new_product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'description',)
    #success_url = reverse_lazy('shop:test')

    def form_validate(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('products:view', args=[self.kwargs.get('pk')])
