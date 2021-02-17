import unittest
import requests
from zylx.common import *
import HTMLTestRunner
import os
import time

now=time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

class vlog(unittest.TestCase):
    # def test_get(self):
    #     url_get_all_catenames = 'http://182.92.178.83:8081/admin/category/all'
    #     headers_all=get_cookie()
    #     result_all = requests.get(url_get_all_catenames,headers=headers_all)
    #     print(result_all.json())

        # rel_get=result_all.json()[0]
        # print(rel_get,list(rel_get.keys()))
        # if 'id' in list(rel_get.keys()):
        #     rel_data=True
        #     self.assertEqual(True, rel_data)

        # rel_catename=result_all.json()[0]['cateName']
        # exp_cateName='DD'
        # self.assertEqual(rel_catename, exp_cateName)

    def test01_post(self):
        # post新增栏目
        url_post = 'http://182.92.178.83:8081/admin/category/'
        data_post = {'cateName': 'fzq新增栏目测试'+now}
        headers_post = get_cookie()
        rel_post = requests.post(url_post, headers=headers_post, data=data_post)
        print(rel_post.json())
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


    def test02_put(self):
        # 修改栏目
        url_put = ' http://182.92.178.83:8081/admin/category/'
        data_put = {'id': str(new_id), 'cateName': 'fzq修改栏目测试'+now}
        headers_put = get_cookie()
        rel_put = requests.put(url_put, headers=headers_put, data=data_put)
        print(rel_put.json())

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

    def test03_delete(self):
        # 删除栏目delete
        url_delete = 'http://182.92.178.83:8081/admin/category/%s' %new_id
        headers_delete = get_cookie()
        rel_delete = requests.delete(url_delete, headers=headers_delete)
        print(rel_delete.json())

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





if __name__ == '__main__':
    unittest.main()

    # # unitest如何执行多条用例:要用到suite套件
    # #需要使用:
    # # unittest.main() #使用main()直接运行时，将按case的名称顺序执行
    # suite = unittest.TestSuite()
    # suite.addTest(vlog('test01_post')) # 将需要执行的case添加到Test Suite中
    # suite.addTest(vlog('test02_put'))
    # suite.addTest(vlog('test03_delete'))
    # #将根据case添加的先后顺序执行
    # #如果没指定路径需要创建路径(获取报告的路径)
    # path = r'E:\Pyc.path\bcbx\zylx'
    # # 通过它(makedirs) 创建一个路径
    # if not os.path.exists(path):
    #    #创建路径方法
    #    #print('他被删除了’)
    #    os.makedirs(path)
    # else:
    #    pass
    # report_path = path + "\index.html"
    # report_title = u"测试报告"
    # desc = u"接口自动化测试报告详情"
    # fp = open(report_path, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=report_title, description = desc)
    # runner.run(suite)



    
