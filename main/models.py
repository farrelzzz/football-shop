import uuid
from django.db import models
#from django.utils import timezone

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jerseys', 'Jerseys'),
        ('pants', 'Pants'),
        ('jackets', 'Jackets'),
        ('shoes', 'Shoes'),
        ('balls', 'Balls'),
    ]
    
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # title = models.CharField(max_length=255)
    # content = models.TextField()
    # category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    # thumbnail = models.URLField(blank=True, null=True)
    # news_views = models.PositiveIntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # is_featured = models.BooleanField(default=False)

    # Atribut Wajib
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)

    # Atribut Tambahan
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_iconic = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField(default=0)
#     persona = models.TextField()

    