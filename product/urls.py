from . import views
from django.urls import path

app_name = 'product'
urlpatterns = [
    path('', views.product_list, name='index'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
