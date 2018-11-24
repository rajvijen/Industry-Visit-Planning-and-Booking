from django.conf.urls import url
from django.urls import re_path
from basicapp import views
from django.urls import re_path

#Tis appp name is for TEMPLATE linking
app_name='basicapp'

urlpatterns=[
    url(r'^register/$',views.register,name="register"),
    url(r'^user_login/$',views.user_login,name="user_login"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate,name="activate"),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/update/$',views.update,name='update'),
]
