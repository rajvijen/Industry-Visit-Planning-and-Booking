from django.db import models

# Create your models here.

class industry(models.Model):
    id_name=models.CharField(max_length=264,unique=True)
    category=models.CharField(max_length=264,default='')
    image=models.ImageField(blank=True,null=True)
    location=models.CharField(max_length=528,default='')
    date=models.DateField(blank=True, null=True,default='')
    About=models.TextField(default='')

    def __str__(self):
        return self.id_name
