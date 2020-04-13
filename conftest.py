import pytest,json
import os
from common.commonData import CommonData
from util.httpUtil import HttpUtil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR+'/report/'
LOG_DIR = BASE_DIR+'/logs/'

http = HttpUtil()
#成功登录
@pytest.fixture(scope='session',autouse=True)
def login():
    data = {"loginId": CommonData.loginId,"password": CommonData.password, "orgId": CommonData.orgId}
    path = "/api/auth/login"
    r = http.Post(path,data)
    assert r["ok"] == True




