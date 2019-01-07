from django import forms
from .models import NewsletterUser
from crispy_forms.helper import FormHelper

class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email
