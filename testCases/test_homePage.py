import pytest
from selenium import webdriver
from pageObjects.homePage import HomePage
class Test_001_Home:
    baseURL = "https://katalon-demo-cura.herokuapp.com"

    def test_homePage_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "CURA Healthcare Service":
            assert True
        else:
            assert False
