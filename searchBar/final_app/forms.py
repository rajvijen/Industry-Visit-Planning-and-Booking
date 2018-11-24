from django import forms
from django.forms import ModelForm,Textarea
from final_app.models import Industry,Review
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS

#from reviews.models import UserProfileInfo
class IndustryForm(ModelForm):
    class meta:
        model = Industry
        fields = '__all__'


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('pub_date',)
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }
