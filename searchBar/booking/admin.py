from django.contrib import admin
from .models import BookingListIndi, BookingListOrga,Tickets

# Register your models here.

admin.site.register(BookingListIndi)
admin.site.register(BookingListOrga)
admin.site.register(Tickets)
