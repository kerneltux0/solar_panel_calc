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
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Solar Panel Calculator</title>', html)
        self.assertIn('<h1>Welcome to the Solar Panel Calculator</h1>')
        self.assertTrue(html.endswith('</html>'))
