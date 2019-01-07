from django.urls import path
from . import views

app_name = 'booking'
urlpatterns = [

    path('con_indi/<int:ind_id>', views.con_indi, name='con_indi'),
    path('con_orga/<int:ind_id>', views.con_orga, name='con_orga'),
    path('book_air_indi/', views.book_air_indi, name='book_air_indi'),
    path('book_air_orga/', views.book_air_orga, name='book_air_orga'),
    path('book_train_indi/', views.book_train_indi, name='book_train_indi'),
    path('book_train_orga/', views.book_train_orga, name='book_train_orga'),
    path('individual_listAPI/',views.IndividualvisitList1.as_view(),name='individual_APIList1'),
    path('individual_listAPI/<industry>/',views.IndividualvisitList2.as_view(),name='individual_APIList2'),
    path('individual_listAPI/<industry>/<branch>/',views.IndividualvisitList3.as_view(),name='individual_APIList3'),
    path('book_bus_indi/', views.book_bus_indi, name='book_bus_indi'),
    path('book_bus_orga/', views.book_bus_orga, name='book_bus_orga'),
]
