from django.test import TestCase ,Client
from django.http import HttpRequest
from django.urls import reverse
from django.contrib.auth.models import User
from practise.models import Info,feed
import datetime
from basicapp.models import UserProfileInfo

class ListView_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")

    def test_feedback(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('practise:feedback'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback.html')

class Model_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        info1 = Info.objects.create(Username='wilson', Organisation = 'patro',date_visit = datetime.datetime.strptime("2018/12/15","%Y/%m/%d")
                                   ,email='ronytowilson3097@gmail.com')
        feed1 = feed.objects.create(name = "hemanth" , services = "good" , Guide = "good")

    def test_info(self):
        info1 = Info.objects.get(id = 1)
        exepected_value = str(info1.Username)+ " "+str(info1.date_visit)+" "+str(info1.email)
        self.assertEquals(str(info1), str(exepected_value))

    def test_maxlength(self):
        user = Info.objects.get(id=1)
        maximamlength=user._meta.get_field('Username').max_length
        self.assertEquals(maximamlength,100)

#URL-Testing
class URL_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")

    def test_url_feedback(self):
        response = self.client.get(reverse('practise:feedback'))
        self.assertEqual(response.status_code, 302)
