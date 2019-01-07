from django.contrib import admin
from .models import Room
# from .models import Room, Chat

admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)
