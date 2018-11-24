from django.db import models
import numpy as np
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User

class Industry(models.Model):
    industry_id = models.CharField(max_length=30,null=False)

    def __str__(self):
        id = self.industry_id
        return (id)

RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class Review(models.Model):
    industry_id = models.ForeignKey(Industry,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.now)
    user_name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200,null=True)
    rating = models.IntegerField(choices=RATING_CHOICES)


