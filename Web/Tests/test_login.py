import pytest
# from Web.Page import Login
from Web.Page.loginPage import Login
import time
import allure

class Test_Login:

    @allure.description('Test_login_with_valid_credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_login_with_valid_credentials(self):
        lg = Login(self)
        lg.open_demoblaz()
        time.sleep(6)
        lg.click_on_login_link()
        time.sleep(6)
        lg.setUsername("azuta")
        time.sleep(2)
        lg.setPassword("azuta1234")
        time.sleep(2)
        lg.click_on_login_button()
        time.sleep(10)
        messageDisplayed = lg.welcome_text_getter
        print(messageDisplayed)
        if "Welcome" in messageDisplayed:
            assert True
        else:
            assert False


    @allure.description('Test_login_with_both_invalid_credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_login_with_both_invalid_credentials(self):
        lg = Login(self)
        lg.open_demoblaz()
        time.sleep(6)
        lg.click_on_login_link()
        time.sleep(6)
        lg.setUsername("azutacbsch")
        time.sleep(2)
        lg.setPassword("azuta1svbsfs234")
        time.sleep(2)
        lg.click_on_login_button()
        time.sleep(10)
        lg.alert_popup_accepter()
        # assertion: user does not exist

    @allure.description('Test_login_with__valid_username_invalid_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_login_with__valid_username_invalid_password(self):
        lg = Login(self)
        lg.open_demoblaz()
        time.sleep(6)
        lg.click_on_login_link()
        time.sleep(6)
        lg.setUsername("azuta")
        time.sleep(2)
        lg.setPassword("azuta1svbsfs234")
        time.sleep(2)
        lg.click_on_login_button()
        time.sleep(10)
        error = lg.alert_popup_text
        assert "Wrong password." == error
        lg.alert_popup_accepter()
        # assertion: invalid password

    @allure.description('Test_login_with_invalid_username_valid_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_login_with_invalid_username_valid_password(self):
        lg = Login(self)
        lg.open_demoblaz()
        time.sleep(6)
        lg.click_on_login_link()
        time.sleep(6)
        lg.setUsername("azutahvfyfrt")
        time.sleep(2)
        lg.setPassword("azuta1234")
        time.sleep(2)
        lg.click_on_login_button()
        time.sleep(10)
        error = lg.alert_popup_text
        print(error)
        assert "User does not exist." == error
        lg.alert_popup_accepter()



    @allure.description('Test_login_with_both_null_username_and_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_login_with_both_null_username_and_password(self):
        lg = Login(self)
        lg.open_demoblaz()
        time.sleep(6)
        lg.click_on_login_link()
        time.sleep(6)
        lg.setUsername("")
        time.sleep(2)
        lg.setPassword("")
        time.sleep(2)
        lg.click_on_login_button()
        time.sleep(10)
        error = lg.alert_popup_text
        print(error)
        assert "Please fill out Username and Password." == error
        lg.alert_popup_accepter()
        # assertion: please fill out username and password

    @allure.description('Test_login_with__null_username_and_valid_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_login_with__null_username_and_valid_password(self):
        lg = Login(self)
        lg.open_demoblaz()
        time.sleep(6)
        lg.click_on_login_link()
        time.sleep(6)
        lg.setUsername("")
        time.sleep(2)
        lg.setPassword("azuta1234")
        time.sleep(2)
        lg.click_on_login_button()
        time.sleep(10)
        error = lg.alert_popup_text
        print(error)
        assert "Please fill out Username and Password." == error
        lg.alert_popup_accepter()
        # assertion: please fill out username and password


    @allure.description('Test_login_with_valid_username_and_null_password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_login_with_valid_username_and_null_password(self):
        lg = Login(self)
        lg.open_demoblaz()
        time.sleep(6)
        lg.click_on_login_link()
        time.sleep(6)
        lg.setUsername("azuta")
        time.sleep(2)
        lg.setPassword("")
        time.sleep(2)
        lg.click_on_login_button()
        time.sleep(10)
        error = lg.alert_popup_text
        print(error)
        assert "Please fill out Username and Password." == error
        lg.alert_popup_accepter()
        # assertion: please fill out username and password


    @allure.description('test_close_button_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_close_button_functionality(self):
        lg = Login(driver=self)
        lg.open_demoblaz()
        time.sleep(6)
        lg.click_on_login_link()
        time.sleep(3)
        lg.click_on_close_button()


    @allure.description('test_logout_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_logout_functionality(self):
        lg = Login(self)
        lg.open_demoblaz()
        time.sleep(6)
        lg.click_on_login_link()
        time.sleep(6)
        lg.setUsername("azuta")
        time.sleep(2)
        lg.setPassword("azuta1234")
        time.sleep(2)
        lg.click_on_login_button()
        time.sleep(5)
        lg.click_logout_link()
        time.sleep(2)
        assert "Log in" == lg.login_text_getter
















