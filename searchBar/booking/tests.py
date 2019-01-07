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
'''
    def test_con_indi(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('booking:con_indi'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book_indi.html')

    def test_con_orga(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('booking:con_orga'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book_orga.html')

    def test_book_train_indi(self):
        #self.client.force_login(self.user)
        response = self.client.get(reverse('booking:book_train_indi'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/list_train.html')



    def test_view_book_air_orga(self):
        response = self.client.get(reverse('booking:book_air_indi'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/list_flight.html')
'''

class URL_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")
'''
    def test_con_indi(self):
        response = self.client.get(reverse('booking:con_indi'))
        self.assertEqual(response.status_code, 302)

    def test_con_orga(self):
        response = self.client.get(reverse('booking:con_orga'))
        self.assertEqual(response.status_code, 302)


    def test_book_train_indi(self):
        #self.client.force_login(self.user)
        response = self.client.get(reverse('booking:book_train_indi'))
        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, 'booking/list_train.html')


class Form_Testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")
'''