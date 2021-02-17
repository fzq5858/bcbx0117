import unittest
import requests
from zylx.common import *
import HTMLTestRunner
import os

# import time
# now=time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
import datetime



class xzs(unittest.TestCase):
    def test01(self):
        '''注册'''
        url_register='http://182.92.178.83:8088/api/student/user/register'
        headers_register={'Content-Type': 'application/json'}
        global now
        now = str(datetime.datetime.now()) + '注册'
        #print(now)
        json_register={"userName":now,"password":"123","userLevel":1}
        result_register=requests.post(url_register,headers=headers_register,json=json_register)
        #print(result_register.json())

        find_result=result_register.json()['message']
        self.assertEqual(find_result,'成功')


    def test02(self):
        '''重复注册'''
        url_register = 'http://182.92.178.83:8088/api/student/user/register'
        headers_register = {'Content-Type': 'application/json'}
        json_register = {"userName": now, "password": "123", "userLevel": 1}
        result_register = requests.post(url_register, headers=headers_register, json=json_register)
        #print(result_register.json())

        find_result = result_register.json()['message']
        self.assertEqual(find_result, '用户已存在')

    def test03(self):
        '''注册名为空'''
        url_register = 'http://182.92.178.83:8088/api/student/user/register'
        headers_register = {'Content-Type': 'application/json'}
        json_register = {"userName": "", "password": "123", "userLevel": 1}
        result_register = requests.post(url_register, headers=headers_register, json=json_register)
        #print(result_register.json())

        find_result = result_register.json()['message']
        self.assertEqual(find_result, '【userName : must not be blank】')

    def test04(self):
        '''登陆'''
        url_login = 'http://182.92.178.83:8088/api/user/login'
        headers_login = {'Content-Type': 'application/json'}
        json_login = {"userName":now,"password":"123","remember":False}
        result_login = requests.post(url_login, headers=headers_login, json=json_login)
        #print(result_login.json())

        login_cookie = requests.utils.dict_from_cookiejar(result_login.cookies)
        #print(login_cookie)
        global lgcookie
        lgcookie={'cookie':'SESSION='+login_cookie['SESSION']}

        find_result = result_login.json()['message']
        self.assertEqual(find_result, '成功')

    def test05(self):
        '''错误密码登陆'''
        url_login = 'http://182.92.178.83:8088/api/user/login'
        headers_login = {'Content-Type': 'application/json'}
        json_login = {"userName":now,"password":"123456","remember":False}
        result_login = requests.post(url_login, headers=headers_login, json=json_login)
        #print(result_login.json())

        find_result = result_login.json()['message']
        self.assertEqual(find_result, '用户名或密码错误')

    def test06(self):
        '''进入试卷中心是否正常'''
        url_sjzx = 'http://182.92.178.83:8088/api/student/education/subject/list'
        headers_sjzx = lgcookie
        result_sjzx = requests.post(url_sjzx, headers=headers_sjzx)
        #print(result_sjzx.json())

        find_result = result_sjzx.json()['message']
        self.assertEqual(find_result, '成功')

    def test07(self):
        '''进入考试记录是否正常'''
        url_ksjl = 'http://182.92.178.83:8088/api/student/exampaper/answer/pageList'
        headers_ksjl = {'Content-Type':'application/json','Cookie':lgcookie['cookie']}
        body={"pageIndex":1,"pageSize":10}
        result_ksjl = requests.post(url_ksjl, headers=headers_ksjl,json=body)
        # print(result_ksjl.json())

        find_result = result_ksjl.json()['message']
        self.assertEqual(find_result, '成功')

    def test08(self):
        '''进入个人中心是否正常'''
        url_grzx = 'http://182.92.178.83:8088/api/student/user/log'
        headers_grzx = {'Content-Type':'application/x-www-form-urlencoded','Cookie':lgcookie['cookie']}
        result_grzx = requests.post(url_grzx, headers=headers_grzx)
        # print(result_grzx.json())

        find_result = result_grzx.json()['message']
        self.assertEqual(find_result, '成功')

    def test09(self):
        '''进入消息中心是否正常'''
        url_xxzx = 'http://182.92.178.83:8088/api/student/user/message/page'
        headers_xxzx = {'Content-Type':'application/json','Cookie':lgcookie['cookie']}
        body = {"pageIndex": 1, "pageSize": 10}
        result_xxzx = requests.post(url_xxzx, headers=headers_xxzx,json=body)
        # print(result_xxzx.json())

        find_result = result_xxzx.json()['message']
        self.assertEqual(find_result, '成功')

    def test10(self):
        '''退出是否正常'''
        url_tc = 'http://182.92.178.83:8088/api/user/logout'
        headers_tc = lgcookie
        result_tc = requests.post(url_tc, headers=headers_tc)
        #print(result_tc.json())

        find_result = result_tc.json()['message']
        self.assertEqual(find_result, '成功')


if __name__ == '__main__':
    #unittest.main()

    # unitest如何执行多条用例:要用到suite套件
    #需要使用:
    # unittest.main() #使用main()直接运行时，将按case的名称顺序执行
    suite = unittest.TestSuite()
    suite.addTest(xzs('test01')) # 将需要执行的case添加到Test Suite中
    suite.addTest(xzs('test02'))
    suite.addTest(xzs('test03'))
    suite.addTest(xzs('test04'))
    suite.addTest(xzs('test05'))
    suite.addTest(xzs('test06'))
    suite.addTest(xzs('test07'))
    suite.addTest(xzs('test08'))
    suite.addTest(xzs('test09'))
    suite.addTest(xzs('test10'))
    #将根据case添加的先后顺序执行
    #如果没指定路径需要创建路径(获取报告的路径)
    path = r'E:\Pyc.path\bcbx\zylx'
    # 通过它(makedirs) 创建一个路径
    if not os.path.exists(path):
       #创建路径方法
       #print('他被删除了’)
       os.makedirs(path)
    else:
       pass
    report_path = path + "\index.html"
    report_title = u"测试报告"
    desc = u"接口自动化测试报告详情"
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=report_title, description = desc)
    runner.run(suite)



    
