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

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/test.html'
    context_object_name = 'product'




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



class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'description',)
    success_url = reverse_lazy('shop:test')



class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('name', 'description')
    success_url = reverse_lazy('shop:index')

