from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:item_id>/', views.item, name='item'),
]
