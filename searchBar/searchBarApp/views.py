from django.shortcuts import render,get_object_or_404,redirect
from .models import industry,Review
from . import forms
from searchBarApp.forms import NewsletterForm,AddToVisitLaterForm
from templated_email import get_templated_mail
from django.core.mail import EmailMessage
from newsletters.models import NewsletterUser
from newsletters.forms import NewsletterUserSignUpForm
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import industry
from . import forms
from searchBarApp.forms import NewsletterForm
from templated_email import get_templated_mail
from django.core.mail import EmailMessage
from newsletters.models import NewsletterUser
from newsletters.forms import NewsletterUserSignUpForm
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail,EmailMultiAlternatives
from newsletters.forms import NewsletterUserSignUpForm
from django.template.loader import get_template
from searchBarApp.models import AddToVisitLater
# Create your views here.

queryset = industry.objects.all()

queryset2 = industry.objects.filter(category__contains="Manufacturing")

queryset3 = industry.objects.filter(category__contains="Automobile")

queryset4 = industry.objects.filter(category__contains="Assembling")

queryset5 = industry.objects.filter(category__contains="IT Companies")

context = {
    "objects" : queryset,
    "objects2" : queryset2,
    "objects3":queryset3,
    "objects4":queryset4,
    "objects5":queryset5,

}

count_industries= industry.objects.all().count()
from_email = settings.EMAIL_HOST_USER
#count_users= NewsletterUser.objects.all().count()



def index(request):
    queryset = industry.objects.all()
    queryset2 = industry.objects.filter(category__contains="Manufacturing")
    queryset3 = industry.objects.filter(category__contains="Automobile")
    queryset4 = industry.objects.filter(category__contains="Assembling")
    queryset5 = industry.objects.filter(category__contains="IT Companies")

    form_newslet=NewsletterUserSignUpForm(request.POST or None)

    if form_newslet.is_valid():
        instance = form_newslet.save(commit = False)

        if NewsletterUser.objects.filter(email = instance.email).exists():
            messages.warning(request,'Your Email already exists in our database',"alert alert-warning alert-dismissable")
        else:
            instance.save()
            messages.success(request,'Your Email  submitted to our database succesfully ',"alert alert-success alert-dismissable")
            subject = "Thank you for subscribing our newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]


            with open(settings.BASE_DIR + "/newsletters/templates/newsletters/sign_up_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject,body=signup_message,from_email=from_email,to=to_email)
            html_template = get_template("newsletters/sign_up_email.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()
            print("Thank u mail sent")

    context2 = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,
        "form_newslet":form_newslet,
    }
    return render(request,'searchBarApp/index.html',context2)





def result(request,name=None):

    queryset = industry.objects.all()
    queryset2 = industry.objects.filter(category__contains="Manufacturing")
    queryset3 = industry.objects.filter(category__contains="Automobile")
    queryset4 = industry.objects.filter(category__contains="Assembling")
    queryset5 = industry.objects.filter(category__contains="IT Companies")

    query = request.POST['query']
    temp = query.upper()
    k=404

    for object in queryset:
        if object.id_name.upper() == temp:
            k = object.id

    #test = industry.objects.get(pk=k)
    #related = industry.objects.filter(category=test.category)
    #no_related = industry.objects.filter(category=test.category).count()
    #rel_location = industry.objects.filter(category = test.location)
    #no_rel_location = industry.objects.filter(category = test.location).count()


    if(k==404):
        k = None
        context1 = {
            "key" : False,
            "objects" : queryset,
            "objects2" : queryset2,
            "objects3":queryset3,
            "objects4":queryset4,
            "objects5":queryset5,
        }
    else:

        test = industry.objects.get(pk=k)
        related = industry.objects.filter(category=test.category)
        no_related = industry.objects.filter(category=test.category).count()
        rel_location = industry.objects.filter(category = test.location)
        no_rel_location = industry.objects.filter(category = test.location).count()

        context1 = {

            "instances" : industry.objects.filter(id_name=query),#get_object_or_404(industry, id=k),
            "objects" : queryset,
            "objects2" : queryset2,
            "objects3":queryset3,
            "objects4":queryset4,
            "objects5":queryset5,
            "related" : related,
            "no_related" : no_related,
            "rel_location" : rel_location,
            "no_rel_location" : no_rel_location,
            "key" : True
                }
    return render(request,'searchBarApp/search.html',context1)

def showIndustry(request, ind_id):
    searched_industry = get_object_or_404(industry, id=ind_id)
    queryset = industry.objects.all()
    queryset2 = industry.objects.filter(category__contains="Manufacturing")
    queryset3 = industry.objects.filter(category__contains="Automobile")
    queryset4 = industry.objects.filter(category__contains="Assembling")
    queryset5 = industry.objects.filter(category__contains="IT Companies")
    count_industries= industry.objects.all().count()

    ind_status = True
    for industry1 in AddToVisitLater.objects.all():
        if industry1.industry_id == searched_industry:
            ind_status = False
    
    #Suggestion to users
    present_industry=industry.objects.get(pk=ind_id)
    category_industries=industry.objects.filter(category=present_industry.category)
    #End of Suggestions to users

    
    context3 = {
        'instance':searched_industry,
        #"instances" : industry.objects.filter(id_name=query),#get_object_or_404(industry, id=k),
        "ind_status" : ind_status,
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,
        "category_industries":category_industries,
        "count_industries":count_industries,
        "reviews": Review.objects.filter(industry_id = ind_id),
        "no_r": Review.objects.filter(industry_id = ind_id).count(),

    }
    return render(request, 'searchBarApp/result.html', context3)




def Assembling(request,name=None):
    return render(request,'searchBarApp/Assembling.html',context)

def Automobiles(request,name=None):
    return render(request,'searchBarApp/Automobiles.html',context)

def Manufacturing(request,name=None):
    return render(request,'searchBarApp/Manufacturing.html',context)

def IT_Companies(request,name=None):
    return render(request,'searchBarApp/IT_Companies.html',context)

def base(request):
    return render(request,'searchBarApp/base.html',context)

def contact(request):
    return render(request,'searchBarApp/contact.html',context)

def blog(request):
    return render(request,'searchBarApp/blog.html',context)

def faq(request):
    return render(request,'searchBarApp/faq.html',context)
#         add_form=AddToVisitLaterForm()

def about(request):
    return render(request,'searchBarApp/about.html',context)

def services(request):
    return render(request,'searchBarApp/services.html',context)

def read(request):
    return render(request,'searchBarApp/read.html',context)

def users(request):

    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR Not Valid')
    else:
            form=NewsletterForm()

    return render(request,'searchBarApp/read.html',{'form':form})

#Function used for Review app
def AddReview(request):
    if request.method == 'POST':    
        ind= request.POST['ind']
        ind = industry.objects.filter(id_name=ind).first()
        user_name_count=Review.objects.filter(user_id=request.user).filter(industry_id=ind).count()

        if (user_name_count == 0):
            newReview = Review()
            newReview.industry_id = ind
            newReview.user_id = request.user
            newReview.user_name = request.user.username
            newReview.comment = request.POST['comment']
            newReview.rating = int(request.POST.get('rating', 5))

            if newReview.rating == 0:
                newReview.rating=5
            else: 
                newReview.rating = int(request.POST.get('rating', 5))
            
            newReview.save()
            null = True
            return redirect(reverse('searchBarApp:industry',kwargs={"ind_id":ind.id}))
        elif(user_name_count == 1):
            update_review=Review.objects.filter(user_id=request.user).filter(industry_id=ind)
            for r in update_review:
                r.comment=request.POST['comment']
                r.rating=int(request.POST.get('rating', 5))
                r.save()
            return redirect(reverse('searchBarApp:industry',kwargs={"ind_id":ind.id}))
    else:
        return redirect(reverse('searchBarApp:industry',kwargs={"ind_id":ind.id}))


# def addToVisitLater(request,ind_id):
#
#     if request.method=="POST":
#
#         industry_id1=industry.objects.get(pk=ind_id)    ind_status = True
#     for industry1 in AddToVisitLater.objects.all():
#         if industry1.industry_id == industry_id1:
#             ind_status = False
# #         user_id1=request.user
#         print(industry_id1)
#         print(user_id1)
#
#         p = AddToVisitLater.objects.create(industry_id=industry_id1,user_id=user_id1)
#         p.save()
#         return redirect("basicapp:profile")
#
#    ind_status = True
    # for industry1 in AddToVisitLater.objects.all():
    #     if industry1.industry_id == industry_id1:
    #         ind_status = False
#     else:
#         print("Else2")
#         add_form=AddToVisitLaterForm()
#         return redirect("basicapp:profile")


def addToVisitLater(request,ind_id):
    industry_id1=industry.objects.get(pk=ind_id)
    user_id1=request.user
    count=AddToVisitLater.objects.filter(user_id=request.user).filter(industry_id=industry_id1).count()

    if (count >= 1):
            return redirect(reverse("searchBarApp:industry",kwargs={'ind_id':ind_id}))
    else:
        p = AddToVisitLater.objects.create(industry_id=industry_id1,user_id=user_id1)
        p.save()
        return redirect(reverse("searchBarApp:industry",kwargs={'ind_id':ind_id}))
