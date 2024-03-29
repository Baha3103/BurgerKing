from django.contrib import admin

from order.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_filter = ['created',]
    list_display = ['id', 'address', 'created']
