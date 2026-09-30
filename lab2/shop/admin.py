from django.contrib import admin

from .models import Cart, Customer, Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'created_at',
        'status',
        'products_count',
    )

    list_filter = ('status',)

    search_fields = (
        'customer__name',
        'customer__email',
    )

    filter_horizontal = ('products',)