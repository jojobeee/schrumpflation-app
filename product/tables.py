import django_tables2 as tables
from .models import Purchase

class PurchaseTable(tables.Table):
    price_per_kg_or_l = tables.Column()
    
    class Meta:
        model = Purchase
        template_name = 'django_tables2/bootstrap.html'
        fields = ('purchase_date', 'supermarket', 'size', 'unit', 'price', 'currency', 'price_per_kg_or_l')
        order_by = 'purchase_date'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def render_price_per_kg_or_l(self, value, record):
        return record.price_per_kg_or_l()

  

 