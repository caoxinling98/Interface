import json
from common.logger import Logger

class Assertions:
    def __init__(self):
        self.logger = Logger(logger="Assertions").getlog()

    def assert_code(self,code,expect_code):
        """
        验证响应码
        :param code:响应码
        :param expect_code: 预期响应码
        :return:
        """
        try:
            assert code == expect_code
            return True
        except:
            self.logger.error("status_code error! expect_code:%s,but code:%s"%(expect_code,code))
            raise

    def assert_msg(self,body,msg,expect_msg):
        """
        验证响应实体内容
        :param body:响应实体
        :param msg: 实体内容
        :param expect_msg: 预期实体内容
        :return:
        """
        try:
            assert body[msg] == expect_msg
            return True
        except:
            self.logger.error("msg error! expect_msg:%s,but msg:%s"%(expect_msg,msg))
            raise

    def assert_in_text(self,body,expect_msg):
        """
        验证响应实体中是否包含某个预期的字符串
        :param body: 实体内容
        :param expect_msg: 预期字符串
        :return:
        """
        try:
            text = json.loads(body)
            assert expect_msg in text
            return True
        except:
            self.logger.error("expect_msg is not included! ")
            raise

    def assert_time(self,time,expect_time):
        """
        验证响应时间是否超过预期时间，单位：ms
        :param time:
        :param expect_time:
        :return:
        """
        try:
            assert time < expect_time
            return True
        except:
            self.logger.error("response_time > expect_time,reponse_time:%s"%time)
            raise