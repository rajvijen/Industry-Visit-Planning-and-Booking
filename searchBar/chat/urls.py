from django.conf.urls import url,include
from chat import views

app_name="chat"

urlpatterns=[
    url(r'^chat_room/$',views.index,name='index'),
]
