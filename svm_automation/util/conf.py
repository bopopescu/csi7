from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Credentials:
    url = "http://10.20.151.39"
    username = "default"
    password = "Secunia1"
    downloadPath = "/home/anusha/csi7_automation/Downloads/"

class SeleniumWebDriver:
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/octet-stream')
    fp.set_preference("browser.download.dir", Credentials.downloadPath)
    browser = webdriver.Firefox(executable_path=r'/home/anusha/csi7_automation/svm_automation/geckodriver',firefox_profile=fp)

class ElementValueLogin:
    ctrl_login = "ext-comp-1034"
    ctrl_password = "ext-comp-1035"
    btn_submit = "ext-gen32"

class ElementValueLogout:
    ctrl_logout ="ext-comp-1015"


class ElementFeatureValue:
   #id1 = "ext-gen270"
   ctrl_scanning_xpath = "//li[2]//a/span[text()='Scanning']"
   ctrl_download_tag = "Download Local Agent"
   ctrl_download_link = "Microsoft Windows"



class Dashboard:
    ctrl_classname = "glyphicon-remove"
    ctrl_save_button = "//div[1]/button/span[text()='Save']"
    ctrl_dashboard = "link_dashboard"

class AddDashboard:
    ctrl_add_class = "glyphicons-plus"
    ctrl_advisories = "//div/div/ul/li[1]/a[text()='Advisories released last year']"
    ctrl_devices = "Devices Overview"
    ctrl_device_status = "Devices status - System score"
    ctrl_devices_status_time = "Devices status - Time since last scan"
    ctrl_latest_advisories_affecting_your_security = "Latest advisories affecting your security"
    ctrl_latest_advisories = "Latest advisories"
    ctrl_latest_advisories_per_watchList = "Latest advisories per watch list"
    ctrl_latest_available_patches = "Latest available patches"
    ctrl_most_critical_advisories = "Most critical advisories affecting your security"
    ctrl_most_prevalent_EOL_software_Installations = "Most prevalent EOL software installations"
    ctrl_most_prevalent_insecure_software_installtions = "Most prevalent insecure software installations"
    ctrl_opened_tickets_pattern = "Opened tickets pattern"
    ctrl_open_tickets_split = "Open tickets split by advisory criticality"
    ctrl_tickets_split_by_status = "Tickets split by status"
    ctrl_your_latest_assigned_tickets = "Your latest assigned tickets"



