from django.db import models
from Library.models import *


class Order(models.Model):
    address = models.CharField(max_length=256, null=True)
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


class ProductInOrder(models.Model):
    session_key_product_in_order = models.CharField(max_length=1024, null=True)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Book, blank=True, null=True, default=None)
    quantity = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Book in order'
        verbose_name_plural = 'Books in order'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        print (self.quantity)

        self.total_price = int(self.quantity) * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


class OrderInBasket(models.Model):
    books = models.ForeignKey(Book, blank=True, null=True, default=None)
    session_key = models.CharField(max_length=1024)
    book_id = models.CharField(max_length=1024, blank=True, null=True, default=None)

    def __str__(self):
        return "OrderInBasket %s" % self.session_key

    class Meta:
        verbose_name = 'OrderInBasket'
        verbose_name_plural = 'OrdersInBasket'
