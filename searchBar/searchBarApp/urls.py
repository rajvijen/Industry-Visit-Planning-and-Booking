from django.urls import path
from django.conf import settings
from django.views.static import serve
from searchBarApp import views
from django.conf.urls.static import static

app_name="searchBarApp"
urlpatterns = [
    path('searching/', views.index,name="searching"),
    path('searching/result', views.result, name="result"),
    path('Assembling',views.Assembling,name="Assembling"),
    path('Automobiles',views.Automobiles,name="Automobiles"),
    path('Manufacturing',views.Manufacturing,name="Manufacturing"),
    path('IT_Companies',views.IT_Companies,name="IT_Companies"),
    path('contact',views.contact,name="contact"),
    path('blog',views.blog,name="blog"),
    path('faq',views.faq,name="faq"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('read',views.read,name="read"),
    path('base',views.base,name="base"),
]
