from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Addition attributes
    name=models.CharField(max_length=200,blank=False,null=True)
    gender=models.CharField(max_length=200,blank=False,null=True)
    image = models.ImageField(default='media/default.jpg', upload_to='profile_pics',null=True)

    #dateofbirth=models.DateField(default=timezone.now())


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):                       # It(**kwargs) does overridden
        super(UserProfileInfo, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
