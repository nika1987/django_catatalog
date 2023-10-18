from audioop import reverse

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from slugify import slugify

from .forms import ProductForm, VersionForm
from .models import Product, Category, Version


class ProductListView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/test.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'shop/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('shop:index')

    def form_validate(self, form):
        response = super().form_valid(form)
        self.object.owner = self.request.user
        self.object.save()
        return response


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'shop/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('shop:index')
    permission_required = [
        'shop.can_change_is_published_permission',
        'shop.can_change_desc_permission',
        'shop.can_change_category_permission',
    ]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        user = self.request.user
        obj = self.get_object()

        active_version_id = self.request.POST.get('active_version')
        if active_version_id:
            active_version = Version.objects.get(id=active_version_id)
            active_version.is_active = True
            active_version.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('shop:index')


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('shop:index')
    permission_required = 'shop.can_delete_product'


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category.html'
    context_object_name = 'category'
