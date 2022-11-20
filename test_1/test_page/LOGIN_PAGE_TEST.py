import time
from selenium import webdriver
import unittest
import sys
import os
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities.READ_PROPERTIES import ReadConfig
from src.pages.LOGIN_PAGE import Login_Page
class login_Test(unittest.TestCase):
    URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver = self.driver
        driver.get(self.URL)
        login = Login_Page(driver)
        login.page_title_meth("Login - iBilling")
        login.username_meth(self.username)
        login.password_meth(self.password)
        login.login_meth()
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")
if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/ADMIN/PycharmProjects/Excel_project/REPORTS'))

