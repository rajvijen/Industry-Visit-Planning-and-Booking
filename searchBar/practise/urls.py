from django.urls import path
from practise import views
from django.conf.urls import url,include

app_name="practise"

urlpatterns = [
    path('feedback/',views.feedback_web,name = "feedback")
]
