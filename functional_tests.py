from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Checking the homepage of the to-do app.
        self.browser.get('http://localhost:8000')

        # The page title and header must mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Someone is invited to enter a to-do item straight away

        # The person types "Buy peacock feathers" into a text box
        # (This person hobby is tying fly-fishing lures)

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting him to add another item. she
        # enters "Use peacock feathers to make a fly" (He is very methodical)

        # The page update again, and now shows both items on her list

        # He wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')