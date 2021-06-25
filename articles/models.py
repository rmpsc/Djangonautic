from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    # auto_now_add automatically adds in a date
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later

    # what displays in ORM
    def __str__(self):
        return self.title