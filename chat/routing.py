# chat/routing.py
from django.urls import path, re_path

from .consumer import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
    # path(r'^ws/chat/<int:room_name_json>/', consumers.ChatConsumer),
]

# from django.conf.urls import url

# from . import consumers

# websocket_urlpatterns = [
#     url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
# ]