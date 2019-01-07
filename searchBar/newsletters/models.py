from django.db import models
from searchBarApp.models import industry
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail,EmailMultiAlternatives
#from .forms import NewsletterUserSignUpForm
from django.template.loader import get_template
from django.db.models.signals import pre_save,post_delete

# Create your models here.

class NewsletterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.email



count_industries= industry.objects.all().count()
from_email = settings.EMAIL_HOST_USER

def Send_Email(sender,**kwargs):
        print("NewIndustry Added ,so sending emails to everyone indiviually from models ")
        subject_News = "New Industry added to the database"
        rec_emails =NewsletterUser.objects.all()
        print(rec_emails)
        print(len(rec_emails))
        query_list = []

        for ob in rec_emails:
            email = str(ob.email)
            query_list.append(email)
            with open(settings.BASE_DIR + "/newsletters/templates/newsletters/New_Industry_Added.txt") as f:
                signup_message = f.read()
            print("Newsletters Sending to",query_list)
            message = EmailMultiAlternatives(subject=subject_News,body=signup_message,from_email=from_email,to=query_list)
            html_template = get_template("newsletters/New_Industry_Added.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()
            print("Newsletters Sent to",query_list)
            query_list.pop()

        print("Newsletters Sent to all!!")


def Send_Email2(sender,**kwargs):
        print("Industry deleted ,so sending emails to everyone indiviually from models ")
        subject_News = " Industry deleted from  database"
        rec_emails =NewsletterUser.objects.all()
        print(rec_emails)
        print(len(rec_emails))
        query_list = []

        for ob in rec_emails:
            email = str(ob.email)
            query_list.append(email)
            with open(settings.BASE_DIR + "/newsletters/templates/newsletters/Industry_Deleted.txt") as f:
                signup_message = f.read()
            print("Newsletters Sending to",query_list)
            message = EmailMultiAlternatives(subject=subject_News,body=signup_message,from_email=from_email,to=query_list)
            html_template = get_template("newsletters/Industry_Deleted.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()
            print("Newsletters Sent to",query_list)
            query_list.pop()
        print("Newsletters Sent to all!!")

pre_save.connect(Send_Email,sender=industry)
post_delete.connect(Send_Email2,sender=industry)









class Newsletter(models.Model):
    EMAIL_STATUS_CHOICES = (
        ('Draft','Draft'),
        ('Published','Published')
    )

    subject = models.CharField(max_length=250)
    body =  models.TextField()
    email = models.ManyToManyField(NewsletterUser)
    status = models.CharField(max_length=10, choices = EMAIL_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def _str_(self):
        return self.subject
