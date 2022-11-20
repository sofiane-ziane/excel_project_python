
import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.base_page.LOCATORS import locators
class Add_customer_Page():

    def __init__(self,driver):
        self.driver = driver
        self.add_customer_btn_1 = locators.add_customer_btn_1
        self.add_customer_btn_2 = locators.add_customer_btn_2
        self.add_customer_name = locators.add_customer_name
        self.add_customer_company = locators.add_customer_company
        self.add_customer_email = locators.add_customer_email
        self.add_customer_phone = locators.add_customer_phone
        self.add_customer_address = locators.add_customer_address
        self.add_customer_city = locators.add_customer_city
        self.add_customer_state = locators.add_customer_state
        self.add_customer_zip = locators.add_customer_zip
        self.add_customer_country = locators.add_customer_country
        self.add_customer_save_btn = locators.add_customer_save_btn
        self.add_customer_smr = locators.add_customer_smr
        self.add_customer_list_btn = locators.add_customer_list_btn
        self.add_customer_table_rows = locators.add_customer_tableRows
        self.add_customer_table_before= locators.add_customer_table_before
        self.add_customer_table_after = locators.add_customer_table_after
        self.add_customer_delete  = locators.add_customer_delete
        self.add_customer_search_box = locators.add_customer_search_box
        self.add_customer_delete_confirmation = locators.add_customer_delete_confirmation
        self.deletion_message = locators.add_customer_deletion_message
    def add_customer_btn_1_meth(self):
        self.driver.find_element(By.XPATH, self.add_customer_btn_1).click()
    def add_customer_btn_2_meth(self):
        self.driver.find_element(By.XPATH, self.add_customer_btn_2).click()
    def add_customer_name_meth(self, name):
        self.driver.find_element(By.XPATH, self.add_customer_name).send_keys(name)
    def add_customer_company_meth(self, company):
        self.driver.find_element(By.XPATH, self.add_customer_company).send_keys(company)
    def add_customer_email_meth(self, email):
        self.driver.find_element(By.XPATH, self.add_customer_email).send_keys(email)
    def add_customer_phone_meth(self, phone):
        self.driver.find_element(By.XPATH, self.add_customer_phone).send_keys(phone)
    def add_customer_address_meth(self, address):
        self.driver.find_element(By.XPATH, self.add_customer_address).send_keys(address)
    def add_customer_city_meth(self, city):
        self.driver.find_element(By.XPATH, self.add_customer_city).send_keys(city)
    def add_customer_state_meth(self, state):
        self.driver.find_element(By.XPATH, self.add_customer_state).send_keys(state)
    def add_customer_zip_meth(self,zip):
        self.driver.find_element(By.XPATH, self.add_customer_zip).send_keys(zip)
    def add_customer_country_meth(self, country):
        drp = Select(self.driver.find_element(By.XPATH, self.add_customer_country))
        drp.select_by_visible_text(country)
    def add_customer_save_btn_meth(self):
        self.driver.find_element(By.XPATH, self.add_customer_save_btn).click()
    def add_customer_smr_meth(self):
        self.driver.find_element(By.XPATH, self.add_customer_smr)
    def add_customer_list_btn_meth(self):
        self.driver.find_element(By.XPATH, self.add_customer_list_btn).click()
    def add_customer_search_box_meth(self,inject_email):
        self.driver.find_element(By.XPATH, self.add_customer_search_box).send_keys(inject_email)
    def add_customer_table_rows_len_meth(self):
        return len(self.driver.find_elements(By.XPATH, self.add_customer_table_rows))
    def add_customer_validation_ByEmail_delete(self,email):
        for r in range(1,self.add_customer_table_rows_len_meth()+1):
          # table=self.driver.find_element(self.add_customer_table_rows)
          emailid=self.driver.find_element(By.XPATH, self.add_customer_table_before+str(r)+self.add_customer_table_after).text
          if emailid == email:
              self.driver.find_element(By.XPATH, self.add_customer_table_before+str(r)+self.add_customer_delete).click()
              time.sleep(2)
              self.driver.find_element(By.XPATH, self.add_customer_delete_confirmation).click()
              break
          else:
              print("name doesn't exist")
              break
    def take_screenshoot_meth(self):

        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y__%H_%M_%S")
        print("time right now", dt_string)
        self.driver.save_screenshot("C:\\Users\\ADMIN\\PycharmProjects\\Excel_project\\reports\\"+dt_string+".png")
    def page_title_meth (self, log_title):
        act_title = self.driver.title
        if act_title==log_title:
            print("you land in :"+ act_title)
            # assert True
        else:
            print("wrong page please check input provided to >>>configurate.ini<<< suppose to land to :" + act_title)
            # assert False
