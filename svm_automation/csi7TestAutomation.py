#from django.test import TestCase


#from selenium import webdriver
#from util.conf import *
from csi7.csi7_login import Login
from csi7.csi7_features import features
from unittest import TestCase
#import unittest



class TestExecution(TestCase):
#class Monolithic(TestCase):

    def test_AdownloadLocalAgent(self):
        l1 = Login()
        f1 = features()
        one = l1.test_login('default', 'Secunia1')
        second = f1.DownloadAgent()
        third = l1.test_logout()


    def test_CheckUser(self):
        l1 = Login()
        f1 = features()
        fourth = l1.test_login('default','Secunia1')
#         fifth = f1.createUser('testUser20','RWUser')
        sixth=l1.test_logout()
        seventh=l1.test_login('testUser2','Secunia1')
        Eight = f1.checkUser('RWUser','testUser2')
#         nine = l1.test_logout()


if __name__=='__main__':
    TestExecution.test_AdownloadLocalAgent(None)
    TestExecution.test_CheckUser(None)



