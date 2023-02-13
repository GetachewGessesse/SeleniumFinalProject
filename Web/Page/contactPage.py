from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.contact_locators import ContactUsLocators
import allure

class Contact(ContactUsLocators):

    def __init__(self, driver):
        self.driver = driver
        self.baseURL  = ContactUsLocators.baseURL
        self.contact_link_locator_linkText = ContactUsLocators.contact_link_locator_linkText
        self.contact_email_field_locator_id = ContactUsLocators.contact_email_field_locator_id
        self.contact_name_field_locator_id = ContactUsLocators.contact_name_field_locator_id
        self.contact_message_field_locator_id = ContactUsLocators.contact_message_field_locator_id
        self. contact_send_message_button_locator_xpath = ContactUsLocators.contact_send_message_button_locator_xpath
        self.contact_close_button_locator_xpath = ContactUsLocators.contact_close_button_locator_xpath

    @allure.step
    @allure.description('Navigate to demobilaz page')
    def open_demoblaz(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


    @allure.step
    @allure.description('Click on contact link text')
    def click_on_contact_link(self):
        self.driver.find_element(By.LINK_TEXT, self.contact_link_locator_linkText).click()

    @allure.step
    @allure.description('Clear and send keys to email field')
    def setContactEmail(self, email):
        self.driver.find_element(By.ID, self.contact_email_field_locator_id).clear()
        self.driver.find_element(By.ID, self.contact_email_field_locator_id).send_keys(email)


    @allure.step
    @allure.description('Clear and send keys to name field')
    def setContactName(self, name):
        self.driver.find_element(By.ID, self.contact_name_field_locator_id).clear()
        self.driver.find_element(By.ID, self.contact_name_field_locator_id).send_keys(name)


    @allure.step
    @allure.description('Clear and send keys to message field')
    def setMessage(self, message):
        self.driver.find_element(By.ID, self.contact_message_field_locator_id).clear()
        self.driver.find_element(By.ID, self.contact_message_field_locator_id).send_keys(message)


    @allure.step
    @allure.description('Click on send message button')
    def click_send_message_button(self):
        self.driver.find_element(By.XPATH, self.contact_send_message_button_locator_xpath).click()

    @allure.step
    @allure.description('Click on close button')
    def click_close_button(self):
        self.driver.find_element(By.XPATH, self.contact_close_button_locator_xpath).click()

    @allure.step
    @allure.description('Click ok/ accept popup alert message')
    def alert_popup_accepter(self):
        self.driver.switch_to.alert.accept()

    @property
    @allure.step
    @allure.description('Extracting message from popup alert window')
    def alert_popup_text(self):
        return self.driver.switch_to.alert.text

