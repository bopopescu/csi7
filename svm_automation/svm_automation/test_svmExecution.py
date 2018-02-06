from unittest import TestCase
from util.features import FeatureClick
from dashboard.removeAll import removeAllDashboard
from selenium_elements.selenum_fetchelement import Element
from util.conf import SeleniumWebdriver
from util.conf import Dashboard
import time

class TestsvmExecution(TestCase):
    #this def runs each funtion from class feature_click()
    def test_test_featureclick(self):
        run = FeatureClick()
        run.test_dashboard_click()
        run.test_feature_vulnerability_click()
        run.test_notification_click()
        time.sleep(5)



    def test_remove_dashboard(self):
        obj = FeatureClick()
        obj.test_dashboard_click() #runs the test_dashboard_click() from class feature_clic()
        obj2 = removeAllDashboard()
        obj2.test_remove() #then test_remove() function will be run from removeAllDashboard() class




#TestsvmExecution().test_test_featureclick()
# TestsvmExecution().test_remove_dashboard()
if __name__ == "__main__":
    TestsvmExecution().test_test_featureclick()
    TestsvmExecution().test_remove_dashboard()
