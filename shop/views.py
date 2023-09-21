from django.shortcuts import render
from .models import Product, Category


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'test.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context=context)


def category_detail(request, id):
    category = Category.objects.get(id=id)
    context = {'category': category}
    return render(request, 'shop/category.html', context)


def category_list(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'shop/category_list.html', context=context)


