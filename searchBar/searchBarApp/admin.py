from django.contrib import admin

from .models import industry,NewsletterEmail,Review,AddToVisitLater
# Register your models here.

admin.site.register(industry)
admin.site.register(NewsletterEmail)
admin.site.register(Review)
admin.site.register(AddToVisitLater)
