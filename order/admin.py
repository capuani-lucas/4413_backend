from django.contrib import admin

# Register your models here.

from order.models.Order import Order, OrderHistory

admin.site.register(Order)
admin.site.register(OrderHistory)