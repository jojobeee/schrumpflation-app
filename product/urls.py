from . import views
from django.urls import path
#from .views import PurchaseListView

app_name = 'product'
urlpatterns = [
    path('', views.product_list, name='index'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    #path('product/<int:product_id>/', PurchaseListView.as_view(), name='productDetail'),
]
