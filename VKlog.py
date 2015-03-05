# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import unittest
from config import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class VKlog(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("http://www.vk.com")
        assert 'VK' in driver.title
        login = driver.find_element_by_name("email")
        login.send_keys(EMAIL)
        password = driver.find_element_by_name("pass")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)
        dialogs = driver.find_element_by_xpath("//li[@id='l_msg']/a/span[2]")
        dialogs.click()
        find_friend = driver.find_element_by_id("im_filter")
        find_friend.send_keys(FRIEND_NAME)
        find_friend.send_keys(Keys.RETURN)
        sendtext = driver.find_element_by_xpath("//div[@id='page_wrap']/div/div")
        sendtext.send_keys(TEXT)
        sendtext.send_keys(Keys.RETURN)
        
if __name__ == "__main__":
    unittest.main()
