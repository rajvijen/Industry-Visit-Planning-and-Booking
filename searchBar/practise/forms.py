from django import forms
from .models import Info,feed

class Info_form(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'

class Feed_Form(forms.ModelForm):
    class Meta:
        model = feed
        exclude = ('name','email','services','Guides','Query',)
