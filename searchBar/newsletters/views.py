from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail,EmailMultiAlternatives
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm
from django.template.loader import get_template
from searchBarApp.models import industry
# Create your views here.

count_industries= industry.objects.all().count()
from_email = settings.EMAIL_HOST_USER
# count_users= NewsletterUser.objects.all().count()

def newsletter_signup(request):
    NewsletterUser2 = NewsletterUser.objects.all()
    count_users= NewsletterUser.objects.all().count()

    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit = False)

        if NewsletterUser.objects.filter(email = instance.email).exists():
            messages.warning(request,'Your Email already exists in our database',"alert alert-warning alert-dismissable")
        else:
            instance.save()
            messages.success(request,'Your Email  submitted to our database succesfully ',"alert alert-success alert-dismissable")
            subject = "Thank you for subscribing our newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            #rec_emails =NewsletterUser.objects.all()
        #    print(rec_emails)
        #    print(len(rec_emails))
        #    query_list = []


            #signup_message = """Welcome to visit+ newsletter.To UnSubscribe,Go To http://127.0.0.1:8000/newsletter/unsubscribe/"""
            #send_mail(subject=subject,from_email=from_email,recipient_list=to_email,message=signup_message,fail_silently=False)
            """"for ob in rec_emails:
                email = str(ob.email)
                query_list.append(email)

            if len(rec_emails) >=3:
                with open(settings.BASE_DIR + "/newsletters/templates/newsletters/sign_up_email.txt") as f:
                    signup_message = f.read()
                message = EmailMultiAlternatives(subject=subject,body=signup_message,from_email=from_email,to=query_list)
                html_template = get_template("newsletters/sign_up_email.html").render()
                message.attach_alternative(html_template,"text/html")
                message.send()
                """

            with open(settings.BASE_DIR + "/newsletters/templates/newsletters/sign_up_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject,body=signup_message,from_email=from_email,to=to_email)
            html_template = get_template("newsletters/sign_up_email.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()
            print("Thank u mail sent")

            if count_industries == 17:
                print("count_industries == 17 ,so sending emails to everyone indiviually")
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

    context ={
        'form':form,
        'NewsletterUser2':NewsletterUser2,
        'count':count_users,
    }

    return render(request,'newsletters/sign_up.html',context)

def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit = False)
        if NewsletterUser.objects.filter(email = instance.email).exists():
            NewsletterUser.objects.filter(email = instance.email).delete()
            messages.success(request,'Your Email removed from our database',"alert alert-success alert-dismissable")
            subject = "You have Unsubscribed to Visit+ Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            #signup_message = """Sorry to see you go let us know if there is an issue with our service.To Subscribe again,Go To http://127.0.0.1:8000/newsletter/sign_up/"""
            #send_mail(subject=subject,from_email=from_email,recipient_list=to_email,message=signup_message,fail_silently=False)
            with open(settings.BASE_DIR + "/newsletters/templates/newsletters/unsubscribe_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject,body=signup_message,from_email=from_email,to=to_email)
            html_template = get_template("newsletters/unsubscribe_email.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()

        else:
            messages.warning(request,'Your Email is not present in our database',"alert alert-warning alert-dismissable")
    context ={
        'form':form,
    }

    return render(request,'newsletters/unsubscribe.html',context)

def newsletter_signup_template(request):

    NewsletterUser2 = NewsletterUser.objects.all()
    count_users= NewsletterUser.objects.all().count()
    context ={
        'form':form,
        'NewsletterUser2':NewsletterUser2,
        'count':count_users,
    }

    return render(request,'newsletters/sign_up_email.html',context)

def New_Industry_Added(request):
    instance = industry.objects.all()
    context ={
        'instance':instance,
    }

    return render(request,'newsletters/New_Industry_Added.html',context)


# print(count_industries)

"""if count_users > 1 :
    print(" updates >16 indusries now sending emails",)
    subject_News = "New Industry added to the database"
    rec_emails =NewsletterUser.objects.all()
    print(rec_emails)
    print(len(rec_emails))
    query_list = []

    for ob in rec_emails:
        email = str(ob.email)
        query_list.append(email)
        with open(settings.BASE_DIR + "/newsletters/templates/newsletters/sign_up_email.txt") as f:
            signup_message = f.read()
        message = EmailMultiAlternatives(subject=subject_News,body=signup_message,from_email=from_email,to=query_list)
        html_template = get_template("newsletters/sign_up_email.html").render()
        message.attach_alternative(html_template,"text/html")
        message.send()
        query_list.pop()
"""
"""for query_email in query_list:
        print(query_email)
        query_email = str(query_email)
        with open(settings.BASE_DIR + "/newsletters/templates/newsletters/sign_up_email.txt") as f:
            signup_message = f.read()
        message = EmailMultiAlternatives(subject=subject_News,body=signup_message,from_email=from_email,to=query_email)
        #html_template = get_template("newsletters/sign_up_email.html").render()
        #message.attach_alternative(html_template,"text/html")
        message.send()
"""
