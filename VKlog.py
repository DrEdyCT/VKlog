import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class VKlog(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("http://www.vk.com")
        assert 'VK' in driver.title
        login = driver.find_element_by_name("email")
        login.send_keys("email")
        password = driver.find_element_by_name("pass")
        password.send_keys("pass")
        password.send_keys(Keys.RETURN)

if __name__ == "__main__":
    unittest.main()
