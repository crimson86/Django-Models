from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body=  models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date  = models.DateTimeField(auto_now_add=True)
    # add in author later