import pytest
# from Web.Page import Contact
from Web.Page.contactPage import Contact
import time
import allure


class Test_Contact:


    @allure.description('Test_sending_message_with_correct_email_name_and_message')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_with_correct_email_name_and_message(self):
        cn = Contact(self)
        cn.open_demoblaz()
        time.sleep(4)
        cn.click_on_contact_link()
        time.sleep(4)
        cn.setContactEmail('getachewayehu77@gmail.com')
        time.sleep(2)
        cn.setContactName("getachew")
        time.sleep(2)
        cn.setMessage("Hi, this is Getachew ")
        time.sleep(2)
        cn.click_send_message_button()
        time.sleep(2)
        alert_message = cn.alert_popup_text
        print(alert_message)
        time.sleep(2)
        assert 'Thanks for' in alert_message
        cn.alert_popup_accepter()

    @allure.description('Test_sending_message_with_null_email_name_and_message')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_with_null_email_name_and_message(self):
        cn = Contact(self)
        cn.open_demoblaz()
        time.sleep(4)
        cn.click_on_contact_link()
        time.sleep(4)
        cn.setContactEmail('')
        time.sleep(2)
        cn.setContactName("")
        time.sleep(2)
        cn.setMessage("")
        time.sleep(2)
        cn.click_send_message_button()
        time.sleep(2)
        alert_message = cn.alert_popup_text
        print(alert_message)
        time.sleep(2)
        assert 'Please fill email and message' in alert_message
        cn.alert_popup_accepter()


    @allure.description('Test_sending_message_with_incorrect_email')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_with_incorrect_email(self):
        cn = Contact(self)
        cn.open_demoblaz()
        time.sleep(4)
        cn.click_on_contact_link()
        time.sleep(4)
        cn.setContactEmail('test123.com')
        time.sleep(2)
        cn.setContactName("tester")
        time.sleep(2)
        cn.setMessage("hi, demoblaze.com")
        time.sleep(2)
        cn.click_send_message_button()
        time.sleep(2)
        alert_message = cn.alert_popup_text
        print(alert_message)
        time.sleep(2)
        assert 'Incorrect email' in alert_message
        cn.alert_popup_accepter()

    @allure.description('Test_sending_message_with_null_email')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_with_null_email(self):
        cn = Contact(self)
        cn.open_demoblaz()
        time.sleep(4)
        cn.click_on_contact_link()
        time.sleep(4)
        cn.setContactEmail('')
        time.sleep(2)
        cn.setContactName("tester")
        time.sleep(2)
        cn.setMessage("hi, demoblaze.com")
        time.sleep(2)
        cn.click_send_message_button()
        time.sleep(2)
        alert_message = cn.alert_popup_text
        print(alert_message)
        time.sleep(2)
        assert 'Please fill email' in alert_message
        cn.alert_popup_accepter()

    @allure.description('Test_sending_message_with_null_message')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_with_null_message(self):
        cn = Contact(self)
        cn.open_demoblaz()
        time.sleep(4)
        cn.click_on_contact_link()
        time.sleep(4)
        cn.setContactEmail('getachewayehu77@gmail.com')
        time.sleep(2)
        cn.setContactName("tester")
        time.sleep(2)
        cn.setMessage("")
        time.sleep(2)
        cn.click_send_message_button()
        time.sleep(2)
        alert_message = cn.alert_popup_text
        print(alert_message)
        time.sleep(2)
        assert 'Please fill message' in alert_message
        cn.alert_popup_accepter()


    @allure.description('Test_close_button_functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_close_button_functionality(self):
        cn = Contact(driver=self)
        cn.open_demoblaz()
        time.sleep(6)
        cn.click_on_contact_link()
        time.sleep(3)
        cn.click_close_button()









