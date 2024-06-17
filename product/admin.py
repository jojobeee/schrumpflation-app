from django.contrib import admin
from .models import Supermarket, Brand, Product, Purchase

# Register your models here.
admin.site.register(Supermarket)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Purchase)