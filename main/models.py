import uuid
from django.db import models

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
    # news_views = models.PositiveIntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)

    ##
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_iconic = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()