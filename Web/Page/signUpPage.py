from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.signUp_Locators import SignUpLocators
import allure

class Signup(SignUpLocators):
    baseURL = "https://www.demoblaze.com/index.html"
    signup_link_locator_id = "signin2"
    signup_username_field_locator_id = "sign-username"
    signup_password_field_locator_id = "sign-password"
    signup_button_locator_xpath = "//button[contains(text(),'Sign up')]"
    signup_close_button_locator_xpath = "//body/div[@id='signInModal']/div[1]/div[1]/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver
        self.baseURL = SignUpLocators.baseURL
        self.signup_link_locator_id = SignUpLocators.signup_link_locator_id
        self.signup_username_field_locator_id = SignUpLocators.signup_username_field_locator_id
        self.signup_password_field_locator_id = SignUpLocators.signup_password_field_locator_id
        self.signup_button_locator_xpath = SignUpLocators.signup_button_locator_xpath
        self.signup_close_button_locator_xpath = SignUpLocators.signup_close_button_locator_xpath



    @allure.step
    @allure.description('Navigate to demoblaz website')
    def open_demoblaz(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


    @allure.step
    @allure.description('Click on sign up link text')
    def click_on_signup_link(self):
        self.driver.find_element(By.ID, self.signup_link_locator_id).click()


    @allure.step
    @allure.description('Clear and send keys to username field')
    def setUsername(self, username):
        self.driver.find_element(By.ID, self.signup_username_field_locator_id).clear()
        self.driver.find_element(By.ID, self.signup_username_field_locator_id ).send_keys(username)


    @allure.step
    @allure.description('Clear and send keys to password field')
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.signup_password_field_locator_id).clear()
        self.driver.find_element(By.ID, self.signup_password_field_locator_id ).send_keys(password)


    @allure.step
    @allure.description('Click on sign up button')
    def click_on_signup_button(self):
        self.driver.find_element(By.XPATH, self.signup_button_locator_xpath).click()


    @allure.step
    @allure.description('Click on close button')
    def click_on_close_button(self):
        self.driver.find_element(By.XPATH, self.signup_close_button_locator_xpath).click()

    @allure.step
    @allure.description('Click ok/ accept popup alert message')
    def alert_popup_accepter(self):
        self.driver.switch_to.alert.accept()

    @property
    @allure.step
    @allure.description('Extracting message from popup alert window')
    def alert_popup_text(self):
        return self.driver.switch_to.alert.text