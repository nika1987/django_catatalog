from django.contrib import admin

from .models import BlogPost

# Register your models here.
# admin.site.register(Student)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    list_filter = ('name',)
    search_fields = ('description',)


admin.site.register(BlogPost, BlogAdmin)
