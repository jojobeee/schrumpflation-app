import django_tables2 as tables
from .models import Purchase

class PurchaseTable(tables.Table):
    """ Benutzerdefinierte Tabelle festlegen
    Festlegen, welche Daten in die Tabelle in productDetail.html 
    übergeben werden.
    Übergebene Parameter: tables.Table
    """
    product__unit = tables.Column(verbose_name='Einheit')
    price_per_kg_or_l = tables.Column()

    class Meta:
        model = Purchase
        template_name = 'django_tables2/bootstrap.html'
        fields = ('purchase_date', 
                  'supermarket', 
                  'size', 
                  'product__unit', 
                  'price', 
                  'currency', 
                  'price_per_kg_or_l',)
        order_by = 'purchase_date'

    def render_product__unit(self, record):
        return record.product.unit

    def render_price_per_kg_or_l(self, record):
        return record.price_per_kg_or_l()

