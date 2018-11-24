from django import forms
from .models import BookingListIndi, BookingListOrga,Tickets
import datetime

class PostForm1(forms.ModelForm):
    class Meta:
        model = BookingListIndi
        exclude = ('code', 'visited', 'total_available', 'total_taken','user1')

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

        num = 0
        slot = all_clean_data['slot_time']
        date_format_1 = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(str(date), date_format_1).strftime(date_format_1)
        tickets = Tickets.objects.filter(day = date1).filter(slot = slot)
        for tc in tickets:
            tk = Tickets.objects.get(pk = tc.id)
            num += tk.ticks
        num1 = 20 - num
        if num1 < num_visit:
            self.add_error("slot_time","The tickets available are : " + str(num1) +" Please select another slot.")

class PostForm2(forms.ModelForm):
    class Meta:
        model = BookingListOrga
        exclude = ('code', 'visited', 'total_available', 'total_taken','user1')

    def clean(self):
        all_clean_data = super().clean()
        date_format_1 = "%Y-%m-%d"
        global date1
        date1 = str(all_clean_data['date_visit'])
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

        num = 0
        slot = all_clean_data['slot_time']
        date_format_1 = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(str(val_date), date_format_1).strftime(date_format_1)
        tickets = Tickets.objects.filter(day = date1).filter(slot = slot)
        for tc in tickets:
            tk = Tickets.objects.get(pk = tc.id)
            num += tk.ticks
        num1 = 20 - num
        if num1 < all_clean_data['visiting_members']:
            self.add_error("slot_time","The tickets available are : " + str(num1) +" Please select another slot.")
