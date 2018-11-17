from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_industries = List.objects.all
            messages.success(request, ('Industry has been added to list!!'))
            return render(request, 'home.html', {'all_industries': all_industries})
    else:
        all_industries = List.objects.all
        return render(request, 'home.html', {'all_industries': all_industries})

def delete(request, list_id):
    industry = List.objects.get(pk=list_id)
    industry.delete()
    messages.success(request, ('Industry has been removed from ur list'))
    return redirect('home')
def cross_off(request, list_id):
    industry = List.objects.get(pk=list_id)
    industry.completed = True
    industry.save()
    return redirect('home')
def uncross(request, list_id):
    industry = List.objects.get(pk=list_id)
    industry.completed = False
    industry.save()
    return redirect('home')
def edit(request, list_id):
    if request.method == 'POST':
       industry = List.objects.get(pk=list_id)

       form = ListForm(request.POST or None, instance=industry)

       if form.is_valid():
          form.save()
          messages.success(request, ('Industry has been edited!!'))
          return redirect('home')
    else:
          industry = List.objects.get(pk=list_id)
          return render(request, 'edit.html', {'industry': industry})

