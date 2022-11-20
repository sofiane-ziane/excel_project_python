import random
import string
from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from utilities.READ_PROPERTIES import ReadConfig
from src.pages.LOGIN_PAGE import Login_Page
from src.pages.ADD_CUSTOMER import Add_customer_Page
from utilities import EXCEL_UTILS
import time
# used multiple time.sleep for showing testing process purpose
class addloginfromexcel(unittest.TestCase):
    URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    login_title= ReadConfig.get_login_title()
    billing_title = ReadConfig.get_billing_title()
    contact_title = ReadConfig.get_contact_title()
    path = "C:\\Users\\ADMIN\\PycharmProjects\\Excel_project\\data_from_excel\\data_eco.xlsx"
    FullName = EXCEL_UTILS.readData(path, 'Sheet1', 2, 1)
    CompanyName= EXCEL_UTILS.readData(path, 'Sheet1', 2, 2)
    Email= EXCEL_UTILS.readData(path, 'Sheet1', 2, 3)
    Phone= EXCEL_UTILS.readData(path, 'Sheet1', 2, 4)
    Address= EXCEL_UTILS.readData(path, 'Sheet1', 2, 5)
    City= EXCEL_UTILS.readData(path, 'Sheet1', 2, 6)
    Country= EXCEL_UTILS.readData(path, 'Sheet1', 2, 7)
    state= EXCEL_UTILS.readData(path, 'Sheet1', 2, 8)
    Zip= EXCEL_UTILS.readData(path, 'Sheet1', 2, 9)
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver = self.driver
        driver.get(self.URL)
        log_in = Login_Page(driver)
        log_in.page_title_meth(self.login_title)
        log_in.username_meth(self.username)
        log_in.password_meth(self.password)
        log_in.login_meth()
        add_cust = Add_customer_Page(driver)
        g_email = random_generator()+"@"+self.Email
        gn = random.randint(0, 1000)
        add_cust.page_title_meth(self.billing_title)
        time.sleep(1)
        add_cust.add_customer_btn_1_meth()
        time.sleep(1)
        add_cust.add_customer_btn_2_meth()
        time.sleep(1)
        add_cust.page_title_meth(self.contact_title)
        add_cust.add_customer_name_meth(self.FullName)
        time.sleep(1)
        add_cust.add_customer_company_meth(self.CompanyName)
        time.sleep(1)
        add_cust.add_customer_email_meth(g_email)
        time.sleep(1)
        add_cust.add_customer_phone_meth(gn + self.Phone)
        time.sleep(1)
        add_cust.add_customer_address_meth(self.Address)
        time.sleep(1)
        add_cust.add_customer_city_meth(self.City)
        time.sleep(1)
        add_cust.add_customer_state_meth(self.state)
        time.sleep(1)
        add_cust.add_customer_zip_meth(self.Zip)
        time.sleep(1)
        add_cust.add_customer_country_meth(self.Country)
        time.sleep(1)
        add_cust.take_screenshoot_meth()
        time.sleep(1)
        add_cust.add_customer_save_btn_meth()
        time.sleep(1)
        add_cust.add_customer_list_btn_meth()
        time.sleep(1)
        add_cust.add_customer_search_box_meth(g_email)
        time.sleep(1)
        add_cust.add_customer_validation_ByEmail_delete(g_email)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("test completed")
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/ADMIN/PycharmProjects/Excel_project/REPORTS'))
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


