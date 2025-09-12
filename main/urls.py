from django.urls import path
from main.views import show_main, create_products, show_products

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-products/', create_products, name='create_products'),
    path('products/<str:id>/', show_products, name='show_products'),
]