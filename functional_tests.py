from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_visit_site(self):
        root = 'http://localhost:8000'
        # user goes to web-site
        self.browser.get('http://localhost:8000')
        # user sees "Solar Panel Calculator" in the title
        self.assertIn('Solar Panel Calculator', self.browser.title)
        # user clicks on link labeled "Start!"
        link = self.browser.find_element_by_link_text('Start!')
        # user clicks on link labeled "Start!"
        link.click()
        # user is taken to /location
        self.assertEquals(
            self.browser.current_url,
            root + '/location'
        )
        print("Visit Site Test Passed")


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
if __name__ == '__main__':
    unittest.main(warnings='ignore')