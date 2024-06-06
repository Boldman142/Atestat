from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('pk', 'author', 'title', 'model', 'release_date')
    list_filter = ('author', 'title',)
    search_fields = ('title',)
