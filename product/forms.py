from django import forms
from .models import Product, Purchase

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brand', 'product_type']  
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [ 'supermarket', 'size', 'unit', 'price', 'currency', 'purchase_date']  