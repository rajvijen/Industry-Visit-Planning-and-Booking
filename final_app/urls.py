from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name="final_app"

urlpatterns = [
    path('review/',views.review,name='review'),
]
