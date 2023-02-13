from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.aboutUs_locators import AboutUsLocators
import allure
class AboutUs(AboutUsLocators):

    def __init__(self, driver):
        self.driver = driver
        self.baseURL = AboutUsLocators.baseURL
        self.aboutUs_link_locator_linkText = AboutUsLocators.aboutUs_link_locator_linkText
        self.aboutUs_playVideo_button_locator_xpath = AboutUsLocators.aboutUs_playVideo_button_locator_xpath
        self.about_close_button_locator_xpath = AboutUsLocators.about_close_button_locator_xpath
        self.about_us_heading_locator_id = AboutUsLocators.about_us_heading_locator_id


    @allure.step
    @allure.description('Navigate to demobilaz page')
    def open_demoblaz(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    @allure.step
    @allure.description('Click on about us text link')
    def click_on_aboutUs_link(self):
        self.driver.find_element(By.LINK_TEXT, self.aboutUs_link_locator_linkText).click()


    @property
    @allure.step
    @allure.description('Verifiying the heading text of about us page ')
    def textGetter(self):
        return self.driver.find_element(By.ID, self.about_us_heading_locator_id).text

    @allure.step
    @allure.description('Click on video play button')
    def click_on_play_button(self):
        self.driver.find_element(By.XPATH, self.aboutUs_playVideo_button_locator_xpath).click()

    @allure.step
    @allure.description('Click close button')
    def click_on_close_button(self):
        self.driver.find_element(By.XPATH, self.about_close_button_locator_xpath).click()