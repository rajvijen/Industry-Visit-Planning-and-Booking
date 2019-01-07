from django.contrib import admin
from .models import NewsletterUser,Newsletter
# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_added',)

admin.site.register(NewsletterUser,NewsletterAdmin)

admin.site.register(Newsletter)
