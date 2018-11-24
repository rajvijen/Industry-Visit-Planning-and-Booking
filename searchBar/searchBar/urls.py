"""learning_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from basicapp import views
from searchBarApp import views as search_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from searchBarApp import views as search_views

from django.views.static import serve

urlpatterns = [
    url(r'^$',search_views.index,name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^search/',include('searchBarApp.urls')),
    url(r'^basicapp/',include('basicapp.urls')),
    url(r'^booking/', include('booking.urls')),
    url(r'^review/', include('final_app.urls')),
    # url(r'^chat/',include('chat.urls')),
    url(r'^logout/$',views.user_logout,name="user_logout"),
    url(r'^special/$',views.special,name="special"),

    url(r'^reset-password/$', auth_views.PasswordResetView.as_view(), name="password_reset"),
    url(r'^reset-password/done/$', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    url(r'reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
