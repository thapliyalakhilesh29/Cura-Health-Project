from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_xpath = "//input[@id='txt-username']"
    textbox_password_xpath = "//input[@id='txt-password']"
    button_login_id = "btn-login"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_xpath).clear()
        self.driver.find_element(By.ID, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_xpath).clear()
        self.driver.find_element(By.ID, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()








