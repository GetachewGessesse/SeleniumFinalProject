import pytest
import allure
from Web.Page.homePage import Home
import time


class Test_Home:

    @allure.description('Test_phone_link_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_phone_link_functionality(self):
        hm = Home(self)
        hm.open_demoblaz()
        hm.click_on_phones_link()
        time.sleep(4)
        hm.finding_major_div_for_products()
        time.sleep(4)
        # The assertion is within the page in finding_major_class_after_div_phone class methode
        phones = hm.finding_major_class_after_div_phone()

    @allure.description('Test_laptop_link_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_laptop_link_functionality(self):
        hm = Home(self)
        hm.open_demoblaz()
        hm.click_on_laptops_link()
        time.sleep(4)
        hm.finding_major_div_for_products()
        time.sleep(4)
        # The assertion is within the page in finding_major_class_after_div_laptops class methode
        phones = hm.finding_major_class_after_div_laptops()


    @allure.description('Test_monitors_link_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_monitors_link_functionality(self):
        hm = Home(self)
        hm.open_demoblaz()
        hm.click_on_monitors_link()
        time.sleep(4)
        hm.finding_major_div_for_products()
        time.sleep(4)
        # The assertion is within the page in finding_major_class_after_div_monitors class methode
        phones = hm.finding_major_class_after_div_monitors()


    @allure.description('Test_next_button_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_next_button_functionality(self):
        hm = Home(self)
        hm.open_demoblaz()
        time.sleep(6)
        hm.click_on_home_link()
        time.sleep(3)
        hm.click_on_next_button()
        time.sleep(3)
        hm.finding_major_div_for_products()
        time.sleep(3)
        # The assertion is within the page in finding_major_class_after_div_second_page class methode
        hm.finding_major_class_after_div_second_page()


    @allure.description('Test_previous_button_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_previous_button_functionality(self):
        hm = Home(self)
        hm.open_demoblaz()
        time.sleep(6)
        hm.click_on_home_link()
        time.sleep(3)
        hm.click_on_next_button()
        time.sleep(3)
        hm.click_on_previous_button()
        time.sleep(3)
        hm.finding_major_div_for_products()
        time.sleep(3)
        # The assertion is within the page in finding_major_class_after_div_first_page class methode
        hm.finding_major_class_after_div_first_page()


    @allure.description('Test_home_link_functionality_from_cart_page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_home_link_functionality_from_cart_page(self):
        hm = Home(self)
        hm.open_demoblaz()
        time.sleep(3)
        hm.click_on_cart_link()
        time.sleep(6)
        hm.click_on_home_link()
        time.sleep(3)
        hm.finding_major_div_for_products()
        time.sleep(3)
        # The assertion is within the page in finding_major_class_after_div_first_page class methode
        hm.finding_major_class_after_div_first_page()


    @allure.description('Test_add_a_product_from_home_page_to_cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_add_a_product_from_home_page_to_cart(self):
        hm = Home(self)
        hm.open_demoblaz()
        time.sleep(3)
        hm.click_on_sample_product_1()
        time.sleep(3)
        hm.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = hm.alert_popup_text
        print(success_message)
        hm.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message









