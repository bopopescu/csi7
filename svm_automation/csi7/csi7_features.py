from util.conf import SeleniumWebDriver
#from util.conf import ElementValueLogin
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

class features:
    def __init__(self):
        self.launch_browser = SeleniumWebDriver.browser

    def DownloadAgent(self):
        self.launch_browser = SeleniumWebDriver.browser
        time.sleep(5)

        Element.fetch_element_by_partial_linktext(self.launch_browser, 'Scanning').click()
        print("Scanning\n")
        for file in os.scandir(Credentials.downloadPath):
            print(file.path)
            os.unlink(file.path)

        try:
            time.sleep(5)
            Element.fetch_element_by_partial_linktext(self.launch_browser, "Download Local Agent").click()

            print("Found Donwlaod local Agent")

        except NoSuchElementException:
            print("Error: Download Local Agent")
        SeleniumWebDriver.browser.implicitly_wait(500)
        try:
            Element.fetch_element_by_partial_linktext(self.launch_browser, "Microsoft Windows").click()
            print("Found Donwlaod local Agent2")
            fileName = Credentials.downloadPath + "csia.exe"
            print(fileName)
            status = os.path.isfile(fileName)
            print("status", status)
            if status:

                size = os.path.getsize(fileName)
                print("size of csia=", size)
            else:
                print("File not found\n")
            info = os.stat(fileName)

        except NoSuchElementException:
            print("ERROR: Download Microsoft Windows")



    def createUser(self, username, usertype,):
        time.sleep(5)
        Element.fetch_element_by_partial_linktext(self.launch_browser,"Administration").click()
        print("Administration Clicked\n")

        time.sleep(5)

        Element.fetch_element_by_partial_linktext(self.launch_browser,"User Management").click()
        time.sleep(3)
        #Element.fetch_element_by_xpath(self.launch_browser,"//button[@id='ext-gen302']").click()
        Element.fetch_element_by_xpath(self.launch_browser, "//table[@id='sfw.csiUserManagement_create_new_button']/tbody/tr[2]/td[2]/em/button").click()


        Element.fetch_element_by_xpath(self.launch_browser,
                                       "//input[@id='sfw.csiUserManagement_account_name']").send_keys(username)
        Element.fetch_element_by_xpath(self.launch_browser,
                                       "//input[@id='sfw.csiUserManagement_account_username']").send_keys(username)
        Element.fetch_element_by_xpath(self.launch_browser,
                                       "//input[@id='sfw.csiUserManagement_account_email']").send_keys("smallikarjunappa@flexera.com")
        Element.fetch_element_by_xpath(self.launch_browser,
                                       "//input[@id='sfw.csiUserManagement_recipient_email']").send_keys("smallikarjunappa@flexera.com")
        if usertype == 'RWUser':
            Element.fetch_element_by_xpath(self.launch_browser,
                                           "//input[@id='sfw.csiUserManagement_roleCheckbox_scanning']").click()
            Element.fetch_element_by_xpath(self.launch_browser,
                                           "//input[@id='sfw.csiUserManagement_roleCheckbox_patching']").click()
            Element.fetch_element_by_xpath(self.launch_browser,
                                           "//input[@id='sfw.csiUserManagement_roleCheckbox_scanning_filter']").click()
        Element.fetch_element_by_xpath(self.launch_browser,
                                       "//input[@id='sfw.csiUserManagement_roleCheckbox_results']").click()
        Element.fetch_element_by_xpath(self.launch_browser,
                                       "//input[@id='sfw.csiUserManagement_roleCheckbox_reporting']").click()
        Element.fetch_element_by_xpath(self.launch_browser,
                                       "//input[@id='sfw.csiUserManagement_roleCheckbox_db_access']").click()
        time.sleep(5)
        Element.fetch_element_by_xpath(self.launch_browser,"//table[@id='sfw.csiUserManagement_saveAccountButton']/tbody/tr[2]/td[2]/em/button").click()
        time.sleep(5)
        Element.fetch_element_by_xpath(self.launch_browser,"//button[@id='ext-gen98']").click()

    def exportCSV(self):
        print("Inside export CSv")
        Element.fetch_element_by_xpath(self.launch_browser, "//table[@class='x-btn x-btn-noicon x-btn-menu-active']/tbody/tr[2]/td[2]/em/button]").click()
        Element.fetch_element_by_xpath(self.launch_browser,
                                       "//table[@class='x-menu x-menu-floating x-layer']/ul/li[1]/a/span]").click()


    def checkUser(self, usertype, username):

        print("userType, userName", usertype, username)
        if usertype == "default":
            print("I am printing default")
            Checkelements = ['Scanning', 'Results', 'Reporting', 'Administration', 'Configuration']
        elif usertype == "RWUser":
            print("I am not an default user")
            Checkelements = ['Scanning', 'Results', 'Reporting', 'Configuration']
        else:
            print("I am an RO/RE user\n")
            Checkelements = ['Results', 'Reporting']

        try:

            for item in Checkelements:
                if item == 'Reporting' and usertype != 'ReUser':
                    Element.fetch_element_by_partial_linktext(self.launch_browser,item).click()
                    if(Element.fetch_element_by_partial_linktext(self.launch_browser,'Database Access').is_displayed()):
                        print("DBAccess Found")
                    else:
                        print("DBAcess not found")
                        exit(1)
                else:
                    Element.fetch_element_by_partial_linktext(self.launch_browser,item)
                    print("item = ", item)
        except:
            print("NOT FOUND")
            exit(1)


    def fullScreenView(self):

        time.sleep(2)
        Element.fetch_element_by_partial_linktext(self.launch_browser,"Fullscreen View").click()
        time.sleep(30)