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

    def test_view_uses_correct_template_home(self):
        response = self.client.get(reverse('blog:blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_view_uses_correct_template_about(self):
        response = self.client.get(reverse('blog:blog-about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

#URL Testing

class URL_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")

    def test_view_uses_correct_template_home(self):
        response = self.client.get(reverse('blog:blog-home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_about(self):
        response = self.client.get(reverse('blog:blog-about'))
        self.assertEqual(response.status_code, 200)
