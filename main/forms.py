from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "thumbnail", "price", "stock", "is_iconic", "is_featured"]

# class CarForm(ModelForm):
#     class Meta:
#         model = Car
#         fields = ["name", "brand", "stock"]