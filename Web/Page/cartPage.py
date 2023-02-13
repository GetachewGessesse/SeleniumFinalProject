from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.cart_locators import CartLocators
import allure

class Cart(CartLocators):

    def __init__(self, driver):
        self.driver = driver
        self.baseURL = CartLocators.baseURL
        self.cart_link_locator_linkText = CartLocators.cart_link_locator_linkText
        self.cart_delete_link_locator_linktext = CartLocators.cart_delete_link_locator_linktext
        self.cart_total_price_id = CartLocators.cart_total_price_id
        self.cart_place_order_xpath = CartLocators.cart_place_order_xpath
        self.place_order_name_field_id = CartLocators.place_order_name_field_id
        self.place_order_country_field_id = CartLocators.place_order_country_field_id
        self.place_order_city_field = CartLocators.place_order_city_field
        self.place_order_credit_card_field_id = CartLocators.place_order_credit_card_field_id
        self.place_order_month_filed_id = CartLocators.place_order_month_filed_id
        self.place_order_year_field_id = CartLocators.place_order_year_field_id
        self.place_order_purchase_button_xpath = CartLocators.place_order_purchase_button_xpath
        self.place_order_close_button_xpath = CartLocators.place_order_close_button_xpath
        self.sample_product_1_link_text = CartLocators.sample_product_1_link_text
        self.add_to_cart_button_xpath = CartLocators.add_to_cart_button_xpath
        self.sample_product_name_within_cart_xpath = CartLocators.sample_product_name_within_cart_xpath
        self.sample_product_price_within_cart_xpath = CartLocators.sample_product_price_within_cart_xpath
        self.place_order_confirmation_message_xpath = CartLocators.place_order_confirmation_message_xpath


    @allure.step
    @allure.description('Navigate to demoblaz page')
    def open_demoblaz(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(9)

    @allure.step
    @allure.description('Click on cart text link')
    def click_on_cart_link(self):
        self.driver.find_element(By.LINK_TEXT, self.cart_link_locator_linkText).click()

    @allure.step
    @allure.description('Click on delete link')
    def click_on_delete_link(self):
        self.driver.find_element(By.LINK_TEXT, self.cart_delete_link_locator_linktext).click()

    @allure.step
    @allure.description('click on place order button')
    def click_on_place_order(self):
        self.driver.find_element(By.XPATH, self.cart_place_order_xpath).click()


    @allure.step
    @allure.description('clear and send keys to name field')
    def setup_name(self, name):
        self.driver.find_element(By.ID, self.place_order_name_field_id).clear()
        self.driver.find_element(By.ID, self.place_order_name_field_id).send_keys(name)

    @allure.step
    @allure.description('clear and send keys to country field')
    def setup_country(self, country):
        self.driver.find_element(By.ID, self.place_order_country_field_id).clear()
        self.driver.find_element(By.ID, self.place_order_country_field_id).send_keys(country)

    @allure.step
    @allure.description('clear and send keys to city field')
    def setup_city(self, city):
        self.driver.find_element(By.ID, self.place_order_city_field).clear()
        self.driver.find_element(By.ID, self.place_order_city_field).send_keys(city)

    @allure.step
    @allure.description('clear and send keys to credit card field')
    def setup_creditCard(self, credit_card):
        self.driver.find_element(By.ID, self.place_order_credit_card_field_id).clear()
        self.driver.find_element(By.ID, self.place_order_credit_card_field_id).send_keys(credit_card)

    @allure.step
    @allure.description('clear and send keys to month field')
    def setup_month(self, month):
        self.driver.find_element(By.ID, self.place_order_month_filed_id).clear()
        self.driver.find_element(By.ID, self.place_order_month_filed_id).send_keys(month)

    @allure.step
    @allure.description('clear and send keys to year field')
    def setup_year(self, year):
        self.driver.find_element(By.ID, self.place_order_year_field_id).clear()
        self.driver.find_element(By.ID, self.place_order_year_field_id).send_keys(year)

    @allure.step
    @allure.description('click on purchase button')
    def click_on_purchase_button(self):
        self.driver.find_element(By.XPATH, self.place_order_purchase_button_xpath).click()

    @allure.step
    @allure.description('click on close button')
    def click_on_close_button(self):
        self.driver.find_element(By.XPATH, self.place_order_close_button_xpath).click()

    @allure.step
    @allure.description('click on samsung galaxy 6 sample product')
    def click_on_sample_product_1(self):
        self.driver.find_element(By.LINK_TEXT, self.sample_product_1_link_text).click()

    @allure.step
    @allure.description('click on add to cart button')
    def click_on_add_to_cart_button(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath).click()

    @allure.step
    @allure.description('click ok/ accept the alert popup')
    def alert_popup_accepter(self):
        self.driver.switch_to.alert.accept()

    @property
    @allure.step
    @allure.description('extract the message on alert popup window')
    def alert_popup_text(self):
        return self.driver.switch_to.alert.text


    @property
    @allure.step
    @allure.description('verify the name of sample product that was added to cart')
    def textGetter(self):
        return self.driver.find_element(By.XPATH, self.sample_product_name_within_cart_xpath).text

    @property
    @allure.step
    @allure.description('verify the price of sample product that was added to cart')
    def priceGetter(self):
        return self.driver.find_element(By.XPATH, self.sample_product_price_within_cart_xpath).text

    @property
    @allure.step
    @allure.description('verify the total price of products on the cart')
    def TotalpriceGetter(self):
        return self.driver.find_element(By.ID, self.cart_total_price_id).text

    @property
    @allure.step
    @allure.description('confirm the checkout message ')
    def confirmationMessageGetter(self):
        return self.driver.find_element(By.XPATH, self.place_order_confirmation_message_xpath).text


