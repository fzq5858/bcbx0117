import unittest
from zylx.common import *
import HTMLTestRunner
import time
import os

now=time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

class vbl(unittest.TestCase):
    def test01(self):
        '''登陆V部落'''
        url_login = 'http://182.92.178.83:8081/login'
        headers_login = {'Content-Type': 'application/x-www-form-urlencoded'}
        body_login = {'username': 'sang', 'password': '123'}
        rel_login = requests.post(url_login, headers=headers_login, data=body_login)
        #print(rel_login.json())

        dict_of_cookie = requests.utils.dict_from_cookiejar(rel_login.cookies)
        global new_cookie
        new_cookie = {'Cookie': 'JSESSIONID=' + dict_of_cookie['JSESSIONID']}

        find_result=rel_login.json()['msg']
        self.assertEqual('登录成功',find_result)

    def test02(self):
        '''密码错误登陆V部落'''
        url_login = 'http://182.92.178.83:8081/login'
        headers_login = {'Content-Type': 'application/x-www-form-urlencoded'}
        body_login = {'username': 'sang', 'password': '123456'}
        rel_login = requests.post(url_login, headers=headers_login, data=body_login)
        #print(rel_login.json())

        find_result=rel_login.json()['msg']
        self.assertEqual('登录失败',find_result)

    def test03(self):
        '''密码为空登陆V部落'''
        url_login = 'http://182.92.178.83:8081/login'
        headers_login = {'Content-Type': 'application/x-www-form-urlencoded'}
        body_login = {'username': 'sang', 'password': ''}
        rel_login = requests.post(url_login, headers=headers_login, data=body_login)
        #print(rel_login.json())

        find_result=rel_login.json()['msg']
        self.assertEqual('登录失败',find_result)

    def test04(self):
        '''post新增栏目'''
        url_post = 'http://182.92.178.83:8081/admin/category/'
        data_post = {'cateName': 'fzq新增栏目测试'+now}
        headers_post = get_cookie()
        rel_post = requests.post(url_post, headers=headers_post, data=data_post)
        #print(rel_post.json())
        #基础简单断言
        rel_data=rel_post.json()['msg']
        exp_data='添加成功!'
        self.assertEqual(rel_data,exp_data)
        #2断言
        find_result = '没找到刚才新建的'
        for ele in get_all():
            if ele['cateName']=='fzq新增栏目测试'+now:
                #print(ele)
                find_result='找到了刚才新建的'
                global new_id  #全局变量 生效
                new_id=ele['id']
        self.assertEqual(find_result,'找到了刚才新建的')


    def test05(self):
        '''修改栏目'''
        url_put = ' http://182.92.178.83:8081/admin/category/'
        data_put = {'id': str(new_id), 'cateName': 'fzq修改栏目测试'+now}
        headers_put = get_cookie()
        rel_put = requests.put(url_put, headers=headers_put, data=data_put)
        #print(rel_put.json())

        rel_data = rel_put.json()['status']
        exp_data = 'success'
        self.assertEqual(rel_data, exp_data)

        find_result = '没找到修改的'
        for cate in get_all():
            if cate['id']==new_id:
                if cate['cateName']=='fzq修改栏目测试'+now:
                    find_result='找到修改的'
                    #print(cate)
        self.assertEqual(find_result, '找到修改的')

    def test06(self):
        '''删除栏目delete'''
        url_delete = 'http://182.92.178.83:8081/admin/category/%s' %new_id
        headers_delete = get_cookie()
        rel_delete = requests.delete(url_delete, headers=headers_delete)
        #print(rel_delete.json())

        rel_data = rel_delete.json()['status']
        exp_data = 'success'
        self.assertEqual(rel_data, exp_data)

        find_result = '没找到删除的'
        for cate in get_all():
            if cate['id'] == new_id:
                if cate['cateName'] == 'fzq修改栏目测试'+now:
                    find_result = '找到删除的'
                    print(cate)
        self.assertEqual(find_result, '没找到删除的')

    def test07(self):
        '''查看全部文章'''
        url_article='http://182.92.178.83:8081/admin/article/all'
        hd={'Content-Type': 'application/x-www-form-urlencoded','Cookie':get_cookie()['Cookie']}
        params_article={'page':'1','count':'6','keywords':'','state':'-1'}
        result_get=requests.get(url_article,headers=hd,params=params_article)
        #print(result_get.json())

        self.assertIn('totalCount', result_get.json())
        self.assertIn('articles', result_get.json())

    def test08(self):
        '''搜索文章'''
        url_search='http://182.92.178.83:8081/article/all?state=1&page=1&count=6&keywords=%E5%95%8A%E5%95%8A%E5%95%8A'
        headers_search={'Content-Type': 'application/x-www-form-urlencoded','Cookie':get_cookie()['Cookie']}
        result_get = requests.get(url_search, headers=headers_search)
        #print(result_get.json())

        a=result_get.json()['articles'][0]['title']
        self.assertEqual('啊啊啊',a)

    def test09(self):
        '''发表文章'''
        url_fb='http://182.92.178.83:8081/article/'
        headers_fb={'Content-Type':'application/x-www-form-urlencoded','Cookie':get_cookie()['Cookie']}
        a=now+'发表发表'
        b=now+'王子王子文章'
        body_data={'id':'-1','title':a,'mdContent':b,'htmlContent':b,'cid':'56','state':'1','dynamicTags':''}
        result_post = requests.post(url_fb,headers=headers_fb,data=body_data)
        #print(result_post.json())
        self.assertEqual('success', result_post.json()['status'])

    def test10(self):
        '''退出登陆'''
        url_logout='http://182.92.178.83:8081/logout'
        headers_logout={'Content-Type': 'application/x-www-form-urlencoded','Cookie':get_cookie()['Cookie']}
        logout_get=requests.get(url_logout,headers=headers_logout)
        #print(logout_get.json())
        self.assertEqual('尚未登录，请登录!', logout_get.json()['msg'])


if __name__=='__main__':
    #unittest.main()
    # unitest如何执行多条用例:要用到suite套件
    #需要使用:
    # unittest.main() #使用main()直接运行时，将按case的名称顺序执行
    suite = unittest.TestSuite()
    suite.addTest(vbl('test01')) # 将需要执行的case添加到Test Suite中
    suite.addTest(vbl('test02'))
    suite.addTest(vbl('test03'))
    suite.addTest(vbl('test04'))
    suite.addTest(vbl('test05'))
    suite.addTest(vbl('test06'))
    suite.addTest(vbl('test07'))
    suite.addTest(vbl('test08'))
    suite.addTest(vbl('test09'))
    suite.addTest(vbl('test10'))
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




