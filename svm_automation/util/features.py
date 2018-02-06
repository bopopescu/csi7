from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time

from util.login import SVMLogin
from util.conf import SeleniumWebdriver
from util.conf import ElementValueFeatures
from selenium_elements.selenum_fetchelement import Element


class FeatureClick:

    def test_dashboard_click(self):
        new_driver = SeleniumWebdriver.driver
        time.sleep(10)
        Element.fetch_element_by_id(new_driver,ElementValueFeatures.ctrl_dashboard).click()

    def test_notification_click(self):
        new_driver = SeleniumWebdriver.driver
        time.sleep(10)
        Element.fetch_element_by_id(new_driver, ElementValueFeatures.ctrl_notification).click()

    def test_feature_vulnerability_click(self):
        new_driver = SeleniumWebdriver.driver
        time.sleep(10)
        Element.fetch_element_by_partial_linktext(new_driver, ElementValueFeatures.ctrl_vulnerability).click()

















