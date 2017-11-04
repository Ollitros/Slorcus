from django.contrib import admin
from .models import *


class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    # search_fields = ['id', 'email', 'mobile_number']
    #
    # fields = ["id", "email", 'name', 'surname']

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class OrderInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in OrderInBasket._meta.fields]
    # search_fields = ['session_key', 'book_id', 'books']
    #
    # fields = ['session_key', 'book_id']

    class Meta:
        model = OrderInBasket

admin.site.register(OrderInBasket, OrderInBasketAdmin)