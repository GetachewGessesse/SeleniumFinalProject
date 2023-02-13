import pytest
# from Web.Page import Signup
from Web.Page.signUpPage import Signup
import time
import allure



class Test_signup:

    @allure.description('Test_signup_with_valid_username_and_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_signup_with_valid_username_and_password(self):
        sg = Signup(self)
        sg.open_demoblaz()
        time.sleep(4)
        sg.click_on_signup_link()
        time.sleep(2)
        sg.setUsername('s56ncf')
        time.sleep(2)
        sg.setPassword('hsm34df')
        time.sleep(2)
        sg.click_on_signup_button()
        time.sleep(4)
        message = sg.alert_popup_text
        print(message)
        assert "successful" in message
        sg.alert_popup_accepter()


    @allure.description('Test_signup_null_username_and_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_signup_null_username_and_password(self):
        sg = Signup(self)
        sg.open_demoblaz()
        time.sleep(4)
        sg.click_on_signup_link()
        time.sleep(2)
        sg.setUsername('')
        time.sleep(2)
        sg.setPassword('')
        time.sleep(2)
        sg.click_on_signup_button()
        time.sleep(4)
        message = sg.alert_popup_text
        print(message)
        assert "Please fill out" in message
        sg.alert_popup_accepter()


    @allure.description('Test_signup_existing_username_and_nonExsting_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_signup_existing_username_and_nonExsting_password(self):
        sg = Signup(self)
        sg.open_demoblaz()
        time.sleep(4)
        sg.click_on_signup_link()
        time.sleep(2)
        sg.setUsername('azuta')
        time.sleep(2)
        sg.setPassword('dncdsjhvfvj')
        time.sleep(2)
        sg.click_on_signup_button()
        time.sleep(4)
        message = sg.alert_popup_text
        print(message)
        assert "user already exist." in message
        sg.alert_popup_accepter()


    @allure.description('Test_signup_nonExisting_username_and_exsting_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_signup_nonExisting_username_and_exsting_password(self):
        sg = Signup(self)
        sg.open_demoblaz()
        time.sleep(4)
        sg.click_on_signup_link()
        time.sleep(2)
        sg.setUsername('we7338rgfhnklna')
        time.sleep(2)
        sg.setPassword('azuta1234')
        time.sleep(2)
        sg.click_on_signup_button()
        time.sleep(4)
        message = sg.alert_popup_text
        print(message)
        assert "user already exist." in message
        sg.alert_popup_accepter()


    @allure.description('Test_signup_null_username_and_valid_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_signup_null_username_and_valid_password(self):
        sg = Signup(self)
        sg.open_demoblaz()
        time.sleep(4)
        sg.click_on_signup_link()
        time.sleep(2)
        sg.setUsername('')
        time.sleep(2)
        sg.setPassword('qwert123')
        time.sleep(2)
        sg.click_on_signup_button()
        time.sleep(4)
        message = sg.alert_popup_text
        print(message)
        assert "Please fill out" in message
        sg.alert_popup_accepter()


    @allure.description('Test_signup_valid_username_and_null_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_signup_valid_username_and_null_password(self):
        sg = Signup(self)
        sg.open_demoblaz()
        time.sleep(4)
        sg.click_on_signup_link()
        time.sleep(2)
        sg.setUsername('asdfg0987')
        time.sleep(2)
        sg.setPassword('')
        time.sleep(2)
        sg.click_on_signup_button()
        time.sleep(4)
        message = sg.alert_popup_text
        print(message)
        assert "Please fill out" in message
        sg.alert_popup_accepter()


    @allure.description('Test_signup_existing_username_and__password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_signup_existing_username_and__password(self):
        sg = Signup(self)
        sg.open_demoblaz()
        time.sleep(4)
        sg.click_on_signup_link()
        time.sleep(2)
        sg.setUsername('azuta')
        time.sleep(2)
        sg.setPassword('azuta1234')
        time.sleep(2)
        sg.click_on_signup_button()
        time.sleep(4)
        message = sg.alert_popup_text
        print(message)
        assert "already exist" in message
        sg.alert_popup_accepter()

    @allure.description('Test_close_btn_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_close_btn_functionality(self):
        sg = Signup(self)
        sg.open_demoblaz()
        time.sleep(4)
        sg.click_on_signup_link()
        time.sleep(2)
        sg.click_on_close_button()



