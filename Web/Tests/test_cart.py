import pytest
# from Web.Page import Cart
from Web.Page.cartPage import Cart
import time
import allure


class Test_Cart:


    @allure.description('Test_if_it_is_possible_to_add_product_to_cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_if_it_is_possible_to_add_product_to_cart(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_sample_product_1()
        time.sleep(3)
        cr.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = cr.alert_popup_text
        print(success_message)
        cr.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message

    @allure.description('Test_the_existance_of_added_product_within_the_cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_the_existance_of_added_product_within_the_cart(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_sample_product_1()
        time.sleep(3)
        cr.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = cr.alert_popup_text
        print(success_message)
        cr.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message
        time.sleep(3)
        cr.click_on_cart_link()
        time.sleep(8)
        product_name = cr.textGetter
        print(product_name)
        assert product_name == "Samsung galaxy s6"
        product_price = cr.priceGetter
        print(product_price)
        assert cr.priceGetter == "360"


    @allure.description('Test_the_removal_of_added_product_from_cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_the_removal_of_added_product_from_cart(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_sample_product_1()
        time.sleep(3)
        cr.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = cr.alert_popup_text
        print(success_message)
        cr.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message
        time.sleep(3)
        cr.click_on_cart_link()
        time.sleep(8)
        product_name = cr.textGetter
        print(product_name)
        assert product_name == "Samsung galaxy s6"
        product_price = cr.priceGetter
        print(product_price)
        assert cr.priceGetter == "360"
        cr.click_on_delete_link()
        total_price = cr.TotalpriceGetter
        assert total_price == "0"
        time.sleep(3)

    @allure.description('Test_checkout_process_by_filling_all_fields')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_checkout_process_by_filling_all_fields(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_sample_product_1()
        time.sleep(3)
        cr.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = cr.alert_popup_text
        print(success_message)
        cr.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message
        time.sleep(3)
        cr.click_on_cart_link()
        time.sleep(8)
        product_name = cr.textGetter
        print(product_name)
        assert product_name == "Samsung galaxy s6"
        product_price = cr.priceGetter
        print(product_price)
        assert cr.priceGetter == "360"
        cr.click_on_place_order()
        time.sleep(3)
        cr.setup_name('Getachew')
        cr.setup_country("Israel")
        cr.setup_city("Beersheva")
        cr.setup_creditCard('1435 4356 0987')
        cr.setup_month('Sep')
        cr.setup_year('2022')
        cr.click_on_purchase_button()
        time.sleep(3)
        confirmation_message = cr.confirmationMessageGetter
        assert confirmation_message == "Thank you for your purchase!"

    @allure.description('Test_checkout_process_by_not_filling_all_fields')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_checkoout_process_by_not_filling_all_fields(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_sample_product_1()
        time.sleep(3)
        cr.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = cr.alert_popup_text
        print(success_message)
        cr.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message
        time.sleep(3)
        cr.click_on_cart_link()
        time.sleep(8)
        product_name = cr.textGetter
        print(product_name)
        assert product_name == "Samsung galaxy s6"
        product_price = cr.priceGetter
        print(product_price)
        assert cr.priceGetter == "360"
        cr.click_on_place_order()
        time.sleep(3)
        cr.click_on_purchase_button()
        error_message = cr.alert_popup_text
        print(error_message)
        assert "Please fill out Name and Creditcard." == error_message
        cr.alert_popup_accepter()

    @allure.description('Test_checkout_process_by_filling_invalid_credit_card')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_checkout_process_by_filling_invalid_credit_card(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_sample_product_1()
        time.sleep(3)
        cr.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = cr.alert_popup_text
        print(success_message)
        cr.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message
        time.sleep(3)
        cr.click_on_cart_link()
        time.sleep(8)
        product_name = cr.textGetter
        print(product_name)
        assert product_name == "Samsung galaxy s6"
        product_price = cr.priceGetter
        print(product_price)
        assert cr.priceGetter == "360"
        cr.click_on_place_order()
        time.sleep(3)
        cr.setup_name('Getachew')
        cr.setup_country("Israel")
        cr.setup_city("Beersheva")
        cr.setup_creditCard('1435 udw')
        cr.setup_month('Sep')
        cr.setup_year('2022')
        cr.click_on_purchase_button()
        time.sleep(3)
        message = cr.confirmationMessageGetter
        assert message == "Invalid credit card!"

    @allure.description('Test_checkout_process_by_filling_null_credit_card')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_checkout_process_by_filling_null_credit_card(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_sample_product_1()
        time.sleep(3)
        cr.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = cr.alert_popup_text
        print(success_message)
        cr.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message
        time.sleep(3)
        cr.click_on_cart_link()
        time.sleep(8)
        product_name = cr.textGetter
        print(product_name)
        assert product_name == "Samsung galaxy s6"
        product_price = cr.priceGetter
        print(product_price)
        assert cr.priceGetter == "360"
        cr.click_on_place_order()
        time.sleep(3)
        cr.setup_name('Getachew')
        cr.setup_country("Israel")
        cr.setup_city("Beersheva")
        cr.setup_creditCard('')
        cr.setup_month('Sep')
        cr.setup_year('2022')
        cr.click_on_purchase_button()
        time.sleep(3)
        error_message = cr.alert_popup_text
        print(error_message)
        assert "Please fill out Name and Creditcard." == error_message
        cr.alert_popup_accepter()

    @allure.description('Test_checkout_process_by_filling_null_name')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_checkout_process_by_filling_null_name(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_sample_product_1()
        time.sleep(3)
        cr.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = cr.alert_popup_text
        print(success_message)
        cr.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message
        time.sleep(3)
        cr.click_on_cart_link()
        time.sleep(8)
        product_name = cr.textGetter
        print(product_name)
        assert product_name == "Samsung galaxy s6"
        product_price = cr.priceGetter
        print(product_price)
        assert cr.priceGetter == "360"
        cr.click_on_place_order()
        time.sleep(3)
        cr.setup_name('')
        cr.setup_country("Israel")
        cr.setup_city("Beersheva")
        cr.setup_creditCard('2345 9086 0924 7123')
        cr.setup_month('Sep')
        cr.setup_year('2022')
        cr.click_on_purchase_button()
        time.sleep(3)
        error_message = cr.alert_popup_text
        print(error_message)
        assert "Please fill out Name and Creditcard." == error_message
        cr.alert_popup_accepter()

    @allure.description('Test_checkout_process_by_filling_null_country_city_month_year')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_checkout_process_by_filling_null_country_city_month_year(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_sample_product_1()
        time.sleep(3)
        cr.click_on_add_to_cart_button()
        time.sleep(3)
        success_message = cr.alert_popup_text
        print(success_message)
        cr.alert_popup_accepter()
        time.sleep(3)
        assert "Product added" == success_message
        time.sleep(3)
        cr.click_on_cart_link()
        time.sleep(8)
        product_name = cr.textGetter
        print(product_name)
        assert product_name == "Samsung galaxy s6"
        product_price = cr.priceGetter
        print(product_price)
        assert cr.priceGetter == "360"
        cr.click_on_place_order()
        time.sleep(3)
        cr.setup_name('Getachew')
        cr.setup_country("")
        cr.setup_city("")
        cr.setup_creditCard('1435 6782 7822 2290')
        cr.setup_month('')
        cr.setup_year('')
        cr.click_on_purchase_button()
        time.sleep(3)
        message = cr.confirmationMessageGetter
        print(message)
        assert message == "Invalid credentials!"

    @allure.description('Test_close_button_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_close_button_functionality(self):
        cr = Cart(self)
        cr.open_demoblaz()
        time.sleep(3)
        cr.click_on_cart_link()
        time.sleep(3)
        cr.click_on_place_order()
        time.sleep(3)
        cr.click_on_close_button()
        time.sleep(3)


