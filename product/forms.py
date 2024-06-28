from django import forms
from .models import Product, Purchase, Brand, Supermarket
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    """ Formular für Produkt """
    
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'unit']

class PurchaseForm(forms.ModelForm):
    """ Formular für Produktkauf """
    
    class Meta:
        model = Purchase
        fields = ['size', 'price', 'currency', 'purchase_date']

class BrandForm(forms.ModelForm):
    """ Formular für Marke """

    class Meta:
        model = Brand
        fields = ['name']

class SupermarketForm(forms.ModelForm):
    """ Formular für Supermarkt """

    class Meta:
        model = Supermarket
        fields = ['name']

class CombinedAddSchrumpflationForm(forms.Form):
    """ Formular, um die einzelnen Felder zu kombinieren """

    product_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': 'product-name'}))
    new_product_type = forms.CharField(max_length=100, required=True)
    
    existing_brand = forms.ModelChoiceField(queryset=Brand.objects.all().order_by('name'), required=False, empty_label="Marke auswählen")
    new_brand = forms.CharField(max_length=100, required=False)
    
    existing_supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all().order_by('name'), required=False, empty_label="Supermarkt auswählen")
    new_supermarket = forms.CharField(max_length=100, required=False)
    
    size = forms.DecimalField(max_digits=10, decimal_places=2)
    unit = forms.ChoiceField(choices=Product.UNIT_CHOICES, initial='g')
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    currency = forms.ChoiceField(choices=Purchase.CURRENCY_CHOICES, initial='EUR')
    purchase_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    def clean(self):
        # Prüfen, ob mindestens eins der jeweils zwei Felder für Marke und Supermarkt ausgefüllt sind und Rückgabe einer Fehlermeldung, falls nicht.
        cleaned_data = super().clean()
        
        existing_brand = cleaned_data.get('existing_brand')
        new_brand = cleaned_data.get('new_brand')
        
        existing_supermarket = cleaned_data.get('existing_supermarket')
        new_supermarket = cleaned_data.get('new_supermarket')

        if not existing_brand and not new_brand:
            raise ValidationError('Bitte füllen Sie mindestens eins der beiden Felder "Marke" oder "oder neue Marke hinzufügen" aus!')

        if not existing_supermarket and not new_supermarket:
            raise ValidationError('Bitte füllen Sie mindestens eins der beiden Felder "Supermarkt" oder "oder neuen Supermarkt hinzufügen" aus!')

        return cleaned_data