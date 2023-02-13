from Server.API.Constants.home_constants import *
import requests
import allure


class TestHome_API:
    @allure.description('Get products from home page')
    def test_home_page_get_products(self):
        url = HomeConstant.url
        res = requests.get(url)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5