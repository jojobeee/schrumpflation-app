import django_tables2 as tables
from .models import Purchase

class PurchaseTable(tables.Table):
 
    class Meta:
        model = Purchase
        template_name = 'django_tables2/bootstrap.html'
        fields = ('product', 'supermarket', 'size', 'unit', 'price', 'currency', 'purchase_date')

 