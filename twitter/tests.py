from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views

class HomePageTests(SimpleTestCase):
#Developer - Akshaya
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
#Developer - Gowri
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
#Developer - Gulya
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'twitter/home.html')
