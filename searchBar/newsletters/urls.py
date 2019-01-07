from django.conf.urls import url
from django.urls import path
from django.conf import settings
from newsletters import views
from .views import newsletter_signup,newsletter_unsubscribe

app_name="newsletters"
urlpatterns = [
    path('sign_up/', views.newsletter_signup,name="newsletter_signup"),
    path('unsubscribe/', views.newsletter_unsubscribe,name="newsletter_unsubscribe"),
    path('newsletter_signup_template/',views.newsletter_signup_template,name="newsletter_signup_template",)
    ]
