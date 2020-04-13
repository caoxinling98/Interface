from common.logger import Logger
from conftest import http
import pytest,allure
logger = Logger(logger="Test_login").getlog()
@allure.feature("登录模块")
class Test_login():
    @allure.story("登录成功")
    def test_login_success(self):
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        data = {"loginId": "1111","password": "1111", "orgId": 00}
        path = "/api/auth/login"
        r = http.Post(path, data)
        assert r["ok"] == False
        assert r["message"] == "该学校下没有此用户"
        logger.info("登录失败:" + str(r))

