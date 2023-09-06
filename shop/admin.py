from django.contrib import admin
from .models import Product, Category


# Register your models here.
# admin.site.register(Student)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
