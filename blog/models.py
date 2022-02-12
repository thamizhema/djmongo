from django.db import models

# Create your models here.
from django.utils import timezone

# Create your models here.
class AddPost(models.Model):
    title = models.CharField(max_length=20,default='title')
    content = models.TextField(default='test')
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    

# Create your models here.
class IMG(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents/', null=True)
    def __str__(self):
        return self.title


    
