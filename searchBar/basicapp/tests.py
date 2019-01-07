from django.test import TestCase ,Client
from django.http import HttpRequest
from django.urls import reverse
from .models import UserProfileInfo
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

    def test_view_register(self):
        response = self.client.get(reverse('basicapp:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/registration.html')

    def test_user_login(self):
        response = self.client.get(reverse('basicapp:user_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/login.html')

    def test_user_profile(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('basicapp:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/profile.html')

    def test_user_profile_update(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('basicapp:update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/update_profile.html')

    def test_visited_industries(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('basicapp:visited_industries'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/visited.html')

    def test_Booked_industries(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('basicapp:booked_to_visit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/booked_to_visit.html')
'''
    def test_charge1(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('basicapp:charge1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/booking_charge.html')

    def test_charge2(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('basicapp:charge2'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/booking_charge.html')


    def test_Cancelticket(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('basicapp:cancel_ticket'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/booked_to_visit.html')

    def test_activate(self,**kwargs,**kwargs1):
        response = self.client.get(reverse('basicapp:activate',**kwargs,**kwargs1))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBarApp/index.html')


class Forms_Testing(TestCase):

    def test_UserProfileInfoForms(self):
        invalid_data = {
                'username':"Hemanth",
                'email':"hreddy281@gmail.com",
                'password':1254,
                'name':'hemanth',
                'gender':"K"
            }
        form = UserProfileInfo(data = invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)
'''

#URL-Testing
class URL_testing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username = "hemanth",email='hreddy281@gmail.com', password='devilmaycry4')
        cls.profile = UserProfileInfo.objects.create(user = cls.user,name = "hemanth",gender = "M")

    def test_URL_register(self):
        response = self.client.get(reverse('basicapp:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/registration.html')

    def test_URL_user_login(self):
        response = self.client.get(reverse('basicapp:user_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basicapp/login.html')

    def test_URL_profile(self):
        #self.client.force_login(self.user)
        response = self.client.get(reverse('basicapp:profile'))
        self.assertEqual(response.status_code, 302)
        #self.assertTemplateUsed(response, 'basicapp/profile.html')

    def test_URL_profile_update(self):
        response = self.client.get(reverse('basicapp:update'))
        self.assertEqual(response.status_code, 302)

    def test_URL_visited_industries(self):
        response = self.client.get(reverse('basicapp:visited_industries'))
        self.assertEqual(response.status_code, 302)

    def test_URL_bookinglist_update(self):
        response = self.client.get(reverse('basicapp:booked_to_visit'))
        self.assertEqual(response.status_code, 302)
'''
    def test_URL_charge1(self):
        response = self.client.get(reverse('basicapp:charge1'))
        self.assertEqual(response.status_code, 302)

    def test_URL_charge2(self):
        response = self.client.get(reverse('basicapp:charge2'))
        self.assertEqual(response.status_code, 302)
'''