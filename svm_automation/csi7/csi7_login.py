#from csi7.configure import Credentials
#from csi7.configure import ElementValueLogin
#from selenium_elements.selenum_fetchelement import Element
#from csi7.configure import SeleniumWebDriver

from util.conf import SeleniumWebDriver
from util.conf import ElementValueLogin
from util.conf import ElementValueLogout
from util.conf import Credentials
from selenium_elements.selenum_fetchelement import Element
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pymysql import cursors as curs, connect
import time
#import sys

import os


class Login:
    def __init__(self):
        self.launch_browser = SeleniumWebDriver.browser

    def test_login(self,username,password):
        new_browser = self.launch_browser.get(Credentials.url)
        time.sleep(2)
        Element.fetch_element_by_id(self.launch_browser, ElementValueLogin.ctrl_login).send_keys(username)
        Element.fetch_element_by_id(self.launch_browser, ElementValueLogin.ctrl_password).send_keys(password)
        Element.fetch_element_by_id(self.launch_browser, ElementValueLogin.btn_submit).click()
        time.sleep(2)

    def test_logout(self):
        Element.fetch_element_by_id(self.launch_browser,ElementValueLogout.ctrl_logout).click()
        try:
            time.sleep(2)
            Element.fetch_element_by_id(self.launch_browser,"ext-gen100").click()
        except NoSuchElementException:
            print("Element not found\n")

    def test_closeBrowser(self):
        self.launch_browser.close()

