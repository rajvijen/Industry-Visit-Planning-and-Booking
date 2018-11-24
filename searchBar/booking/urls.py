from django.urls import path
from . import views

app_name = 'booking'
urlpatterns = [

    path('con_indi/', views.con_indi, name='con_indi'),
    path('con_orga/', views.con_orga, name='con_orga'),

]