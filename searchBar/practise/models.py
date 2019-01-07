from django.db import models

# Create your models here.
class Info(models.Model):
    Username = models.CharField(max_length = 100)
    Organisation = models.CharField(max_length = 50 , blank = True)
    date_visit = models.DateField()
    email = models.EmailField(null = True)

    def __str__(self):
        return '{} {} {}'.format(self.Username,self.date_visit,self.email)

CHOICES = (
   ('Very Good', "Very good"),
   ('Good', "good"),
   ('Bad', "Bad")
)

class feed(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    services = models.CharField(max_length = 15 , choices = CHOICES)
    Guide = models.CharField(max_length = 15, choices = CHOICES)
    Query = models.CharField(max_length = 300)

    def __str__(self):
        return "{}  {}  {} ".format(self.name,self.email,self.services,self.Guide,self.Query)

'''def feed_back(sender,**kwargs):
    if kwargs['created']:
        time.sleep(5)
        return redirect('Home')

post_save.connect(feed_back,sender = feed)
'''
