from django.core.management.base import BaseCommand
from product.models import Supermarket, Brand, Product, Purchase
from datetime import date

class Command(BaseCommand):
    """ Datenbank mit Beispieldaten befüllen """

    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        print("Starting database population...")

        Supermarket.objects.all().delete()
        Brand.objects.all().delete()
        Product.objects.all().delete()
        Purchase.objects.all().delete()

        supermarkets = [
            Supermarket(name='Edeka'),
            Supermarket(name='Rewe'),
            Supermarket(name='Aldi'),
            Supermarket(name='Lidl'),
            Supermarket(name='Kaufland'),
            Supermarket(name='DM'),
            Supermarket(name='Penny'),
        ]
        Supermarket.objects.bulk_create(supermarkets)
        print("Supermarkets created")

        brands = [
            Brand(name='Ory'),
            Brand(name='Garnier'),
            Brand(name='Marabou'),
            Brand(name='Pringles'),
            Brand(name='Neutrogena'),
            Brand(name='Naturgut'),
            Brand(name="Gaudas's Glorie"),
            Brand(name='Lorenz'),
            Brand(name='Edeka Bio'),
            Brand(name='Lipton'),
            Brand(name='Haribo'),
        ]
        Brand.objects.bulk_create(brands)
        print("Brands created")

        products = [
            Product(name='Milchreis', product_type="Milchreis", brand=Brand.objects.get(name='Ory'), unit='g'),
            Product(name='Fructis Shampoo', product_type="Shampoo", brand=Brand.objects.get(name='Garnier'), unit='ml'),
            Product(name='Fructis Spülung', product_type="Spülung", brand=Brand.objects.get(name='Garnier'), unit='ml'),
            Product(name='Mjölkchoklad', product_type="Schokolade", brand=Brand.objects.get(name='Marabou'), unit='g'),
            Product(name='Pringles - versch. Sorten', product_type="Chips", brand=Brand.objects.get(name='Pringles'), unit='g'),
            Product(name='Deep Moisture', product_type="Bodylotion", brand=Brand.objects.get(name='Neutrogena'), unit='ml'),
            Product(name='Babyspinat', product_type="Babyspinat", brand=Brand.objects.get(name='Naturgut'), unit='g'),
            Product(name="Sweet Onion Sauce", product_type="Sauce", brand=Brand.objects.get(name="Gaudas's Glorie"), unit='ml'),
            Product(name='Snack-Hits', product_type="Chips", brand=Brand.objects.get(name='Lorenz'), unit='g'),
            Product(name='Kürbiskernbrötchen', product_type="Brot", brand=Brand.objects.get(name='Edeka Bio'), unit='g'),
            Product(name='Lipton Ice Tea', product_type="Eistee", brand=Brand.objects.get(name='Lipton'), unit='l'),
            Product(name='Party Box - Phantasia', product_type="Süßigkeiten", brand=Brand.objects.get(name='Haribo'), unit='g'),
        ]

        Product.objects.bulk_create(products)
        print("Products created")

        purchases = [
            Purchase(product=Product.objects.get(name='Milchreis'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=500, price=1.79, currency='EUR', purchase_date=date(2023, 6, 1)),
            Purchase(product=Product.objects.get(name='Milchreis'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=400, price=1.79, currency='EUR', purchase_date=date(2023, 6, 15)),
            Purchase(product=Product.objects.get(name='Fructis Shampoo'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=300, price=2.29, currency='EUR', purchase_date=date(2022, 3, 9)),
            Purchase(product=Product.objects.get(name='Fructis Shampoo'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=250, price=2.49, currency='EUR', purchase_date=date(2023, 6, 14)),
            Purchase(product=Product.objects.get(name='Fructis Spülung'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=250, price=2.29, currency='EUR', purchase_date=date(2022, 3, 9)),
            Purchase(product=Product.objects.get(name='Fructis Spülung'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=200, price=2.49, currency='EUR', purchase_date=date(2023, 6, 14)),
            Purchase(product=Product.objects.get(name='Mjölkchoklad'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=250, price=3.99, currency='EUR', purchase_date=date(2023, 1, 9)),
            Purchase(product=Product.objects.get(name='Mjölkchoklad'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=220, price=3.99, currency='EUR', purchase_date=date(2023, 6, 10)),
            Purchase(product=Product.objects.get(name='Pringles - versch. Sorten'), supermarket=Supermarket.objects.get(name='Kaufland'),
                     size=200, price=2.99, currency='EUR', purchase_date=date(2022, 10, 11)),
            Purchase(product=Product.objects.get(name='Pringles - versch. Sorten'), supermarket=Supermarket.objects.get(name='Kaufland'),
                     size=185, price=2.99, currency='EUR', purchase_date=date(2023, 3, 10)),
            Purchase(product=Product.objects.get(name='Pringles - versch. Sorten'), supermarket=Supermarket.objects.get(name='Kaufland'),
                     size=165, price=2.99, currency='EUR', purchase_date=date(2024, 6, 8)),
            Purchase(product=Product.objects.get(name='Deep Moisture'), supermarket=Supermarket.objects.get(name='DM'),
                     size=400, price=4.95, currency='EUR', purchase_date=date(2023, 11, 18)),
            Purchase(product=Product.objects.get(name='Deep Moisture'), supermarket=Supermarket.objects.get(name='DM'),
                     size=250, price=3.95, currency='EUR', purchase_date=date(2024, 5, 28)),
            Purchase(product=Product.objects.get(name='Babyspinat'), supermarket=Supermarket.objects.get(name='Penny'),
                     size=150, price=1.89, currency='EUR', purchase_date=date(2022, 4, 7)),
            Purchase(product=Product.objects.get(name='Babyspinat'), supermarket=Supermarket.objects.get(name='Penny'),
                     size=125, price=1.89, currency='EUR', purchase_date=date(2023, 5, 14)),
            Purchase(product=Product.objects.get(name='Babyspinat'), supermarket=Supermarket.objects.get(name='Penny'),
                     size=100, price=1.89, currency='EUR', purchase_date=date(2024, 6, 15)),
            Purchase(product=Product.objects.get(name='Sweet Onion Sauce'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=650, price=3.99, currency='EUR', purchase_date=date(2022, 7, 25)),
            Purchase(product=Product.objects.get(name='Sweet Onion Sauce'), supermarket=Supermarket.objects.get(name='Rewe'),
                     size=550, price=3.99, currency='EUR', purchase_date=date(2024, 4, 5)),
            Purchase(product=Product.objects.get(name='Snack-Hits'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=320, price=3.49, currency='EUR', purchase_date=date(2022, 9, 13)),
            Purchase(product=Product.objects.get(name='Snack-Hits'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=280, price=3.49, currency='EUR', purchase_date=date(2024, 5, 5)),
            Purchase(product=Product.objects.get(name='Kürbiskernbrötchen'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=300, price=2.89, currency='EUR', purchase_date=date(2024, 5, 6)),
            Purchase(product=Product.objects.get(name='Kürbiskernbrötchen'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=320, price=2.89, currency='EUR', purchase_date=date(2024, 1, 5)),
            Purchase(product=Product.objects.get(name='Lipton Ice Tea'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=1.5, price=1.29, currency='EUR', purchase_date=date(2023, 10, 19)),
            Purchase(product=Product.objects.get(name='Lipton Ice Tea'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=1.25, price=1.29, currency='EUR', purchase_date=date(2024, 3, 21)),
            Purchase(product=Product.objects.get(name='Party Box - Phantasia'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=1000, price=4.99, currency='EUR', purchase_date=date(2020, 2, 27)),
            Purchase(product=Product.objects.get(name='Party Box - Phantasia'), supermarket=Supermarket.objects.get(name='Edeka'),
                     size=750, price=6.29, currency='EUR', purchase_date=date(2024, 5, 11)),
        ]
        Purchase.objects.bulk_create(purchases)
        print("Purchases created")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))
