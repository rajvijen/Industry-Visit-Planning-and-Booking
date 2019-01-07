from django.shortcuts import get_object_or_404,render,redirect
from .models import BookingListIndi, BookingListOrga,Tickets
from .forms import PostForm1, PostForm2
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from basicapp.forms import UserForm

import random
import string

from searchBarApp.models import industry

#Models used for django rest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.serializers import BookingListIndiSerializer
#End of RestFramework models


def rand_str(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your views here.
def sending_email(site, user, current_site, code, to_email,bus_code="you don't have it"):
    mail_subject = 'Thanks for choosing our App'
    message = render_to_string(site, {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'code': code,
        'bus_code':bus_code,
    })
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.content_subtype = 'html'
    email.mixed_subtype = 'related'

    email.send()

AIR_DEST = {'Ahmedabad':'AMD', 'Aizawl':'AJL', 'Aloka':'AKD', 'Amausi':'LKO', 'Amritsar':'LUH', 'Bagdogra':'IXB', 'Bajpe':'IXE',
        'Bakula Rimpoche':'IXL', 'Balurghat':'RGH', 'Bamraulli':'IXD', 'Barapani':'SHL', 'Bareli':'BEK', 'Bellary':'BEP',
        'Bengaluru':'BLR', 'Bengaluru International':'BLR', 'Bhatinda':'BUP', 'Bhavnagar':'BHU', 'Bhopal':'BHO', 'Bhubaneshwar':'BBI', 'Bikaner':'BKB',
        'Bilaspur':'PAB', 'Ranchi':'IXR', 'Birsa Munda International':'IXR', 'Borjhar':'GAU', 'Guwahati':'GAU', 'Car Nicobar':'CBD',
        'Chandigarh':'Chandigarh', 'Chennai':'MAA', 'Chennai International':'MAA', 'Chatrapati Sivaji International':'BOM', 'Mumbai':'BOM',
        'Chikkalthana':'IXU', 'Cochin International':'COK', 'Kochi':'COK','Cooch Beher':'COH', 'Cuddapah':'CDP', 'Dabok':'UDR',
        'Dabolim':'GOI', 'Daman':'NMB', 'Daparizo':'DAE', 'Darjeeling':'DAI', 'Dehra Dun':'DED', 'Indore':'IDR', 'Devi Ahilyabai Holkar':'IDR',
        'Dhanbad':'DBD', 'Dibrugarh':'DIB', 'Dimapur':'DMU', 'Diu':'DIU', 'Gaggal':'DHM', 'Dharamshala':'DHM', 'Gandhinagar':'ISK',
        'Nasik':'ISK', 'Gaya':'GAY', 'Gorakhpur':'GOP', 'Govardhanpur':'JGA', 'Guna':'GUX', 'Gwalior':'GWL', 'Hissar':'HSS',
        'Hubli':'HBX', 'Hyderabad International':'HYD', 'Hyderabad':'HYD', 'Indira Gandhi International':'DEL', 'New Delhi':'DEL', 'Delhi':'DEL',
        'Jabalpur':'JLR', 'Jaisalmer':'JSA', 'Jeypore':'PYB', 'Jodhpur':'JDH', 'Kailashahar':'IXH', 'Kamalpur':'IXQ', 'Kandla':'IXY',
        'Kanpur':'KNU', 'Keshod':'IXK', 'Khajuraho':'HJR', 'Kheria':'AGR', 'Agra':'AGR', 'Khowai':'IXN', 'Kohlapur':'KLH',
        'Kota':'KTU', 'Kozhikode':'CCJ', 'Kullu Manali':'KUU', 'Khumbhirgram':'IXS', 'Lilabari':'IXI', 'Lohegaon':'PNQ',
        'Madhurai':'IMX', 'Malda':'LDA', 'Mohanbari':'MOH', 'Municipal':'IMF', 'Imphal':'IMF', 'Muzaffarpur':'MZU', 'Mysore':'MYQ',
        'Nanded':'NDC', 'Netaji Subhash Chandra Bose International':'CCU', 'Kolkata':'CCU', 'Neyveli':'NYV', 'Pantnagar':'PGH',
        'Pasighat':'IXT', 'Pathankot':'IXP', 'Patna':'PAT', 'Peelamedu':'CJB', 'Coimbatore':'CJB', 'Pondicherry':'PNY', 'Porbandar':'PBD',
        'Port Blair':'IXZ', 'Puttaparthi':'PUT', 'Raipur':'RPR', 'Raja Sansi':'ATQ', 'Rajahmundry':'RJA', 'Rajkot':'RAJ',
        'Ratnagiri':'RTC', 'Rourkela':'RRK', 'Jorhat':'JRH', 'Bhuj':'BHJ', 'Rudra Mata':'BHJ', 'Rupsi':'RUP', 'Salem':'SXV',
        'Salonibari':'TEZ', 'Sambre':'IXG', 'Sanganeer':'JAI', 'Satna':'TNI', 'Satwari':'IXJ', 'Sholapur':'SSE', 'Simla':'SLV',
        'Singerbhil':'IXA', 'Sonari':'IXW', 'Sonegaon':'NAG', 'Srinagar':'SXR', 'Surat':'STV', 'Tezu':'TEI', 'Thanjavur':'TJV',
        'Thiruvananthapuram International':'TRV', 'Trivandrum':'TRV', 'Tirupati':'TIR', 'Trichy':'TRZ', 'Tuticorin':'TCR',
        'Vadodara':'BDQ', 'Varanasi':'VNS', 'Vijayawada':'VGA', 'Vishakapatnam':'VTZ', 'Vizak':'VTZ', 'Warangal':'WGC', 'Zero':'ZER'}

TRAIN_DEST = {'Agra':'AGC', 'Ahmedabad':'ADI', 'Amritsar':'ASR', 'Ajmer':'AII', 'Aloka':'AK', 'Allahabad':'ALD',
              'Ambala': 'UMB', 'Asansol':'ASN', 'Bengaluru':'SBC', 'Bhopal':'BPL', 'Bhubaneshwar':'BBS', 'Chandigarh':'CDG',
              'Chennai':'MAS', 'Mumbai':'BCT', 'Kochi':'ERS', 'Indore':'INDB', 'Gandhi Nagar':'GNC', 'Gwalior':'GWL',
              'Hyderabad':'HYB', 'Delhi':'DLI', 'Jabalpur':'JBP', 'Kanpur':'CNB', 'Mysore':'MYS', 'Kolkata':'KOAA',
              'Patna':'PNBE', 'Abu Road':'ABR', 'Adoni':'AD', 'Ahmednagar':'ANG', 'Aligarh':'ALJN', 'Alleppey':'ALLP',
              'Aluva':'AWY', 'Amla':'AMLA', 'Anand':'ANND', 'Ara':'ARA', 'Arakkonam':'AJJ', 'Badnera':'BD',
              'Bakhtiyarpur':'BKP', 'Balasore':'BLS', 'Balharshah':'BPQ', 'Balugan':'BALU', 'Bandel':'BDC',
              'Bandra Terminus':'BDTS', 'Bangalore Cantt':'BNC', 'Bangarapet':'BWT', 'Bapatla':'BPP', 'Barabanki':'BBK',
              'Barauni':'BJU', 'Barddhaman':'BWN', 'Bareilly':'BE', 'Barh':'BARH', 'Barhiya':'BRYA', 'Barsoi':'BOE',
              'Basti':'BST', 'Beas':'BEAS', 'Betul':'BZU', 'Bhadrakh':'BHC', 'Bhaurch':'BH', 'Bhusaval':'BSL',
              'Bilaspur':'BSP', 'Bina':'BINA', 'Bokaro':'BKSC', 'Borivali':'BVI', 'Brahmapur':'BAM', 'Burhanpur':'BAU',
              'Buxar':'BXR', 'Chakki':'CHKB', 'Chandrapur':'CD', 'Chengalpattu':'CGL', 'Chengannur':'CNGR',
              'Chennai Central':'MAS', 'Chennai Egmore':'MS', 'Chhapra':'CPR', 'Chirala':'CLX', 'Chittaranjan':'CRJ',
              'Coimbatore':'CBE', 'Coimbatore Junction':'CBE', 'Cuttack':'CTC', 'Dadar':'DR', 'Danapur':'DNR',
              'Daund':'DD', 'Dehri On Sone':'DOS', 'Delhi Cantt':'DEC', 'Delhi Kishangnj':'DKZ', 'Deoria Sadar':'DEOS',
              'Dhanbad':'DHN', 'Durgapur':'DGR', 'Ernakulam':'ERN', 'Ernakulam Jn':'ERS', 'Erode':'ED', 'Etawah':'ETW',
              'Faizabad':'FD','Faridabad':'FDB', 'Fatwa':'FUT', 'Gaya':'GAYA', 'Ghaziabad':'GZB', 'Godhra':'GDA',
              'Gonda':'GD','Gondia':'G', 'Gooty':'GY', 'Gorakhpur':'GKP', 'Gudur':'GDR', 'Gulbarga':'GB',
              'Guntakal':'GTL','Guntur':'GNT', 'Guwahati':'GHY', 'Nizamuddin':'NZM', 'Habibganj':'HBJ', 'Hajipur':'HJP',
              'Hapur':'HPU','Hardoi':'HRI', 'Haridwar':'HR', 'Hindupur':'HUP', 'Howrah':'HWH', 'Howrah Jn':'HWH',
              'Hubli':'UBL','Igatpuri':'IGP', 'Itarsi':'ET', 'Jaipur':'JP', 'Jalandhar Cantt':'JRC', 'Jalandhar':'JUC',
              'Jalgaon':'JL','Jammu Tawi':'JAT', 'Jasidih':'JSME', 'Jhajha':'JAJ', 'Jhansi':'JHS','Jodhpur':'JU',
              'Jolarpettai':'JTJ', 'Kalyan Jn':'KYN','Kamakhya':'KYQ', 'Kannur':'CAN', 'Karjat':'KJT', 'Kasaragod':'KGQ',
              'Kathua':'KTHU', 'Katihar':'KIR', 'Katni':'KTE', 'Katpadi':'KPD','Kayankulam':'KYJ', 'Kazipet':'KZJ',
              'Khalilabad':'KLD', 'Khammam':'KMT', 'Khandwa':'KNW','Kharagpur Jn':'KGP', 'Khurda Road':'KUR',
              'Kishanganj':'KNE', 'Kiul':'KIUL', 'Koderma':'KQR','Kollam':'QLN', 'Kota':'KOTA', 'Kottayam':'KTYM',
              'Kozhikode':'CLT', 'Krishnarajapurm':'KJM','Laksar':'LRJ', 'Lalitpur':'LAR', 'Lokmanyatilak T':'LTT',
              'Lonavala':'LNL', 'Lucknow Ne':'LJN','Lucknow Nr':'LKO', 'Ludhiana':'LDN', 'Madgaon':'MAO',
              'Madhupur':'MDP', 'Madurai':'MDU', 'Mahesana':'MSH', 'Maihar':'MYR', 'Malda':'MLDT', 'Manikpur':'MKP',
              'Manmad':'MMR', 'Mathura':'MTJ', 'Mirzapur':'MZP','Mokameh':'MKA', 'Moradabad':'MB', 'Morena':'MRA',
              'Mughal Sarai Jn':'MGS', 'Mumbai Cst':'CSTM', 'Muzaffarpur':'MFP', 'Nandid':'ND', 'Nagda':'NAD',
              'Nagpur':'NGP', 'Nasik':'NK', 'Navsari':'NVS', 'Nellore':'NLR', 'New Delhi':'NDLS', 'Ongole':'OGL',
              'Palakkad':'PGT', 'Palanpur':'PNU', 'Palasa':'PSA', 'Pandhurna':'PAR', 'Panipat':'PNP',
              'Parna Saheb':'PNC', 'Phagwara':'PGW', 'Pipariya':'PPI', 'Pune':'PUNE', 'Raipur':'R', 'Raja Ki Mandi':'RKM',
              'Rajamundry':'RJY', 'Rajkot':'RJT', 'Rajpura':'RPJ', 'Ramgundam':'RDM', 'Rampur':'RMU', 'Ranchi':'RNC',
              'Raniganj':'RNG', 'Ratlam':'RTM', 'Renigunta':'RU', 'Roorkee':'RK', 'Saharanpur':'SRE', 'Salem':'SA',
              'Samalkot':'SLO', 'Samastipur':'SPJ', 'Sasaram':'SSM', 'Satna':'STA', 'Sawai Madhopur':'SWM',
              'Sealdah':'SDAH', 'Secundrabad':'SC', 'Sevagram':'SEGM', 'Shahjehanpur':'SPN', 'Shoranur':'SRR',
              'Sirpur Kagazngr':'SKZR', 'Solapur':'SUR', 'Sonpur':'SEE', 'Srikakulam':'CHE', 'Surat':'ST',
              'Surendranagar':'SUNR', 'Tambaram':'TBM', 'Tatanagar':'TATA', 'Tenali':'TEL', 'Thane':'TNA',
              'Thrissur':'TCR', 'Tiruchirappalli':'TPJ', 'Tirupati':'TPTY', 'Tiruppur':'TUP', 'Trivandrum Cntl':'TVC',
              'Trivandrum Pett':'TVP', 'Tundla':'TDL', 'Tuni':'TUNI', 'Ujjain':'UJN', 'Vadodara':'BRC', 'Valsad':'BL',
              'Vapi':'VAPI', 'Varanasi':'BSB', 'Vasai Road':'BSR', 'Vidisha':'BHS', 'Vijayawada':'BZA', 'Villuparam':'VM',
              'Viramgam':'VG', 'Vishakhapatnam':'VSKP', 'Vizianagram':'VZM', 'Warangal':'WL', 'Yesvantpur Jn':'YPR'}


def index(request):
    return render(request, 'booking/index.html')

@login_required
def con_indi(request,ind_id):
    if request.method == 'POST':
        form = PostForm1(request.POST)
        if form.is_valid() :

            ind_location_list=industry.objects.get(pk=ind_id).location.split(',')
            print(ind_location_list)
            name_person = form.cleaned_data['name_person']
            industry_name = industry.objects.get(pk=ind_id).id_name
            industry_branch=ind_location_list[2]
            email=form.cleaned_data['email']
            date_visit = form.cleaned_data['date_visit']
            slot_time = form.cleaned_data['slot_time']
            visiting_members = form.cleaned_data['visiting_members']
            street_name = form.cleaned_data['street_name']
            city_name = form.cleaned_data['city_name']
            pin_code = form.cleaned_data['pin_code']
            code = rand_str()
            user1 = User.objects.get(username=request.user.username)
            p = BookingListIndi(user1=user1,name_person=name_person, industry_name=industry_name,industry_branch=industry_branch,email=email, date_visit=date_visit,
                                slot_time=slot_time, visiting_members=visiting_members, street_name=street_name,
                                city_name=city_name, pin_code=pin_code, code=code)
            p.save()


            total = Tickets.objects.filter(day = date_visit).filter(slot = slot_time).count()
            if total == 0:
                tick = Tickets.objects.create(day = date_visit,slot = slot_time,ticks = 20-visiting_members)
                tick.save()
            else:
                tick = Tickets.objects.filter(day = date_visit).filter(slot = slot_time)
                for tc in tick:
                    num = tc.ticks
                tk = Tickets.objects.get(pk = tc.id)
                tk.ticks = num - visiting_members
                tk.save()
            transport = request.POST['transport']
            if transport == 'none':
                user = form.save(commit=False)
                user.is_active = False
                current_site = get_current_site(request)
                to_email = email
                site = 'booking/tick_indi_other.html'
                sending_email(site=site, user=user, current_site=current_site, code=code, to_email=to_email)
                return redirect('searchBarApp:searching')
            elif transport == 'bus':
                user = form.save(commit=False)
                user.is_active = False
                current_site = get_current_site(request)
                to_email = email
                site = 'booking/tick_indi_other.html'
                sending_email(site=site, user=user, current_site=current_site, code=code, to_email=to_email)
                return render(request, 'booking/bus_book_indi.html')
            elif transport == 'train':
                user = form.save(commit=False)
                user.is_active = False
                current_site = get_current_site(request)
                to_email = email
                site = 'booking/tick_indi_other.html'
                sending_email(site=site, user=user, current_site=current_site, code=code, to_email=to_email)
                return render(request, 'booking/train_book_indi.html')
            elif transport == 'plane':
                user = form.save(commit=False)
                user.is_active = False
                current_site = get_current_site(request)
                to_email = email
                site = 'booking/tick_indi_other.html'
                sending_email(site=site, user=user, current_site=current_site, code=code, to_email=to_email)
                return render(request, 'booking/air_book_indi.html')
            else:
                return HttpResponse(
                    "<h3>How can you get here without clicking any option <br> It is a miracle and you truely are a genius</h3>")
        else:
            print(PostForm1.errors)
    else:
        form = PostForm1()
    return render(request, 'booking/book_indi.html', context={'form': form,'ind_id':ind_id})

@login_required
def con_orga(request,ind_id):
    if request.method == 'POST':
        form = PostForm2(request.POST)
        if form.is_valid():
            
            ind_location_list=industry.objects.get(pk=ind_id).location.split(',')
            
            name_person = form.cleaned_data['name_person']
            industry_name = industry_name = industry.objects.get(pk=ind_id).id_name
            industry_branch=ind_location_list[2]
            organisation_name = form.cleaned_data['organisation_name']
            email = form.cleaned_data['email']
            date_visit = form.cleaned_data['date_visit']
            slot_time = form.cleaned_data['slot_time']
            visiting_members = form.cleaned_data['visiting_members']
            street_name = form.cleaned_data['street_name']
            city_name = form.cleaned_data['city_name']
            pin_code = form.cleaned_data['pin_code']
            code = rand_str()
            user1 = User.objects.get(username=request.user.username)
            p = BookingListOrga(user1=user1,name_person=name_person, industry_name=industry_name,industry_branch=industry_branch,email=email,
                                organisation_name=organisation_name, date_visit=date_visit, slot_time=slot_time,
                                visiting_members=visiting_members, street_name=street_name, city_name=city_name,
                                pin_code=pin_code, code=code)
            p.save()
            total = Tickets.objects.filter(day = date_visit).filter(slot = slot_time).count()
            if total == 0:
                tick = Tickets.objects.create(day = date_visit,slot = slot_time,ticks = 20-visiting_members)
                tick.save()
            else:
                tick = Tickets.objects.filter(day = date_visit).filter(slot = slot_time)
                for tc in tick:
                    num = tc.ticks
                tk = Tickets.objects.get(pk = tc.id)
                tk.ticks = num - visiting_members
                tk.save()

            transport = request.POST['transport']
            if transport == 'none':
                user = form.save(commit=False)
                user.is_active = False
                current_site = get_current_site(request)
                to_email = email
                site = 'booking/tick_orga_other.html'
                sending_email(site=site, user=user, current_site=current_site, code=code, to_email=to_email)
                return redirect('searchBarApp:searching')
            elif transport == 'bus':
                user = form.save(commit=False)
                user.is_active = False
                current_site = get_current_site(request)
                to_email = email
                site = 'booking/tick_orga_other.html'
                sending_email(site=site, user=user, current_site=current_site, code=code, to_email=to_email)
                return render(request, 'booking/bus_book_orga.html')
            elif transport == 'train':
                user = form.save(commit=False)
                user.is_active = False
                current_site = get_current_site(request)
                to_email = email
                site = 'booking/tick_indi_other.html'
                sending_email(site=site, user=user, current_site=current_site, code=code, to_email=to_email)
                return render(request, 'booking/train_book_orga.html')
            elif transport == 'plane':
                user = form.save(commit=False)
                user.is_active = False
                current_site = get_current_site(request)
                to_email = email
                site = 'booking/tick_indi_other.html'
                sending_email(site=site, user=user, current_site=current_site, code=code, to_email=to_email)
                return render(request, 'booking/air_book_orga.html')
            else:
                return HttpResponse(
                    "<h3>How can you get here without clicking any option <br> It is a miracle and you truely are a genius</h3>")
        else:
            print(PostForm2.errors)
    else:
        form = PostForm2()
    return render(request, 'booking/book_orga.html', context={'form': form,'ind_id':ind_id})


def book_air_indi(request):
    type = request.POST['Type']
    from_dest = request.POST['from_des']
    to_dest = request.POST['to_des']
    dep_on = request.POST['depart_on']
    ret_on = request.POST['return_on']
    adult = request.POST['adults']
    child = request.POST['children']
    infant = request.POST['infants']
    from_des = AIR_DEST[from_dest]
    to_des = AIR_DEST[to_dest]
    yr1 = dep_on[0:4]
    mon1 = dep_on[5:7]
    da1 = dep_on[8:10]
    yr2 = ret_on[0:4]
    mon2 = ret_on[5:7]
    da2 = ret_on[8:10]
    dep_on = da1 + '/' + mon1 + '/' + yr1
    ret_on = da2 + '/' + mon2 + '/' + yr2
    if (type == 'One_Way'):
        return render(request, 'booking/list_flight.html', context={'type':'one_way', 'from_des':from_des,
                                                                    'to_des':to_des,'dep_on':dep_on, 'adult':adult,
                                                                    'child':child, 'infant':infant,
                                                                    'from_dest':from_dest,
                                                                    'to_dest':to_dest})
    else:
        return render(request, 'booking/list_flight.html', context={'type':'round_trip', 'from_des':from_des, 'to_des':to_des,
                                                                    'dep_on':dep_on, 'ret_on':ret_on, 'adult':adult,
                                                                    'child':child, 'infant':infant,
                                                                    'from_dest':from_dest,
                                                                    'to_dest':to_dest})

def book_air_orga(request):
    type = request.POST['Type']
    from_dest = request.POST['from_des']
    to_dest = request.POST['to_des']
    dep_on = request.POST['depart_on']
    ret_on = request.POST['return_on']
    adult = request.POST['adults']
    child = request.POST['children']
    infant = request.POST['infants']
    from_des = AIR_DEST[from_dest]
    to_des = AIR_DEST[to_dest]
    yr1 = dep_on[0:4]
    mon1 = dep_on[5:7]
    da1 = dep_on[8:10]
    yr2 = ret_on[0:4]
    mon2 = ret_on[5:7]
    da2 = ret_on[8:10]
    dep_on = da1 + '/' + mon1 + '/' + yr1
    ret_on = da2 + '/' + mon2 + '/' + yr2
    if (type == 'One_Way'):
        return render(request, 'booking/list_flight.html',
                      context={'type': 'one_way', 'from_des': from_des, 'to_des': to_des, 'dep_on': dep_on,
                               'adult': adult, 'child': child, 'infant': infant})
    else:
        return render(request, 'booking/list_flight.html',
                      context={'type': 'round_trip', 'from_des': from_des, 'to_des': to_des,'dep_on': dep_on,
                               'ret_on': ret_on, 'adult': adult, 'child': child, 'infant': infant})

def book_train_indi(request):
    from_dest = request.POST['from_des']
    to_dest = request.POST['to_des']
    date = request.POST['date']
    from_des = TRAIN_DEST[from_dest]
    to_des = TRAIN_DEST[to_dest]
    yr = date[0:4]
    mon = date[5:7]
    da = date[8:10]
    date = yr + mon + da
    return render(request, 'booking/list_train.html',
                  context={'from_dest':from_dest, 'to_dest':to_dest, 'date':date, 'from_des':from_des, 'to_des':to_des})

def book_train_orga(request):
    from_dest = request.POST['from_des']
    to_dest = request.POST['to_des']
    date = request.POST['date']
    from_des = TRAIN_DEST[from_dest]
    to_des = TRAIN_DEST[to_dest]
    yr = date[0:4]
    mon = date[5:7]
    da = date[8:10]
    date = yr + mon + da
    return render(request, 'booking/list_train.html',
                  context={'from_dest': from_dest, 'to_dest': to_dest, 'date': date, 'from_des':from_des, 'to_des':to_des})



class IndividualvisitList1(APIView):

    def get(self,request):
        booking_list=BookingListIndi.objects.all()
        serializer=BookingListIndiSerializer(booking_list,many=True)
        return Response(serializer.data)


class IndividualvisitList2(APIView):

    def get(self,request,industry):
        booking_list=BookingListIndi.objects.filter(industry_name=industry)
        serializer=BookingListIndiSerializer(booking_list,many=True)
        return Response(serializer.data)


class IndividualvisitList3(APIView):

    def get(self,request,industry,branch):
        booking_list=BookingListIndi.objects.filter(industry_name=industry).filter(industry_branch=branch)
        serializer=BookingListIndiSerializer(booking_list,many=True)
        return Response(serializer.data)

def book_bus_indi(request):
    from_des = request.POST['from_des']
    to_des = request.POST['to_des']
    date = request.POST['date']
    yr = date[0:4]
    mon = date[5:7]
    da = date[8:10]
    date = da + '-' + mon + '-' + yr
    return render(request, 'booking/list_bus.html', context={'from_des':from_des, 'to_des':to_des, 'date':date})

def book_bus_orga(request):
    from_des = request.POST['from_des']
    to_des = request.POST['to_des']
    date = request.POST['date']
    yr = date[0:4]
    mon = date[5:7]
    da = date[8:10]
    date = da + '-' + mon + '-' + yr
    return render(request, 'booking/list_bus.html', context={'from_des':from_des, 'to_des':to_des, 'date':date})
