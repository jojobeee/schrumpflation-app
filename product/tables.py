import django_tables2 as tables
from product.models import Purchase

class ProductHTMxTable(tables.Table):
    class Meta:
        model: Purchase
        template_name = "tables/bootstrap_htmx.html"