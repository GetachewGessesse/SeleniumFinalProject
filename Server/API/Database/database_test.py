
from selenium import webdriver
import pyodbc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Web.Locators.login_locators import *
import time

import pyodbc
def test_data_entry():
    # driver = webdriver.Chrome()
    # driver.get("https://www.demoblaze.com/index.html")
    # driver.maximize_window()
    # time.sleep(3)
    x = LoginLocators
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-CFNBSI63;'
                          'Database=Northwind;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees where EmployeeID = 1 or EmployeeID = 3 or EmployeeID = 5')

    for i in cursor:
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://www.demoblaze.com/index.html")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, x.login_link_locator_linkText).click()
        driver.find_element(By.ID, x.login_username_field_locator_id).clear()
        driver.find_element(By.ID, x.login_username_field_locator_id).send_keys(i[1])
        driver.find_element(By.ID, x.login_password_field_locator_id).clear()
        driver.find_element(By.ID, x.login_password_field_locator_id).send_keys(i[2])
        driver.find_element(By.XPATH, x.login_button_locator_xpath).click()
        time.sleep(3)
        driver.switch_to.alert.dismiss()
        time.sleep(3)
        # driver.find_element(By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[1]/button[1]/span[1]")
        driver.close()
        # print(i)

test_data_entry()
