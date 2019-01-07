from django import forms
from django.contrib.auth.models import User
from basicapp.models import *
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    username=forms.CharField(max_length=120)
    email=forms.EmailField(max_length=120)
    class Meta():
        model=User
        fields=("username","email","password")

    def clean_username(self):
        usname=self.cleaned_data.get('username')
        if usname and User.objects.filter(username=usname).exists():
            raise forms.ValidationError('Username already exists')
        return usname

    # def clean_email(self):
    #     emil=self.cleaned_data.get('email')
    #     if emil and User.objects.filter(email=emil).exists():
    #         raise forms.ValidationError('Email already exists')
    #     return emil





class UserProfileInfoForms(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=("name","gender")

    def clean_gender(self):
        gen=self.cleaned_data.get('gender')
        print(gen)

        if ((gen.lower()!=("male")) and (gen.lower()!=("female")) and (gen.lower()!=("other"))):
            raise forms.ValidationError("Gender should be either male, female or other")

        return gen


class UpdateUser(forms.ModelForm):
    username=forms.CharField(max_length=120)
    email=forms.EmailField()
    class Meta():
        model=User
        fields=("username","email")

class UpdateProfile(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ("name", "gender",'image')
