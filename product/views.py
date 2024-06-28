from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Purchase, Brand, Supermarket

from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import CombinedAddSchrumpflationForm
from django.views.decorators.http import require_GET

import django_tables2 as tables
from django_tables2 import RequestConfig

from .tables import PurchaseTable


def product_detail(request, product_id):
    """ Auswahl der Produktdetails für Detailseite productDetail.html 
    Über die Produkt-ID werden die Informationen für das ausgewählte 
    Produkt gefiltert, um sie an die Tabelle zu übergeben.
    Der Spaltentitel von Preis/Verpackungsgröße wird dynamisch 
    angepasst, je nachdem, ob die Verpackungsgröße in Kilo oder Litern ist.
    Es werden Veränderungen des Preises, der Verpackungsgröße 
    und des Preises/Verpackungsgröße zwischen dem letzten Einkauf 
    und dem jetzigen Einkauf in Prozent berechnet.
    Zuletzt wird ein Graph erstellt, der die Informationen 
    Preis und Verpackungsgröße über die Zeit abbildet.
    Die übergebenen Parameter sind: request, product_id
    """

    product = get_object_or_404(Product, id=product_id)

    # Abfrage für Tabelle erstellen
    queryset = Purchase.objects.filter(product=product)
    
    # Dynamische Spaltentitel in der Tabelle
    if queryset.exists():
        if product.unit in ['kg', 'g']:
            column_title = 'Preis pro Kilo'
        elif product.unit in ['l', 'ml']:
            column_title = 'Preis pro Liter'
        else:
            column_title = 'Preis pro Einheit'

        class CustomPurchaseTable(PurchaseTable):
            # Klasse CustomPurchaseTable auf Basis der PurchaseTable erstellen
            price_per_kg_or_l = tables.Column(verbose_name=column_title)

            class Meta(PurchaseTable.Meta):
                # Meta-Daten festlegen
                model = Purchase
                template_name = 'django_tables2/bootstrap.html'
                fields = ('purchase_date', 'supermarket', 'size', 
                          'product__unit', 'price', 'currency', 
                          'price_per_kg_or_l')
                order_by = 'purchase_date'

            def render_price_per_kg_or_l(self, value, record):
                return record.price_per_kg_or_l()

        table = CustomPurchaseTable(queryset)
    else:
        table = PurchaseTable(queryset)
     
    RequestConfig(request).configure(table)

    # Berechnung der Preisaenderung
    # In absteigender Reihenfolge sortiert
    purchases = Purchase.objects.filter(product=product).order_by('-purchase_date') 
    
    price_change = None 
    if purchases.count() >= 2:
        previous_purchase = purchases[1]
        newest_purchase = purchases[0]
        change_p = ((newest_purchase.price - previous_purchase.price) 
                    / previous_purchase.price) * 100
        change_p_flag = 0
        
        # Negative Werte: - entfernen und Flag-Variable auf 1 setzen
        if change_p < 0:
            change_p = change_p * (-1)
            change_p_flag = 1
        
        price_change = { 'previous_date': previous_purchase.purchase_date, 
                        'newest_date': newest_purchase.purchase_date, 
                        'change_p': round(change_p, 2), 
                        'change_p_flag': change_p_flag }
    
    # Berechnung der Groessenaenderung
    size_change = None 
    if purchases.exists() and purchases.count() > 1:
        previous_purchase = purchases[1]
        newest_purchase = purchases[0]
        change_s = ((newest_purchase.size - previous_purchase.size) 
                    / previous_purchase.size) * 100
        change_s_flag = 0
        
        # Negative Werte: - entfernen und Flag-Variable auf 1 setzen
        if change_s < 0:
            change_s = change_s * (-1)
            change_s_flag = 1
        
        size_change = { 'previous_date': previous_purchase.purchase_date, 
                       'newest_date': newest_purchase.purchase_date, 
                       'change_s': round(change_s, 2), 
                       'change_s_flag': change_s_flag }
    
    # Berechnung der prozentualen Aenderung des Wertes Preis/Verpackungsgröße
    price_size_change = None 
    if purchases.exists() and purchases.count() > 1:
        previous_purchase = purchases[1]
        previous_p_s = previous_purchase.price_per_kg_or_l()
        newest_purchase = purchases[0]
        newest_p_s = newest_purchase.price_per_kg_or_l()
        change_p_s = ((newest_p_s - previous_p_s) 
                      / previous_p_s) * 100
        change_p_s_flag = 0
        
        # Negative Werte: - entfernen und Flag-Variable auf 1 setzen
        if change_p_s < 0:
            change_p_s = change_p_s * (-1)
            change_p_s_flag = 1
        
        price_size_change = { 'previous_date': previous_purchase.purchase_date, 
                             'newest_date': newest_purchase.purchase_date, 
                             'change_p_s': round(change_p_s, 2), 
                             'change_p_s_flag': change_p_s_flag }
    
    # Graph für productDetail.html erstellen
    graph_data = []

    if purchases.exists() and purchases.count() > 1:
        graph_data = [{
            'purchase_date': purchase.purchase_date.strftime('%Y-%m-%d'),
            'price_per_kg_or_l': str(purchase.price_per_kg_or_l()),
        } for purchase in purchases]

    # Kontextvariablen festlegen
    context = {'product': product, 
               'table': table, 
               'price_change': price_change, 
               'size_change': size_change, 
               'price_size_change': price_size_change, 
               'graph_data': graph_data}

    return render(request, 'product/productDetail.html', context)


