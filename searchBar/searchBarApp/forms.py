from django import forms
from searchBarApp.models import NewsletterEmail,Review,AddToVisitLater
from django.forms import ModelForm,Textarea
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS


class NewsletterForm(forms.ModelForm):
 class Meta:
     model = NewsletterEmail
     fields = '__all__'


#Forms Used for review
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('pub_date','industry_id','user_name','user_id')
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }

class AddToVisitLaterForm(ModelForm):
    class Meta:
        model = AddToVisitLater
        fields=("industry_id","user_id")
