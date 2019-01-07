from django.shortcuts import render,redirect,get_object_or_404 #Also importing redirect
from basicapp.forms import UserForm,UserProfileInfoForms,UpdateProfile,UpdateUser


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#Importing modules for creating email conformation
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from basicapp.tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import datetime

from booking.models import BookingListIndi

#End of models for email conformation


#Models used for stripe payment
import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
#End of models for stripe


#Used for add to visit later
from searchBarApp.models import AddToVisitLater
#End of add to visit later


#setting API key for stripe
stripe.api_key = settings.STRIPE_SECRET_KEY # new



def index(request):
    return render(request,"basicapp/index.html")

@login_required
def special(request):
    return HttpResponse("Logged in success,Nice...")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def register(request):

    #registered=False

    if request.method == "POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForms(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():


            user=user_form.save(commit=False)
            user.set_password(user.password)
            user.is_active=False#User cant login without email conformation
            user.save()

            #Email verification activity starts
            current_site=get_current_site(request)#It checks if current site is present in domain or not
            mail_subject='Activate your account' #Subject of the mail that we are sending
            message=render_to_string('basicapp/acc_active_email.html',{'user':user,    #Email message created by a template acc_active_email.html this template creates email body with activation link that will send for application
                                     'domain':current_site.domain,# domain-type in a web address, e.g., www.jimsbikes.com, your Internet Service Provider views the DNS associated with the domain name, translates it into a machine friendly IP address (for example 216.168.224.70 is the IP for jimsbikes.com) and directs your Internet connection to the correct website.
                                     'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),#encodes a byte string in base64 for use in URL,stripping any trailing equal signs &&&&& and user.pk gives user.id.In django2.0 we also need to call decode() after encode.
                                     'token':account_activation_token.make_token(user)})
            to_email=user_form.cleaned_data.get('email')
            email=EmailMessage(mail_subject,message,to=[to_email])#creating email message
            email.send() #Sending Email
            print("Email Sent")

            #views for user_profile_info
            profile=profile_form.save(commit=False)
            profile.user=user #Since it has OneToOne relationship.Mentioned in the models

            profile.save()
                #views for user profile info ends here


            return render(request,"basicapp/confirm_email.html")



            #registered=True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForms()

    return render(request,"basicapp/registration.html",{"user_form":user_form,
                                                        "profile_form":profile_form})



def activate(request,uidb64,token): #creating a function for activating emailID
    try:
        uid=force_text(urlsafe_base64_decode(uidb64)) #decoding uidb64 which we sent through email
        user=User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):#When the mentioned errors are made
        user=None

    if user is not None and account_activation_token.check_token(user,token):# if user is none and token is checked via tokens.property
        user.is_active=True #Activating the account
        user.save()
        login(request,user)

        return render(request,"searchBarApp/index.html")

    else:
        return HttpResponse("Activation link is INVALID!!!")




def user_login(request):
    if request.method == "POST":
        username=request.POST.get("username") #username is the name of the "input field" and we are using "get" method because it is just a simple form
        password=request.POST.get("password") #Getting the password and the above method is done

        user=authenticate(username=username,password=password) # It authenticates the user for us.

        if user:
            if user.is_active:# checking if user is active or not
                login(request,user)#Logging in user
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE')
        else:
            print("Someone tried to login and failed")
            print("username:{} and password:{}".format(username,password))
            return render(request,"basicapp/invalid.html")
    else:
        return render(request,"basicapp/login.html")



@login_required
def profile(request):
    user_form=UpdateUser(instance=request.user)
    profile_form=UpdateProfile(instance=request.user.userprofileinfo)

    return render(request,"basicapp/profile.html",{'user_form':user_form,'profile_form':profile_form})


@login_required
def update(request):
    if request.method == 'POST':
        user_form=UpdateUser(request.POST,instance=request.user)
        user_profile=UpdateProfile(request.POST,request.FILES,instance=request.user.userprofileinfo)

        if user_form.is_valid() and user_profile.is_valid():
            user_form.save()
            user_profile.save()
            return render(request,"basicapp/profile.html")
    else:
        user_form=UpdateUser(instance=request.user)
        profile_form=UpdateProfile(instance=request.user.userprofileinfo)
        return render(request,"basicapp/update_profile.html",{'user_form':user_form,'profile_form':profile_form})

@login_required
def visited_industries(request):
    visited=BookingListIndi.objects.filter(user1=request.user)
    date_now=datetime.datetime.now().date() 
    print(visited)
    print(date_now)
    return render(request,'basicapp/visited.html',{'visited':visited,'datetime_now':date_now})

@login_required
def booked_to_visit(request):
    booked_industries=BookingListIndi.objects.filter(user1=request.user)
    date_now = datetime.datetime.now().date()
    print(date_now)
    date = str(date_now)
    date_list = date.split('-')
    print(date_list)
    for d in booked_industries:
        temp = str(d.date_visit)
        temp1 = temp.split('-')
        if(int(temp1[0]) - int(date_list[0]) < 1):
            if(int(temp1[1]) - int(date_list[1]) == 0):
                if((int(temp1[2]) - int(date_list[2]) <= 5)):
                    d.left_days_bool = False
            elif(int(temp1[1]) - int(date_list[1]) == 1):
                if ((int(temp1[2]) - int(date_list[2]) == 25)):
                    d.left_days_bool = False
    return render(request,'basicapp/booked_to_visit.html',{'booked_industries':booked_industries,'date_now':date_now,})

@login_required
def cancel_ticket(request,industry_id):

    if request.method=="POST":
        industry_to_delete=get_object_or_404(BookingListIndi,id=industry_id)#BookingListIndi.objects.get(id=industry_id)
        industry_to_delete.delete()
        print(industry_id)
        return redirect('basicapp:booked_to_visit')

    return render(request,'basicapp/booked_to_visit.html')


class booking_charge(LoginRequiredMixin,TemplateView):
    template_name = 'basicapp/booking_charge.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        print(kwargs)
        context['industry_id']=kwargs['ind_id']
        return context


@login_required
def charge1(request,ind_id):
    if request.method == 'POST':
        charge=stripe.Charge.create(
            amount=1000,
            currency='usd',
            description='Booking charge',
            source=request.POST['stripeToken'],
        )

        return redirect(reverse('booking:con_indi',kwargs={"ind_id":ind_id}))
    else:
        return render(request,'basicapp/booking_charge.html',{"ind_id":ind_id})


@login_required
def charge2(request,ind_id):
    if request.method == 'POST':
        charge=stripe.Charge.create(
            amount=3000,
            currency='usd',
            description='Booking charge',
            source=request.POST['stripeToken'],
        )

        return redirect(reverse('booking:con_orga',kwargs={"ind_id":ind_id}))
    else:
        return render(request,'basicapp/booking_charge.html',{"ind_id":ind_id})


@login_required
def add_to_visit_later(request):
    add_to_visit_later=AddToVisitLater.objects.filter(user_id=request.user)
    return render(request,'basicapp/add_to_visit_later.html',{'add_to_visit_later':add_to_visit_later})


@login_required
def cancel_ticket2(request,industry_id):

    if request.method=="POST":
        industry_to_delete=get_object_or_404(AddToVisitLater,id=industry_id)#BookingListIndi.objects.get(id=industry_id)
        industry_to_delete.delete()
        return redirect('basicapp:add_to_visit_later')

    return render(request,'basicapp/add_to_visit_later.html')
