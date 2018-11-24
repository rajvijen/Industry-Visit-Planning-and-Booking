from django import forms

class FormName(forms.Form):
    input=forms.CharField()
    select_type=forms.ChoiceField()
