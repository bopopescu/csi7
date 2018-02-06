from django.test import TestCase


#from selenium import webdriver
#from util.conf import *
from csi7.csi7_login import Login
from csi7.csi7_features import features
from unittest import TestCase
import unittest

#l1=Login()
#f1 = features()

class CSI_TestExecution(unittest.TestCase):
    def test_login(self):
        #self.a=1
        #self.assertEqual(None,1,self.a)
        # self.assertEqual(1+1,2)
        # resp=self.client.get('/polls/')
        # self.assertEqual(resp.status_code,200)
        # self.assertTrue('latest_poll_list' in resp.context)
        # self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']],[1])
        l1=Login()
        first= l1.test_login('default','Secunia1')

    def test_Downloadgent(self):
         f1=features()
         second = f1.DownloadAgent()
    def test_CreateUser(self):
         f1 = features()
         third = f1.createUser('testUser3','ROUser')
    def test_FirstLogout(self):
         l1=Login()
         Fourth = l1.test_logout()
    def test_LoginSecondTime(self):
         l1=Login()
         fifth = l1.test_login('testUser2','Secunia1')
    def test_checkUser(self):
         f1=features()
         sixth = f1.checkUser('testUser2','RWUser')
    def test_FinalLogout(self):
         l1=Login()
         Seventh = l1.test_logout()
    def tearDown(self):
         l1=Login()
         Eight=l1.test_closeBrowser()



#f1.exportCSV()
#f1.DownloadAgent()
#username='testUser4'
#userType = 'RWUser'
#f1.createUser(username,userType)
#l1.logout()
#l1.login('testUser2','Secunia1')
#f1.checkUser('testUser2','RWUser')
#l1.logout()
#l1.closeBrowser()


# CSI_TestExecution.test_login(None)
# CSI_TestExecution.test_Downloadgent(None)
# CSI_TestExecution.test_CreateUser(None)
# CSI_TestExecution.test_FirstLogout(None)
# CSI_TestExecution.test_LoginSecondTime(None)
# CSI_TestExecution.test_checkUser(None)
# CSI_TestExecution.test_FinalLogout(None)
# CSI_TestExecution.tearDown(None)

# Create your tests here.


if __name__ == '__main__':
    unittest.main()