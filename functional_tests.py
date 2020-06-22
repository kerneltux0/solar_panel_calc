from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # do something
    
    def tearDown(self):
        # do something
    
    def test_one(self):
        # do something

# user goes to web-site
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# user sees "Solar Panel Calculator" in the title
assert 'Solar Panel Calculator' in browser.title, "Browser Title was:" + browser.title

# user sees a welcome message describing what the site accomplishes

# user clicks on button labeled "start here"

# user is taken to /location

# user sees message about location data

# user sees a page with one text field & submit button

# field accepts a zip/postal code

# if not valid, user sees an error message

# if valid, user sees success message & button labeled "next"

# user clicks "next" and routed to /power

# user sees message asking for kw/h usage

# user sees message about varying power usage

# user sees one number field & submit button

# user enters kw/h usage & clicks "submit"

# user is routed to /results

# user sees ballpark figure disclaimer

# user sees result in m^2 or ft^2

browser.quit()
print('Test passed')