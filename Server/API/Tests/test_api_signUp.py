from Server.API.Constants.signUp_constants import *
import requests
import allure


class TestLogin_API:
    @allure.description('Sign up correctly')
    def test_login_correctly(self):
        url = SignUpConstants.url
        data = SignUpConstants.valid_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5


    @allure.description('Login incorrectly with both invalid credintials')
    def test_login_incorrectly_with_both_invalid_credintials(self):
        url = SignUpConstants.url
        data = SignUpConstants.invalid_both_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('Login incorrectly with invalid username')
    def test_login_incorrectly_with_invalid_username(self):
        url = SignUpConstants.url
        data = SignUpConstants.invalid_data_username
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('Login incorrectly with invalid password')
    def test_login_incorrectly_incorrectly_with_invalid_password(self):
        url = SignUpConstants.url
        data = SignUpConstants.invalid_data_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('Login incorrectly with existing username and password')
    def test_login_incorrectlyexisting_username_and_password(self):
        url = SignUpConstants.url
        data = SignUpConstants.invalid_existing_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5