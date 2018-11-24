from django.shortcuts import render
from django.http import HttpResponse
from final_app.models import Industry,Review
from final_app.forms import ReviewForm,IndustryForm
from final_app import forms
import numpy as np
from django.db.models import Count,Avg,Max
from django.db.models import IntegerField

def review(request):
    rate = Review.objects.all()
    if request.method == 'POST':
        f = ReviewForm(request.POST)
        review_details = Review.objects.order_by('pub_date')
        if f.is_valid():
            F=f.save(commit=False)
            try:
                obj1 = Review.objects.get(firstname = F.firstname, industry_id = F.industry_id)
                obj1.rating = F.rating
                obj1.pub_date = F.pub_date
                obj1.user_name = F.user_name
                obj1.comment = F.comment
                obj1.save()
            except:
                F.save()
        a = []
        industry_dict = Industry.objects.all()
        count = Industry.objects.all().count()
        for i in range(0,count):
            b = Review.objects.filter(industry_id=industry_dict[i]).aggregate(Avg('rating',output_field=IntegerField()))
            a.append(b)
        print(a)
        return render(request,'temp/rating.html',{'doc':industry_dict,'rating':a})
    else:
        f = ReviewForm()
        return render(request,'temp/review.html',{'form':f})
