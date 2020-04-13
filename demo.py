import requests

# r = requests.get("https://www.baidu.com")
# print(r.text)

# payload = {"loginId":"caoxinling1","password":"cxl123456.","orgId":16}
# r = requests.post("http://acv3.learn.it101.live/api/auth/login",data=payload)
# print(r.json())

# token = HOrNpJMrGDKaP1pu6ntFeyXbiDDt5BBX
# token = {"ac-token":"HOrNpJMrGDKaP1pu6ntFeyXbiDDt5BBX"}
# r = requests.get("http://acv3.learn.it101.live/api/courses/v3/trends",headers = token)
# print(r.json())

#打印响应请求头函数
def printResponse(r):
    print("************************************")
    print("------------响应状态码--------------")
    print(r.status_code)
    print("------------响应头---------------")
    for k,v in r.headers.items():
        print(f"{k}:{v}")
    print("-------------响应实体---------------")
    print(r.content.decode("utf8"))

#使用session
session = requests.session()
payload = {"loginId":"caoxinling1","password":"cxl123456.","orgId":16}
r = session.post("http://acv3.learn.it101.live/api/auth/sys",data=payload)
printResponse(r=r)

r = session.get("http://acv3.learn.it101.live/api/courses/v3/trends")
printResponse(r)