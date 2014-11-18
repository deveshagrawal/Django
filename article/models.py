from django.db import models
from django.utils import timezone

# Create your models here.
class ArticleObj(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=20)
    bodytext = models.TextField()
    hero_image = models.ImageField(upload_to="static/images/", default='anonymous.png')

def publish(self):
    self.publication_date = timezone.now()
    self.save()

def __str__(self):
    return self.title