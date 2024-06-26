from django.db import models

class Supermarket(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilogramm'),
        ('g', 'Gramm'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
    ]

    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    CURRENCY_CHOICES = [
        ('EUR', 'Euro'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE, verbose_name='Supermarkt')
    size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Größe')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preis')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, verbose_name='Währung')
    purchase_date = models.DateField(verbose_name='Kaufdatum')

    def price_per_kg_or_l(self):
        if self.product.unit in ['kg', 'l']:
            return round(self.price / self.size, 2)
        elif self.product.unit in ['g', 'ml']:
            return round((self.price / self.size) * 1000, 2)
        else:
            return None

    def __str__(self):
        return f'{self.product.name} - {self.supermarket.name} - {self.unit} - {self.price} - {self.purchase_date} - {self.price_per_kg_or_l()}'

    @property
    def price_per_kg_or_l_display(self):
        return self.price_per_kg_or_l() if self.price_per_kg_or_l() is not None else 'N/A'
