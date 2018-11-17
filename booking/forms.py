from django import forms
from .models import BookingListIndi, BookingListOrga
import datetime

class PostForm1(forms.ModelForm):
    class Meta:
        model = BookingListIndi
        exclude = ('code', 'visited', 'slot_time')

    def clean(self):
        all_clean_data = super().clean()
        date_format_1 = "%Y-%m-%d"  # {} %H:%M:%S+00:0"
        global date
        date = str(all_clean_data['date_visit'])
        val_date = all_clean_data.get('date_visit')
        num_visit = all_clean_data.get('visiting_members')
        curr = datetime.date.today()
        a = datetime.datetime.strptime(str(val_date), date_format_1)
        b = datetime.datetime.strptime(str(curr), date_format_1)
        delta = a - b
        if delta.days < 5:
            self.add_error('date_visit', "You need to book before 5 days")
        if num_visit <= 0:
            self.add_error('visiting_members', 'Please enter a positive number')

class Slot_Indi(forms.ModelForm):
    class Meta:
        model = BookingListIndi
        fields = ('slot_time', )

    def clean(self):
        all_clean_data = super().clean()
        slot = all_clean_data['slot_time']
        global date
        date = str(date)
        date = date.split(',')
        date_format_1 = "%Y-%m-%d"
        b = datetime.datetime.strptime(str(date[0]), date_format_1).strftime(date_format_1)
        result = BookingListIndi.objects.filter(date_visit=b)
        for r in result:
            if str(slot) == str(r.slot_time):
                self.add_error('slot_time', "This slot already booked")

class PostForm2(forms.ModelForm):
    class Meta:
        model = BookingListOrga
        exclude = ('code', 'visited', 'slot_time')

    def clean(self):
        all_clean_data = super().clean()
        date_format_1 = "%Y-%m-%d"  # {} %H:%M:%S+00:0"
        global date
        date = str(all_clean_data['date_visit'])
        val_date = all_clean_data.get('date_visit')
        num_visit = all_clean_data.get('visiting_members')
        curr = datetime.date.today()
        a = datetime.datetime.strptime(str(val_date), date_format_1)
        b = datetime.datetime.strptime(str(curr), date_format_1)
        delta = a - b
        if delta.days < 5:
            self.add_error('date_visit', "You need to book before 5 days")
        if num_visit <= 0:
            self.add_error('visiting_members', 'Please enter a positive number')

class Slot_Orga(forms.ModelForm):
    class Meta:
        model = BookingListOrga
        fields = ('slot_time', )

    def clean(self):
        all_clean_data = super().clean()
        slot = all_clean_data['slot_time']
        global date
        date = str(date)
        date = date.split(',')
        date_format_1 = "%Y-%m-%d"
        b = datetime.datetime.strptime(str(date[0]), date_format_1).strftime(date_format_1)
        result = BookingListOrga.objects.filter(date_visit=b)
        for r in result:
            if str(slot) == str(r.slot_time):
                self.add_error('slot_time', "This slot already booked")