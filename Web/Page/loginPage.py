from selenium.webdriver.common.by import By
from Web.Locators.login_locators import LoginLocators
from Web.Base.base import *
import allure


class Login(LoginLocators):

    def __init__(self, driver):
        self.driver = driver
        self.baseURL = LoginLocators.baseURL
        self.login_link_locator_linkText = LoginLocators.login_link_locator_linkText
        self.login_username_field_locator_id = LoginLocators.login_username_field_locator_id
        self.login_password_field_locator_id = LoginLocators.login_password_field_locator_id
        self.login_button_locator_xpath = LoginLocators.login_button_locator_xpath
        self.login_close_button_locator_xpath = LoginLocators.login_close_button_locator_xpath
        self.logout_link_locator_id = LoginLocators.logout_link_locator_id
        self.welcome_txt_locator_id = LoginLocators.welcome_txt_locator_id


    @allure.step
    @allure.description('Navigate to demoblaz website')
    def open_demoblaz(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    @allure.step
    @allure.description('Click on login link text')
    def click_on_login_link(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link_locator_linkText).click()


    @allure.step
    @allure.description('Clear and send keys to username field')
    def setUsername(self, username):
        self.driver.find_element(By.ID, self.login_username_field_locator_id).clear()
        self.driver.find_element(By.ID, self.login_username_field_locator_id ).send_keys(username)

    @allure.step
    @allure.description('Clear and send keys to password field')
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.login_password_field_locator_id).clear()
        self.driver.find_element(By.ID, self.login_password_field_locator_id ).send_keys(password)

    @allure.step
    @allure.description('Click on login button')
    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_locator_xpath).click()

    @allure.step
    @allure.description('Click on close button')
    def click_on_close_button(self):
        self.driver.find_element(By.XPATH, self.login_close_button_locator_xpath).click()

    @property
    @allure.step
    @allure.description('Verify the welcome text displayed after login')
    def welcome_text_getter(self):
        return self.driver.find_element(By.ID, self.welcome_txt_locator_id).text

    @allure.step
    @allure.description('Click on close button')
    def click_logout_link(self):
        self.driver.find_element(By.ID, self.logout_link_locator_id).click()


    @allure.step
    @allure.description('Click ok/ accept popup alert message')
    def alert_popup_accepter(self):
        self.driver.switch_to.alert.accept()

    @property
    @allure.step
    @allure.description('Extracting message from popup alert window')
    def alert_popup_text(self):
        return self.driver.switch_to.alert.text


    @property
    @allure.step
    @allure.description('Verify the login text displayed after logout')
    def login_text_getter(self):
        return self.driver.find_element(By.LINK_TEXT, self.login_link_locator_linkText ).text



















