from django.db import models
import numpy as np
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class industry(models.Model):
    id_name=models.CharField(max_length=264)
    category=models.CharField(max_length=264,default='')
    image=models.ImageField(blank=True,null=True)
    location=models.CharField(max_length=528,default='')
    date=models.DateField(blank=True, null=True,default='')
    About=models.TextField(default='')

    def __str__(self):
        return self.id_name

class NewsletterEmail(models.Model):
    email=models.EmailField()


RATING_CHOICES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class Review(models.Model):
    industry_id = models.ForeignKey(industry,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)
    pub_date = models.DateTimeField(default=datetime.now)
    user_name = models.CharField(max_length=200)
    comment = models.CharField(max_length=500,null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5,null=True)


class AddToVisitLater(models.Model):
        industry_id = models.ForeignKey(industry,on_delete=models.CASCADE,null=True)
        user_id = models.ForeignKey(User,on_delete=models.PROTECT,null=True)
