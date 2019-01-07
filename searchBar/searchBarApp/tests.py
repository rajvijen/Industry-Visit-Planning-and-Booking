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

    def test_view_uses_correct_template_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/index.html')

    def test_view_uses_correct_template_base(self):
        response = self.client.get(reverse('searchBarApp:base'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/base.html')

    def test_view_uses_correct_template_contact(self):
        response = self.client.get(reverse('searchBarApp:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/contact.html')

    def test_view_uses_correct_template_blog(self):
        response = self.client.get(reverse('searchBarApp:blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/blog.html')

    def test_view_uses_correct_template_faq(self):
        response = self.client.get(reverse('searchBarApp:faq'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/faq.html')

    def test_view_uses_correct_template_about(self):
        response = self.client.get(reverse('searchBarApp:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/about.html')

    def test_view_uses_correct_template_services(self):
        response = self.client.get(reverse('searchBarApp:services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/services.html')

    def test_view_uses_correct_template_read(self):
        response = self.client.get(reverse('searchBarApp:read'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/read.html')

    def test_view_uses_correct_template_users(self):
        response = self.client.get(reverse('searchBarApp:users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/read.html')
'''
    def test_view_uses_correct_template_Addreview(self):
        response = self.client.get(reverse('searchBarApp:AddReview'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp:searching')


    def test_view_uses_correct_template_index(self):
        response = self.client.get(reverse('searchBarApp:result'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/search.html')
'''
#URL-testing
class URL_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")

    def test_url_uses_correct_template_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template_base(self):
        response = self.client.get(reverse('searchBarApp:base'))
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template_contact(self):
        response = self.client.get(reverse('searchBarApp:contact'))
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template_blog(self):
        response = self.client.get(reverse('searchBarApp:blog'))
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template_faq(self):
        response = self.client.get(reverse('searchBarApp:faq'))
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template_about(self):
        response = self.client.get(reverse('searchBarApp:about'))
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template_services(self):
        response = self.client.get(reverse('searchBarApp:services'))
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template_read(self):
        response = self.client.get(reverse('searchBarApp:read'))
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template_users(self):
        response = self.client.get(reverse('searchBarApp:users'))
        self.assertEqual(response.status_code, 200)
