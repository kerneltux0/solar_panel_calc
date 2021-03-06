from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_visit_site(self):
        root = 'http://localhost:8000'
        # user goes to web-site
        self.browser.get(root)
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
    
    def test_location(self):
        location = 'http://localhost:8000/location'
        self.browser.get(location)
        # user sees a page with one text field & submit button
        formField = self.browser.find_element_by_name('postal code')
        formButton = self.browser.find_element_by_name('submit')
        # after entering invalid postal code, user sees error message
        formField.send_keys('sonteuhoetnsa')
        formButton.click()
        formError = self.browser.find_element_by_name('Error')
        self.assertTrue(formError)
        # after entering valid postal code, user sees success message & "next" link/button
        formField.send_keys('M4V')
        formButton.click()
        formSuccess = self.browser.find_element_by_name('Success')
        self.assertTrue(formSuccess)
        # user is redirected to /power
        print("Location Test Passed")

# user sees message asking for kw/h usage

# user sees message about varying power usage

# user sees one number field & submit button

# user enters kw/h usage & clicks "submit"

# user is routed to /results

# user sees ballpark figure disclaimer

# user sees result in m^2 or ft^2
if __name__ == '__main__':
    unittest.main(warnings='ignore')