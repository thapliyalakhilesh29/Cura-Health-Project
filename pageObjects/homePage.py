from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    button_appointment_id = "btn-make-appointment"

    def __init__(self, driver):
        self.driver = driver

    def clickAppointment(self):
        self.driver.find_element(By.ID, self.button_appointment_id).click()
