from django import forms
from .models import Product, Purchase, Brand, Supermarket

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['size', 'unit', 'price', 'currency', 'purchase_date']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class SupermarketForm(forms.ModelForm):
    class Meta:
        model = Supermarket
        fields = ['name']

class CombinedAddSchrumpflationForm(forms.Form):
    product_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': 'product-name'}))
    new_product_type = forms.CharField(max_length=100, required=False)
    existing_brand = forms.ModelChoiceField(queryset=Brand.objects.all().order_by('name'), required=False, empty_label="Marke auswählen")
    new_brand = forms.CharField(max_length=100, required=False)
    existing_supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all().order_by('name'), required=False, empty_label="Supermarkt auswählen")
    new_supermarket = forms.CharField(max_length=100, required=False)
    size = forms.DecimalField(max_digits=10, decimal_places=2)
    unit = forms.ChoiceField(choices=Purchase.UNIT_CHOICES, initial='g')
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    currency = forms.ChoiceField(choices=Purchase.CURRENCY_CHOICES, initial='EUR')
    purchase_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
