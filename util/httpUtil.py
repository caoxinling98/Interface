import requests
from common.commonData import CommonData
import json
import pytest

class HttpUtil():
    def __init__(self):
        self.session = requests.session()
        # self.header = {"Accept":"application/json, text/plain, */","Content-Type":"application/json;charset=UTF-8"}
    # def printResponse(self,response):
    #     self.response = response
    #     print("*********begin**********")
    #     print(self.response.status_code)
    #     for k,v in self.response.headers.items():
    #         print(f"{k}:{v}")
    #     print(self.response.content.decode('utf8'))
    #     print("*********end************")

    def Post(self,path,data):
        host = CommonData.host
        r = self.session.post(url=host+path,data=data)
        r_json = r.content.decode('utf8')
        r_dict = json.loads(r_json)
        return r_dict


    def Get(self,path):
        host = CommonData.host
        r = self.session.get(url=host+path)
        r_json = r.content.decode('utf8')
        r_dict = json.loads(r_json)
        return r_dict
