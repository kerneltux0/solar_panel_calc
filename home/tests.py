from django.test import TestCase
from django.urls import resolve
from home.views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)
    
    def test_home_page_content(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        redir = '/location'
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Solar Panel Calculator</title>', html)
        self.assertIn('<h1>Welcome to the Solar Panel Calculator</h1>', html)
        self.assertIn('<p>Here, you can figure out how many solar panels you would need to go off-grid according to your current power usage.</p><br>', html)
        self.assertIn("<p>This is meant to be a ballpark figure. This uses data from the Nat'l Renewable Energy Laboratory to grab the amount of useable solar energy in your area, and is only one piece of the puzzle. Going off-grid involves many variables that are best answered by a certified installer.</p><br>", html)
        self.assertIn('<form><submit>Start!</submit></form>', html)
        self.assertTrue(html.endswith('</html>'))
        self.assertRedirects(redir)
