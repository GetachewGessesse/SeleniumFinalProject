import pytest
import time
from Web.Page.aboutUsPage import AboutUs
import allure


class Test_AboutUs:

    @allure.description('Test_play_video_button functionality')
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_play_video_buttonfunctionality(self):
        ab = AboutUs(self)
        ab.open_demoblaz()
        time.sleep(4)
        ab.click_on_aboutUs_link()
        time.sleep(4)
        ab.click_on_play_button()
        time.sleep(15)
        # assertion video should start

    @allure.description('Test lose_button functionality')
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_close_buttonfunctionality(self):
        ab = AboutUs(self)
        ab.open_demoblaz()
        time.sleep(4)
        ab.click_on_aboutUs_link()
        time.sleep(4)
        ab.click_on_close_button()
        time.sleep(3)
        # assertion the new window should close



