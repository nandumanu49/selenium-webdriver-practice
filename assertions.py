<<<<<<< HEAD
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")

    def test_google_search(self):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)

        self.assertIn("Selenium", self.driver.title)
        search_results = self.driver.find_elements(By.CSS_SELECTOR, "h3")
        self.assertGreater(len(search_results), 0)
        first_result = search_results[0]
        self.assertIn("Selenium", first_result.text)

        self.driver.execute_script("window.open('https://www.python.org', '_blank');")

        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual("Welcome to Python.org", self.driver.title)

        # Close the new window
        self.driver.close()

        # Switch back to the original window
        self.driver.switch_to.window(self.driver.window_handles[0])

        search_box.is_displayed()
        images_link = self.driver.find_element(By.LINK_TEXT, "Images")
        self.assertTrue(images_link.is_displayed())
        self.assertTrue(images_link.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
=======
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")

    def test_google_search(self):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)

        self.assertIn("Selenium", self.driver.title)
        search_results = self.driver.find_elements(By.CSS_SELECTOR, "h3")
        self.assertGreater(len(search_results), 0)
        first_result = search_results[0]
        self.assertIn("Selenium", first_result.text)

        self.driver.execute_script("window.open('https://www.python.org', '_blank');")

        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual("Welcome to Python.org", self.driver.title)

        # Close the new window
        self.driver.close()

        # Switch back to the original window
        self.driver.switch_to.window(self.driver.window_handles[0])

        search_box.is_displayed()
        images_link = self.driver.find_element(By.LINK_TEXT, "Images")
        self.assertTrue(images_link.is_displayed())
        self.assertTrue(images_link.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
>>>>>>> origin/main
