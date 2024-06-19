from django.core.management.base import BaseCommand
from product.models import Supermarket, Brand, Product, Purchase
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        print("Starting database population...")

        Supermarket.objects.all().delete()
        Brand.objects.all().delete()
        Product.objects.all().delete()
        Purchase.objects.all().delete()

        supermarkets = [
            Supermarket(name='Edeka', address='Teststr. 1', city='Berlin', postal_code='10963', country='Deutschland'),
            Supermarket(name='Rewe', address='Teststr. 2', city='Frankfurt', postal_code='60311', country='Deutschland'),
            Supermarket(name='Aldi', address='Teststr. 3', city='München', postal_code='80336', country='Deutschland'),
            Supermarket(name='Lidl', address='Teststr. 4', city='Köln', postal_code='50672', country='Deutschland')
        ]
        Supermarket.objects.bulk_create(supermarkets)
        print("Supermarkets created")

        brands = [
            Brand(name='Ory'),
            Brand(name='Garnier'),
            Brand(name='Marabou'),
        ]
        Brand.objects.bulk_create(brands)
        print("Brands created")

        products = [
            Product(name='Milchreis', brand=Brand.objects.get(name='Ory')),
            Product(name='Fructis Shampoo', brand=Brand.objects.get(name='Garnier')),
            Product(name='Fructis Spülung', brand=Brand.objects.get(name='Garnier')),
            Product(name='Mjölkchoklad', brand=Brand.objects.get(name='Marabou')),
        ]
        Product.objects.bulk_create(products)
        print("Products created")

        purchases = [
            Purchase(product=Product.objects.get(name='Milchreis'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=500, unit='g', price=1.79, currency='EUR', purchase_date=date(2023, 6, 1)),
            Purchase(product=Product.objects.get(name='Milchreis'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=400, unit='g', price=1.79, currency='EUR', purchase_date=date(2023, 6, 15)),
            Purchase(product=Product.objects.get(name='Fructis Shampoo'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=300, unit='ml', price=2.29, currency='EUR', purchase_date=date(2022, 3, 9)),
            Purchase(product=Product.objects.get(name='Fructis Shampoo'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=250, unit='ml', price=2.49, currency='EUR', purchase_date=date(2023, 6, 14)),
            Purchase(product=Product.objects.get(name='Fructis Spülung'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=250, unit='ml', price=2.29, currency='EUR', purchase_date=date(2022, 3, 9)),
            Purchase(product=Product.objects.get(name='Fructis Spülung'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=200, unit='ml', price=2.49, currency='EUR', purchase_date=date(2023, 6, 14)),
            Purchase(product=Product.objects.get(name='Mjölkchoklad'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=250, unit='g', price=3.99, currency='EUR', purchase_date=date(2023, 1, 9)),
            Purchase(product=Product.objects.get(name='Mjölkchoklad'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=220, unit='g', price=3.99, currency='EUR', purchase_date=date(2023, 6, 10)),   
        ]
        Purchase.objects.bulk_create(purchases)
        print("Purchases created")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))
