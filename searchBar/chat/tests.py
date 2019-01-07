from django.test import TestCase ,Client
from django.http import HttpRequest
from django.urls import reverse
from basicapp.models import UserProfileInfo
from django.contrib.auth.models import User

class ListView_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")

    def test_user_profile(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('chat:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index_chat.html')

#URL-Testing
class URL_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")

    def test_user_profile(self):
        response = self.client.get(reverse('chat:index'))
        self.assertEqual(response.status_code, 302)
