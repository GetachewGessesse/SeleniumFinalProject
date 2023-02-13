from selenium import webdriver
import time
import pytest


class TestBase_Facebook:

    driver = webdriver.Chrome()
    time.sleep(3)

    def test_demoweb(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        return self.driver


# def demoblaz():
#     driver = webdriver.Chrome()
#     time.sleep(3)
#     driver.get("https://www.demoblaze.com/index.html")
#     time.sleep(3)
#     driver.maximize_window()

