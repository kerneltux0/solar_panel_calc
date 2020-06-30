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
        # user sees message about location data
        # user sees a form with one text field & submit button
        # user sees error message for invalid postal code
        # user sees success message & "next" link/button for correct postal code