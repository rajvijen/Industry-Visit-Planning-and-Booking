from rest_framework import serializers
from booking.models import *

class BookingListIndiSerializer(serializers.ModelSerializer):

    class Meta:
        model=BookingListIndi
        fields=('name_person','industry_name','industry_branch','date_visit')
