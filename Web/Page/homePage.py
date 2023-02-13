import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.home_locators import HomeLocators

class Home(HomeLocators):

    def __init__(self, driver):
        self.driver = driver
        self.baseURL = HomeLocators.baseURL
        self.home_link_locator_PlinkText = HomeLocators.home_link_locator_PlinkText
        self.cart_link_locator_linkText = HomeLocators.cart_link_locator_linkText
        self.home_phone_locator_linkText = HomeLocators.home_phone_locator_linkText
        self.home_laptop_locator_linkText = HomeLocators.home_laptop_locator_linkText
        self.home_monitor_locator_linkText = HomeLocators.home_monitor_locator_linkText
        self.home_previous_button_id = HomeLocators.home_previous_button_id
        self.home_next_button_id = HomeLocators.home_next_button_id
        self.sample_product_1_link_text = HomeLocators.sample_product_1_link_text
        self.add_to_cart_button_xpath = HomeLocators.add_to_cart_button_xpath
        self.major_div_for_all_products_id = HomeLocators.major_div_for_all_products_id
        self.major_class_for_all_products_after_major_div = HomeLocators.major_class_for_all_products_after_major_div


    @allure.step
    @allure.description('Navigate to demoblaz website')
    def open_demoblaz(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    @allure.step
    @allure.description('Click on home text link')
    def click_on_home_link(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.home_link_locator_PlinkText).click()
        time.sleep(7)
        # self.driver.execute_script("window.scrollBy(0, 1000")
        self.driver.execute_script("window.scrollBy(0, 1000);")
        # time.sleep(7)

    @allure.step
    @allure.description('Click on phone text link')
    def click_on_phones_link(self):
        self.driver.find_element(By.LINK_TEXT, self.home_phone_locator_linkText).click()

    @allure.step
    @allure.description('Click on cart text link')
    def click_on_cart_link(self):
        self.driver.find_element(By.LINK_TEXT, self.cart_link_locator_linkText).click()

    @allure.step
    @allure.description('Click on laptop text link')
    def click_on_laptops_link(self):
        self.driver.find_element(By.LINK_TEXT, self.home_laptop_locator_linkText).click()

    @allure.step
    @allure.description('Click on cart monitor link')
    def click_on_monitors_link(self):
        self.driver.find_element(By.LINK_TEXT, self.home_monitor_locator_linkText).click()

    @allure.step
    @allure.description('Click on next button')
    def click_on_next_button(self):
        self.driver.find_element(By.ID, self.home_next_button_id).click()

    @allure.step
    @allure.description('Click on previous button')
    def click_on_previous_button(self):
        self.driver.find_element(By.ID, self.home_previous_button_id).click()

    @allure.step
    @allure.description('Click on samsung galaxy s6 sample product')
    def click_on_sample_product_1(self):
        self.driver.find_element(By.LINK_TEXT, self.sample_product_1_link_text).click()

    @allure.step
    @allure.description('Click on add to cart button')
    def click_on_add_to_cart_button(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath).click()

    @allure.step
    @allure.description('Find the main div element for products')
    def finding_major_div_for_products(self):
        self.driver.find_element(By.ID, self.major_div_for_all_products_id)


    @allure.step
    @allure.description('Find the main class element for products and counting the number of phones')
    def finding_major_class_after_div_phone(self):
        num_of_phones = self.driver.find_elements(By.CLASS_NAME, self.major_class_for_all_products_after_major_div)
        for i in num_of_phones:
            print(len(num_of_phones))
            assert len(num_of_phones) == 7
            break

    @allure.step
    @allure.description('Find the main class element for products and counting the number of laptops')
    def finding_major_class_after_div_laptops(self):
        num_of_laptops = self.driver.find_elements(By.CLASS_NAME, self.major_class_for_all_products_after_major_div)
        for i in num_of_laptops:
            print(len(num_of_laptops))
            assert len(num_of_laptops) == 6
            break

    @allure.step
    @allure.description('Find the main class element for products and counting the number of monitors')
    def finding_major_class_after_div_monitors(self):
        num_of_monitors = self.driver.find_elements(By.CLASS_NAME, self.major_class_for_all_products_after_major_div)
        for i in num_of_monitors:
            print(len(num_of_monitors))
            assert len(num_of_monitors) == 2
            break

    @allure.step
    @allure.description('Find the main class element for products and counting the number of items in the next page')
    def finding_major_class_after_div_second_page(self):
        num_of_monitors = self.driver.find_elements(By.CLASS_NAME, self.major_class_for_all_products_after_major_div)
        for i in num_of_monitors:
            print(len(num_of_monitors))
            assert len(num_of_monitors) == 6
            break


    def finding_major_class_after_div_first_page(self):
        num_of_monitors = self.driver.find_elements(By.CLASS_NAME, self.major_class_for_all_products_after_major_div)
        for i in num_of_monitors:
            print(len(num_of_monitors))
            assert len(num_of_monitors) == 9
            break

    def alert_popup_accepter(self):
        self.driver.switch_to.alert.accept()

    @property
    def alert_popup_text(self):
        return self.driver.switch_to.alert.text