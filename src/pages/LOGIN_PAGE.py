from selenium.webdriver.common.by import By
from src.base_page.LOCATORS import locators
class Login_Page():
    def __init__(self,driver):
        self.driver = driver
        self.login_un= locators.login_username
        self.login_pw = locators.login_password
        self.login_login_btn = locators.login_login_btn

    def username_meth(self,username):
        self.driver.find_element(By.XPATH, self.login_un).clear()
        self.driver.find_element(By.XPATH, self.login_un).send_keys(username)
    def password_meth(self,password):
        self.driver.find_element(By.XPATH, self.login_pw).clear()
        self.driver.find_element(By.XPATH, self.login_pw).send_keys(password)
    def login_meth(self):
        self.driver.find_element(By.XPATH, self.login_login_btn).click()
    def page_title_meth (self, log_title):
        act_title = self.driver.title
        if act_title==log_title:
            print("you land in :" + act_title)
            assert True
        else:
            print("wrong page suppose to land to " + act_title)
            assert False














