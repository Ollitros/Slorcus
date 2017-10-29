from django.db import models
from Library.models import *


class Order(models.Model):
    product = models.ForeignKey(Book)
    email = models.EmailField(blank=False, max_length=64)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    quantity = models.CharField(blank=False, max_length=4096)
    mobile_number = models.EmailField(blank=False, max_length=32)
    appendage = models.TextField(max_length=2048, blank=True)
    total_price = models.CharField(blank=False, max_length=256)

    def __str__(self):
        return "Order %s" % self.id

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderInBasket(models.Model):
    books = models.ForeignKey(Book, blank=True, null=True, default=None)
    session_key = models.CharField(max_length=1024)
    book_id = models.CharField(max_length=1024, blank=True, null=True, default=None)


    def __str__(self):
        return "OrderInBasket %s" % self.session_key

    class Meta:
        verbose_name = 'OrderInBasket'
        verbose_name_plural = 'OrdersInBasket'
