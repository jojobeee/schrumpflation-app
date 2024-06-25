import django_tables2 as tables
from .models import Purchase

class PurchaseTable(tables.Table):
    product__unit = tables.Column(verbose_name='Unit')
    price_per_kg_or_l = tables.Column(verbose_name='Price per Kilo')

    class Meta:
        model = Purchase
        template_name = 'django_tables2/bootstrap.html'
        fields = ('product', 'supermarket', 'size', 'product__unit', 'price', 'currency', 'purchase_date', 'price_per_kg_or_l',)
        order_by = 'purchase_date'

    def render_product__unit(self, value, record):
        return record.product.unit

    def render_price_per_kg_or_l(self, value, record):
        return record.price_per_kg_or_l()

