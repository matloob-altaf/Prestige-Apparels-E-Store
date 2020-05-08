from django.contrib import admin
from Guest.models import Product, Customer, Reviews , Orders, Inventory, Newsletter, Cart, CartItem


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart

admin.site.register(Product)
admin.site.register(Reviews)
admin.site.register(Orders)
admin.site.register(Inventory)
admin.site.register(Newsletter)
admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(Cart, CartAdmin)