def product_list(request):
    """ Abfrage der Daten für die Hauptseite der App
    Die Suchabfrage wird erstellt.
    Alle oder nur die gefilterten Produkte werden in 
    eine Tabelle übergeben.
    Es wird die Paginierung der Produkttabelle festgelegt.
    Außerdem wird hier eine Abfrage nach den fünf größten 
    Schrumpflationen eingefügt.
    Der übergebene Parameter ist: request
    """

    # Suchabfrage
    search_query = request.GET.get('search', '')
    brand_filter = request.GET.get('brand', '')
    product_type_filter = request.GET.get('product_type', '')

    if search_query:
        product_list = Product.objects.filter(
            Q(name__icontains=search_query) | 
            Q(brand__name__icontains=search_query) |
            Q(product_type__icontains=search_query)
        )
    else:
        product_list = Product.objects.all()

    if brand_filter:
        product_list = product_list.filter(brand__name__icontains=brand_filter)

    if product_type_filter:
        product_list = product_list.filter(product_type__icontains=product_type_filter)

    product_list = product_list.order_by('id')

    # Paginierung festlegen
    paginator = Paginator(product_list, 8)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    brands = Product.objects.filter(
        Q(name__icontains=search_query) | 
        Q(brand__name__icontains=search_query) |
        Q(product_type__icontains=search_query)
    ).values_list('brand__name', flat=True).distinct()

    product_types = Product.objects.filter(
        Q(name__icontains=search_query) | 
        Q(brand__name__icontains=search_query) |
        Q(product_type__icontains=search_query)
    ).values_list('product_type', flat=True).distinct()


    # Erfassung der fünf größten Shrumpflationswerte
    purchases = Purchase.objects.all()
    shrinkflations = []

    # Erstellen einer Sammlung, in der jedes Element 
    # (hier: Kaufelement) nur ein Mal vorkommen kann
    products_set = set()   

    for purchase in purchases:
        product = purchase.product

        if product not in products_set:
            related_purchases = Purchase.objects.filter(product=product).order_by('-purchase_date')
            
            if related_purchases.count() > 1:
                newest_purchase = related_purchases[0]
                newest_p_s = newest_purchase.price_per_kg_or_l()
                previous_purchase = related_purchases[1]
                previous_p_s = previous_purchase.price_per_kg_or_l()
                
                if previous_p_s > 0:
                    shrinkflation_p_s = ((newest_p_s - previous_p_s) 
                                         / previous_p_s) * 100
                    shrinkflations.append({ 'product': product,
                                           'previous_date': previous_purchase.purchase_date,
                                            'newest_date': newest_purchase.purchase_date,
                                            'shrinkflation_p_s': round(shrinkflation_p_s, 2) })
            products_set.add(product)

    # Sortieren der Schrumpflationswerte 
    for i in range(len(shrinkflations)):
        for j in range(i + 1, len(shrinkflations)):
            if shrinkflations[i]['shrinkflation_p_s'] < shrinkflations[j]['shrinkflation_p_s']:
                shrinkflations[i], shrinkflations[j] = shrinkflations[j], shrinkflations[i]
    
    # Auswahl der fünf größten Werte
    largest_shrinkflations = shrinkflations[:5]

    return render(request, 'product/index.html', {
        'products': products,
        'brands': brands,
        'product_types': product_types,
        'selected_brand': brand_filter,
        'selected_product_type': product_type_filter,
        'search_query': search_query,
        'largest_shrinkflations': largest_shrinkflations
    })


