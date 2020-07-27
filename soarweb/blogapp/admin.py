from django.contrib import admin
from .models import Category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'created', 'update',)
    list_filter = ('status', 'category')
    search_fields = ('title', 'body')


admin.site.register(Post, PostAdmin)
