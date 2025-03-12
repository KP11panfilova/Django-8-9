from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField()
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