def add_purchase(request):
    """ Neuen Einkauf ergänzen
    Es wird ein Formulat erstellt, um neue Einkäufe ergänzen zu können.
    Der übergebene Parameter ist: request
    """
    if request.method == 'POST':
        form = CombinedAddSchrumpflationForm(request.POST)
        
        if form.is_valid():
            # Marke vorhanden oder neue Marke hinzufügen
            brand = form.cleaned_data['existing_brand']
            if not brand and form.cleaned_data['new_brand']:
                brand, created = Brand.objects.get_or_create(name=form.cleaned_data['new_brand'])
            
            # Supermarkt vorhanden oder neuen Supermarkt hinzufügen
            supermarket = form.cleaned_data['existing_supermarket']
            if not supermarket and form.cleaned_data['new_supermarket']:
                supermarket, created = Supermarket.objects.get_or_create(name=form.cleaned_data['new_supermarket'])
            
            # Produkt vorhanden oder neues Produkt hinzufügen
            product_name = form.cleaned_data['product_name']
            product = Product.objects.filter(name=product_name).first()
            if not product:
                product = Product.objects.create(
                    name=product_name,
                    brand=brand,
                    product_type=form.cleaned_data['new_product_type'],
                    unit=form.cleaned_data['unit']
                )
            
            Purchase.objects.create(
                product=product,
                supermarket=supermarket,
                size=form.cleaned_data['size'],
                price=form.cleaned_data['price'],
                currency=form.cleaned_data['currency'],
                purchase_date=form.cleaned_data['purchase_date']
            )
            
            return redirect('product:index')
    else:
        form = CombinedAddSchrumpflationForm()

    # Alphabetisch sortieren
    brands = Brand.objects.all().order_by('name')
    supermarkets = Supermarket.objects.all().order_by('name')

    return render(request, 'product/add_purchase.html', {
        'form': form,
        'brands': brands,
        'supermarkets': supermarkets
    })


@require_GET
def autocomplete_products(request):
    """ Autocomplete bei bekanntem Produkt
    Nur bei GET-Anfragen ausführen 
    Der übergebene Parameter ist: request
    """
    if 'term' in request.GET:
        qs = Product.objects.filter(name__icontains=request.GET.get('term'))
        products = list(qs.values_list('name', flat=True))
        return JsonResponse(products, safe=False)
    return JsonResponse([], safe=False)

@require_GET
def product_details(request):
    """ Sucht in der Datenbank nach einem Produkt,
    das dem über den GET-Parameter 'product_name' übergebenen Namen entspricht
    und gibt die Produktinformationen als JSON zurück. Diese werden benutzt, um
    in add_purchase.html die Felder für Produkttyp, Marke und Einheit bei einem
    bereits existierenden Produkt zu füllen.
    Der übergebene Parameter ist: request
    """
    product_name = request.GET.get('product_name', None)
    if product_name:
        product = Product.objects.filter(name__iexact=product_name).first()
        
        if product:
            return JsonResponse({
                'product_type': product.product_type,
                'brand_id': product.brand.id if product.brand else None,
                'brand_name': product.brand.name if product.brand else '',
                'unit': product.unit
            })
    return JsonResponse({}, status=400)

