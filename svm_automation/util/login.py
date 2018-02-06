import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from util.conf import Credentials
from util.conf import SeleniumWebdriver
from util.conf import ElementValueLogin
from selenium_elements.selenum_fetchelement import Element

class SVMLogin:
    launch_driver = SeleniumWebdriver.driver
    launch_driver.get(Credentials.url)
    Element.fetch_element_by_id(launch_driver, ElementValueLogin.ctrl_login).send_keys(Credentials.user_name)
    Element.fetch_element_by_id(launch_driver, ElementValueLogin.ctrl_password).send_keys(Credentials.password)
    Element.fetch_element_by_id(launch_driver, ElementValueLogin.btn_submit).click()





