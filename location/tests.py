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
        self.assertIn('<h1>Location</h1></br>',html)
        # user sees message about location data
        self.assertIn('<p>Please enter the zip/postal code for the location where you intend to install the solar panels.</p></br>',html)
        # user sees a form with one text field, submit button, and pulls location data from API
        self.assertIn("<form method='GET'>\n    <input type='text' name='postal code' placeholder='Postal Code'>\n    <input type='submit'/>\n  </form>",html)

    def test_location_behavior(self):
        
        # returns empty array for invalid zip/postal code
        # latitude-longitude saved to session
        # "next" link appears after session data cached