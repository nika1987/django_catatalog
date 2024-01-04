from django.contrib import admin
from .models import Product, Category, Version


# Register your models here.
# admin.site.register(Student)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Version, VersionAdmin)
