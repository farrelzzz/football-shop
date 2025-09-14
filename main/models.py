import uuid
from django.db import models
#from django.utils import timezone

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jerseys', 'Jerseys'),
        ('shoes', 'Shoes'),
        ('socks', 'Socks'),
        ('balls', 'Balls'),
        ('bags', 'Bags'),
    ]
    
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # title = models.CharField(max_length=255)
    # content = models.TextField()
    # category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    # thumbnail = models.URLField(blank=True, null=True)
    # news_views = models.PositiveIntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # is_featured = models.BooleanField(default=False)

    ##
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_iconic = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    products_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_products_hot(self):
        return self.products_views > 20
        
    def increment_views(self):
        self.products_views += 1
        self.save()

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField(default=0)
#     persona = models.TextField()

    