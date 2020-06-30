from django.test import TestCase
from django.urls import resolve
from location.views import locateUser
from django.http import HttpRequest

# Create your tests here.

class LocationTest(TestCase):

    def test_location_url(self):
        found = resolve("/location")
        self.assertEqual(found.func, locateUser)

    def test_location_content(self):
        request = HttpRequest()
        response = locateUser(request)
        html = response.content.decode('utf8')