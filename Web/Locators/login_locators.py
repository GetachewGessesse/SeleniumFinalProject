
class LoginLocators:
    baseURL = "https://www.demoblaze.com/index.html"
    login_link_locator_linkText = "Log in"
    login_username_field_locator_id = "loginusername"
    login_password_field_locator_id = "loginpassword"
    login_button_locator_xpath = "//button[contains(text(),'Log in')]"
    login_close_button_locator_xpath = "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[1]"
    logout_link_locator_id = "logout2"
    welcome_txt_locator_id = "nameofuser"