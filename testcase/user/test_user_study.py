from common.logger import Logger
from conftest import http
import pytest,allure,json,time
logger = Logger(logger="Test_user_study").getlog()
@allure.feature("课程学习")
class Test_user_study():
    @allure.story("获取学习动态")
    def test_get_trends(self):
        path = "/api/courses/v3/trends"
        r = http.Get(path)
        assert r["ok"] == True
        logger.info("获取学习动态" + str(r))

    @allure.story("获取课程列表")
    def test_get_myCourses(self):
        path = "/api/courses/v3/myCourses"
        r = http.Get(path)

        logger.info("获取课程列表" + str(r))

    @allure.story("获取最近学习小节")
    def test_get_recentLesson(self):
        path = "/api/learning/v3/126/recentLesson"
        r = http.Get(path)
        assert r["ok"] == True
        logger.info("获取最近学习小节" + str(r))

    @allure.story("获取课程角色")
    def test_get_courseRole(self):
        path = "/api/courses/v3/126/courseRole/"
        r = http.Get(path)
        assert r["ok"] == True
        logger.info("获取课程角色" + str(r))

    @allure.story("获取课程详情")
    def test_get_recentLesson(self):
        path = "/api/courses/v3/126/detail"
        r = http.Get(path)
        assert r["ok"] == True
        logger.info("获取课程详情" + str(r))

    @allure.story("获取菜单")
    def test_get_modules(self):
        path = "/api/courses/v3/126/modules/"
        r = http.Get(path)
        assert r["ok"] == True
        logger.info("获取菜单" + str(r))

    @allure.story("获取课程大纲")
    def test_get_chapters(self):
        path = "/api/courses/v3/126/chapters"
        r = http.Get(path)
        assert r["ok"] == True
        logger.info("获取课程大纲" + str(r))

    @allure.story("获取课程章节")
    def test_get_chapterDetail(self):
        path = "/api/courses/v3/126/chapterDetail"
        r = http.Get(path)
        assert r["ok"] == True
        logger.info("获取课程章节" + str(r))

    @allure.story("获取小节详情")
    def test_get_xiaojieDetail(self):
        path = "/api/learning/v3/126/lesson/dao-xue"
        r = http.Get(path)
        assert r["ok"] == True
        logger.info("获取小节详情" + str(r))

    @allure.story("记录时间")
    def test_get_recordStudyTime(self):
        beginat = int(round(time.time() * 1000))
        print(beginat)
        path = "/api/record/recordStudyTime/"
        payload = {"courseId":"126","lessonId":"xiao-zhu-pei-qi","duration":520,"type":"lesson","beginAt":beginat,"url":"http://acv3.learn.it101.live/learning/126/xiao-zhu-pei-qi/"}
        try:
            r = http.Post(path, payload)
            print(r)
            assert r["ok"] == True
            logger.info("成功记录时间:" + str(r))
        except Exception as e:
            print(e)
            logger.error("失败记录时间:" + str(r))

    @allure.story("运行")
    def test_run(self):
        path = '/api/learning/v3/run'
        payload = {"courseId":"181","lessonId":"tiao-yong-test-fang-fa","exerciseId":"5e4f919b8e1a9404f85e274b","language":"java","code":"public  Program {\n  public static void main(String args[ ]) {\n    obj =  A();\n     obj.;\n  }\n}\n\nclass A {\n  public void test() {\n    System.out.println(\"Hi\");\n  }  \n}\n","stdin":""}
        try:
            r = http.Post(path, payload)
            assert r["ok"] == True
            logger.info("运行成功:" + str(r))
        except Exception as e:
            print(e)
            logger.error("运行失败:" + str(r))

    @allure.story("退出登录")
    def test_logout(self):
        path = '/api/auth/logout'
        r = http.Get(path)
        assert r["ok"] == True
        logger.info("成功退出登录!"+str(r))