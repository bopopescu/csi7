from cgitb import text

from csi7.csi7_login import Login
from selenium_elements.selenum_fetchelement import Element
from util.conf import selenium_webdriver
from csi7.configure import ElementFeatureValue
import time
import os
from stat import *


class DownloadLocalAgent:

    def test_download(self):
        launch_browser = selenium_webdriver.driver
        time.sleep(10)
        Element.fetch_element_by_xpath(launch_browser, ElementFeatureValue.ctrl_scanning_xpath).click()
        time.sleep(5)
        Element.fetch_element_by_partial_linktext(launch_browser, ElementFeatureValue.ctrl_download_tag).click()

    def test_downloadversion(self):
        launch_browser = selenium_webdriver.driver
        time.sleep(10)
        Element.fetch_element_by_partial_linktext(launch_browser, ElementFeatureValue.ctrl_download_link).click()
        time.sleep(5)

#this function is mainly to get the size of the downloaded file
    def test_downloadFileLocation(self):
        #fileLocation = os.access("/home/anusha/Downloads/csia.exe",os.F_OK) ,, this is to check if the location has file specified ,, F_OK is to check the existence of path
        #print("file is there?", fileLocation)
        #st = os.stat("/home/anusha/Downloads/csia.exe")
#this try catch is to check if the location has file downloaded and what is the size of the file
        try:
            st = os.stat("/home/anusha/Downloads/csia.exe")
        except IOError:
            print ("failed to get the file",st)
        else:
            size = st[ST_SIZE]
            return print ("file size", st[ST_SIZE]) #ST_SIZE is pre-defined variable in class stat to get the size of the file


#downloadLocalAgent.test_download(None)
#downloadLocalAgent.test_downloadversion(None)
#downloadLocalAgent.test_downloadFileLocation(None)