# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import pyodbc
#
# login_link_locator_linkText = "Log in"
# login_username_field_locator_id = "loginusername"
# login_password_field_locator_id = "loginpassword"
# login_button_locator_xpath = "//button[contains(text(),'Log in')]"
# login_close_button_locator_xpath = "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[1]"
# logout_link_locator_id = "logout2"
# welcome_txt_locator_id = "nameofuser"
#
# def test_sample_login():
#     driver = webdriver.Chrome()
#     driver.get("https://www.demoblaze.com/index.html")
#     driver.maximize_window()
#     time.sleep(6)
#     driver.find_element(By.LINK_TEXT, "Log in").click()
#     time.sleep(6)
#     driver.find_element(By.ID, login_username_field_locator_id).clear()
#     time.sleep(2)
#     driver.find_element(By.ID, login_username_field_locator_id).send_keys("azuta")
#     time.sleep(2)
#     driver.find_element(By.ID, login_password_field_locator_id).clear()
#     time.sleep(2)
#     driver.find_element(By.ID, login_password_field_locator_id).send_keys("azuta1234")
#     time.sleep(2)
#     driver.find_element(By.XPATH, login_button_locator_xpath).click()
#     time.sleep(10)
#     welcome = driver.find_element(By.ID, welcome_txt_locator_id).text
#     print(welcome)
#     if "Welcome" in welcome:
#         assert True
#     else:
#         assert False
#     driver.close()
#
#
#
# baseURL = "https://www.demoblaze.com/index.html"
# signup_link_locator_id = "signin2"
# signup_username_field_locator_id = "sign-username"
# signup_password_field_locator_id = "sign-password"
# signup_button_locator_xpath = "//button[contains(text(),'Sign up')]"
# signup_close_button_locator_xpath = "//body/div[@id='signInModal']/div[1]/div[1]/div[3]/button[1]"
#
#
# def test_sample_signup():
#     driver = webdriver.Chrome()
#     driver.get("https://www.demoblaze.com/index.html")
#     driver.maximize_window()
#     time.sleep(6)
#     driver.find_element(By.ID, signup_link_locator_id).click()
#     time.sleep(6)
#     # driver.find_element(By.ID, login_username_field_locator_id).clear()
#     # time.sleep(2)
#     # driver.find_element(By.ID, login_username_field_locator_id).send_keys("azuta")
#     # time.sleep(2)
#     # driver.find_element(By.ID, login_password_field_locator_id).clear()
#     # time.sleep(2)
#     # driver.find_element(By.ID, login_password_field_locator_id).send_keys("azuta1234")
#     # time.sleep(2)
#     # driver.find_element(By.XPATH, login_button_locator_xpath).click()
#     # time.sleep(10)
#
#
#
# def test_cart():
#     driver = webdriver.Chrome()
#     driver.get("https://www.demoblaze.com/index.html")
#     driver.maximize_window()
#     time.sleep(6)
#     driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]").click()
#     time.sleep(3)
#     driver.switch_to.alert.accept()
#     time.sleep(3)
#     driver.find_element(By.LINK_TEXT, "Cart").click()
#     time.sleep(5)
#     c = driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]").text
#     print(c)
#
#
# def test_home_laptops():
#     driver = webdriver.Chrome()
#     driver.get("https://www.demoblaze.com/index.html")
#     driver.maximize_window()
#     time.sleep(6)
#     driver.find_element(By.LINK_TEXT, "Laptops").click()
#     time.sleep(5)
#     driver.find_element(By.ID, "tbodyid")
#     time.sleep(5)
#     laptops = driver.find_elements(By.CLASS_NAME, "hrefch")
#
#     for i in laptops:
#        print(len(laptops))
#        assert len(laptops) == 6
#        break
#
#
# def test_home_phone():
#     driver = webdriver.Chrome()
#     driver.get("https://www.demoblaze.com/index.html")
#     driver.maximize_window()
#     time.sleep(6)
#     driver.find_element(By.LINK_TEXT, "Phones").click()
#     time.sleep(5)
#     driver.find_element(By.ID, "tbodyid")
#     time.sleep(5)
#     phones = driver.find_elements(By.CLASS_NAME, "hrefch")
#
#     for i in phones:
#        print(len(phones))
#        assert len(phones) == 7
#        break
#
#
# def test_home_monitors():
#     driver = webdriver.Chrome()
#     driver.get("https://www.demoblaze.com/index.html")
#     driver.maximize_window()
#     time.sleep(6)
#     driver.find_element(By.LINK_TEXT, "Monitors").click()
#     time.sleep(5)
#     driver.find_element(By.ID, "tbodyid")
#     time.sleep(5)
#     monitors = driver.find_elements(By.CLASS_NAME, "hrefch")
#
#     for i in monitors:
#        print(len(monitors))
#        assert len(monitors) == 3
#        break
import pyodbc


def database():

    # conn = pyodbc.connect('Driver={SQL Server};'
    #                       'Server=LAPTOP-CFNBSI63;'
    #                       'Database=student;'
    #                       'Trusted_Connection=yes;')
    #
    # cursor = conn.cursor()
    # cursor.execute('SELECT * FROM st1')
    # for i in cursor:
    #     print(i)
    #
    # import pyodbc
    #
    # conn = pyodbc.connect('Driver={SQL Server};'
    #                       'Server=LAPTOP-CFNBSI63;'
    #                       'Database=database_name;'
    #                       'Trusted_Connection=yes;')
    #
    # cursor = conn.cursor()
    # cursor.execute('SELECT * FROM table_name')
    #
    # for i in cursor:
    #     print(i)

    import pyodbc

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server= LAPTOP-CFNBSI63;'
                          'Database= Northwind;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')

    for i in cursor:
        print(i)












