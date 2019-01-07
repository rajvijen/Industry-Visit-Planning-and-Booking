from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
#from .models import Room, Chat

# from django.db.models import Q
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.authentication import SessionAuthentication
# from .serializers import ChatModelSerializer

# from django.forms import model_to_dict
# from django.core.serializers.json import DjangoJSONEncoder
# from django.db.models import Model



@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")
    print("Went inside view")
    # Render that in the index template
    return render(request, "index_chat.html", {
        "rooms": rooms,
    })

# class ChatModelViewSet(ModelViewSet):
#     queryset = Chat.objects.all()
#     serializer_class = ChatModelSerializer
#     allowed_methods = ('GET', 'HEAD', 'OPTIONS')
#     pagination_class = None  # Get all user

#     def list(self, request, *args, **kwargs):
#         # Get all users except yourself
#         self.queryset = self.queryset.filter(Q(pk=kwargs['pk']))
#         return super(ChatModelViewSet, self).list(request, *args, **kwargs)
