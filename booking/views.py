from django.shortcuts import render
from .models import BookingListIndi, BookingListOrga
from .forms import PostForm1, PostForm2, Slot_Indi, Slot_Orga

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

import random
import string

def rand_str(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your views here.
def sending_email(site, user, current_site, code, to_email):
    mail_subject = 'Thanks for choosing our App'
    message = render_to_string(site, {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'code': code,
    })
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.content_subtype = 'html'
    email.mixed_subtype = 'related'

    email.send()


def index(request):
    return render(request, 'booking/index.html')

def con_indi(request):
    if request.method == 'POST':
        form = PostForm1(request.POST)
        slot = Slot_Indi(request.POST)
        if form.is_valid() and slot.is_valid():
            name_person = form.cleaned_data['name_person']
            industry_name = form.cleaned_data['industry_name']
            date_visit = form.cleaned_data['date_visit']
            slot_time = slot.cleaned_data['slot_time']
            visiting_members = form.cleaned_data['visiting_members']
            street_name = form.cleaned_data['street_name']
            city_name = form.cleaned_data['city_name']
            pin_code = form.cleaned_data['pin_code']
            code = rand_str()
            p = BookingListIndi(name_person=name_person, industry_name=industry_name, date_visit=date_visit,
                                slot_time=slot_time, visiting_members=visiting_members, street_name=street_name,
                                city_name=city_name, pin_code=pin_code, code=code)
            p.save()

            user = form.save(commit=False)
            user.is_active = False
            current_site = get_current_site(request)
            to_email = 'lushaankkancherla1999@gmail.com'
            site = 'booking/ticket_gen_indi.html'
            sending_email(site, user, current_site, code, to_email)
            return render(request, 'booking/success.html')
        else:
            print(PostForm1.errors, "\n", Slot_Indi.errors)
    else:
        form = PostForm1()
        slot = Slot_Indi()
    return render(request, 'booking/book_indi.html', context={'form': form, 'slot':slot})

def con_orga(request):
    if request.method == 'POST':
        form = PostForm2(request.POST)
        slot = Slot_Orga(request.POST)
        if form.is_valid() and slot.is_valid():
            name_person = form.cleaned_data['name_person']
            industry_name = form.cleaned_data['industry_name']
            organisation_name = form.cleaned_data['organisation_name']
            date_visit = form.cleaned_data['date_visit']
            slot_time = slot.cleaned_data['slot_time']
            visiting_members = form.cleaned_data['visiting_members']
            street_name = form.cleaned_data['street_name']
            city_name = form.cleaned_data['city_name']
            pin_code = form.cleaned_data['pin_code']
            code = rand_str()
            p = BookingListOrga(name_person=name_person, industry_name=industry_name,
                                organisation_name=organisation_name, date_visit=date_visit, slot_time=slot_time,
                                visiting_members=visiting_members, street_name=street_name, city_name=city_name,
                                pin_code=pin_code, code=code)
            p.save()

            user = form.save(commit=False)
            user.is_active = False
            current_site = get_current_site(request)
            to_email = 'lushaankkancherla1999@gmail.com'
            site = 'booking/ticket_gen_orga.html'
            sending_email(site, user, current_site, code, to_email)
            return render(request, 'booking/success.html')
        else:
            print(PostForm2.errors, "\n", Slot_Orga.errors)
    else:
        form = PostForm2()
        slot = Slot_Orga()
    return render(request, 'booking/book_orga.html', context={'form': form, 'slot':slot})

def list_indi(request):
    all_lists = BookingListIndi.objects.all()
    return render(request, 'booking/list_indi.html', {'all_lists':all_lists})

def list_orga(request):
    all_lists = BookingListOrga.objects.all()
    return render(request, 'booking/list_orga.html', {'all_lists':all_lists})
