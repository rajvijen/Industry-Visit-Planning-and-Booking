from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Addition attributes
    name=models.CharField(max_length=200,blank=False,null=True)
    gender=models.CharField(max_length=200,blank=False,null=True)
    #dateofbirth=models.DateField(default=timezone.now())


    def __str__(self):
        return self.user.username
