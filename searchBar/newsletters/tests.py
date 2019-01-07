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

    def test_view_newsletter_sign_up(self):
        response = self.client.get(reverse('newsletters:newsletter_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletters/sign_up.html')

    def test_view_newsletter_unsubscibe(self):
        response = self.client.get(reverse('newsletters:newsletter_unsubscribe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletters/unsubscribe.html')

'''
    def test_view_newsletter_signup_template(self):
        response = self.client.get(reverse('newsletters:newsletter_signup_template'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletters/sign_up_email.html')
'''
#URL-Testing
class URL_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")

    def test_url_newsletter_sign_up(self):
        response = self.client.get(reverse('newsletters:newsletter_signup'))
        self.assertEqual(response.status_code, 200)

    def test_url_newsletter_unsubscibe(self):
        response = self.client.get(reverse('newsletters:newsletter_unsubscribe'))
        self.assertEqual(response.status_code, 200)
'''
    def test_url_newsletter_signup_template(self):
        response = self.client.get(reverse('newsletters:newsletter_signup_template'))
        self.assertEqual(response.status_code, 200)
'''
