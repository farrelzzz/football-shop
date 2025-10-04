import uuid
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

class Author(models.Model):
    bio = models.TextField()
    books = models.ManyToManyRel(Book)
    user = models.OneToOneRel(User)