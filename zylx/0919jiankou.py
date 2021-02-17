#接口自动化优缺点:
#优点:
# 1.测试复用性
# 2.维护成本相对UI自动化低一些
# 3.回归方便
# 4.可以运行更多更繁琐的测试。 自动化的个明显的好处是可以在较少的时间内运行更多的测试
#缺点:
# 1.不能能完全取代手工测试
# 2.手工测试比自动测试发现的缺陷更多，自动化测试不容易发现新的BUG

# get请求和post请求的区别
# 1.get是从服务器上获取数据(例如看到列表页面等)，post是向服务器传送数据(登录、注册)什么时候用get，什么时候用post取决于开发
# 2.get请求接口的请求数据是放在url里面的，post请求接口的请求数据是放在body里面的，get请求可以在浏览器中直接访问，而post请求只能借助工具
#前后端分离
#开发模式
#以前老的方式是:
#产品经理/领导/客户提出需求
# UI做出设计图
#前端工程师做html页面
#后端工程师将html页面套成jsp页面(前后端强依赖，后端必须要等前端的html做好才能套jsp。如果html出现错误，前后端都要改

#集成出现问题
#前端返工
#后端返工
#二次集成
#集成成功
#交付
#
#新的方式是:
#产品经历/领导/客户提出需求
# UI做出设计图
#前后端约定接口&数据&参数
#前后端并行开发(无强依赖，可前后端并行开发， 如果需求变更，只要接口&参数不变，就不用两边都修改代码
#前后端集成
#前端页面调整
#集成成功
#交付

#接口自动化核心库: requests
#第一种:命令行安装: pip install requests -i https://pypi.douban.com/simple/
#第二种:在pycharm中安装->settings ->project ->选择你的PYTHON点击+输入"requests" 安装



import  requests
# url_get_toutiao='https://www.toutiao.com/2/comment/v2/reply_list/?aid=24&app_name=toutiao-web&id=6870770947247357966&offset=0&count=20&repost=0'
# rel_get_toutiao = requests.get(url=url_get_toutiao)
# #rel_get_toutiao = requests.get(url_get_toutiao)
# #rel_get_toutiao = requests.get('https://www.toutiao.com/2/comment/v2/reply_list/?aid=24&app_name=toutiao-web&id=6870770947247357966&offset=0&count=20&repost=0')
# print(rel_get_toutiao.json())

#v部落  查看所有栏位接口
# url_get_all_catenames ='http://182.92.178.83:8081/admin/category/all'
# headers_all={'Cookie': 'SESSION=ZTg0NjY3NmUtNTQxNy00MDc0LWJmNzktODc2MDNlYTBlYWZl;JSESSIONID=2548131EB1C30D01F4FCFF185DAAF852'}
# result_all = requests.get(url_get_all_catenames,headers=headers_all)
# print(result_all.json())

#文章
#http://182.92.178.83:8081/artice/all?state= 1&page= 1 &icount= 6&keywords=
#state=1代表已发表
#state=0代表草稿箱
#state=2代表回收站
#state=-1代表全部
#page代表页数
#count代表每页展示的数量
#keywords=查询的关键字(文章title )

#url_article = 'http://182.92.178.83:8081/admin/article/all?page=1&count=6&keywords=文'
###把url里的 ?page=1&count=6&keywords=文' 拆下来写params
# url_article = 'http://182.92.178.83:8081/admin/article/all'
# params_artil={'state':'1','page':'1','count':'6','keyword':'文'}
# result_arti = requests.get(url_article, headers=headers_all, params=params_artil)
# print(result_arti.json())
# print(result_arti.url)

# url_article = 'http://182.92.178.83:8081/admin/article/all'
# list=['文','发','一醉方休']
# n=1
# for key in list:
#     print('这是第%d次调用接口'%n)
#     params_artil={'state':'1','page':'1','count' :'6',' keywords': key} #把url里的 ?page=1&count=6&keywords=文' 拆下来写
#     print(params_artil)
#     try:
#         result_arti = requests.get(url_article,headers=headers_all, params=params_artil,timeout=5) #timeout超时
#         print (result_arti.json(),type(result_arti.json()))
#         print (result_arti.url)
#         print(result_arti.text,type(result_arti.text))
#         print(result_arti.encoding) #编码方式
#         print(result_arti.status_code) #响应状态码
#         print(result_arti.cookies)
#         n +=1
#     except:
#         print('查询文章接口超时了')

#登陆V部落
# import requests
# url_login='http://182.92.178.83:8081/login'
# headers_login={'Content-Type':'application/x-www-form-urlencoded'}
# body_login={'username':'sang','passworrd':'123'}
# rel_login = requests.post(url_login, headers=headers_login, data=body_login)
# print(rel_login.json())


import requests
#登陆V部落
url_login='http://182.92.178.83:8081/login'
headers_login={'Content-Type':'application/x-www-form-urlencoded'}
body_login={'username':'sang','password':'123' }
rel_login = requests.post (url_login, headers=headers_login, data=body_login)
print(rel_login.json())
#获取最新cookie
dict_of_cookie=requests.utils.dict_from_cookiejar(rel_login.cookies)
#{JSESSIONID':’ 274526B88D37F3AD9401A54A20BBCD3E'}
print(dict_of_cookie)
new_cookie = {' Cookie' :'JSESSIONID='+dict_of_cookie['JSESSIONID']}
print (new_cookie)
#{’Cookie' : 'JSESSIONID=D4FC775D13731C9FFE4E08ED5CB60EF2’}
#查看栏目
url_get_all_catenames = 'http://182.92.178.83:8081/admin/category/all'
headers_all = {}
result_all = requests.get(url_get_all_catenames, headers=headers_all)
print (result_all.json())


#v部落查看所有栏目
import requests
from zylx.common import get_cookie
new_cookie=get_cookie()
url_get_all_catenames ='http://182.92.178.83:8081/admin/category/all'
headers_all = {'Cookie':new_cookie['Cookie']}
result_all = requests.get(url_get_all_catenames, headers=headers_all)
print(result_all.json())

#post新增栏目
url_post ='http://182.92.178.83:8081/admin/category/'
data_post = {'cateName':'requests_091901'}
headers_post = {' Cookie' :new_cookie['Cookie' ], 'Content-Type' :'application/x-www-form urlencoded'}
rel_post = requests.post(url_post, headers=headers_post, data=data_post)
print(rel_post.json())

#修改栏目
url_put=' http://182.92.178.83:8081/admin/category/'
data_put={'id':'950','cateName':'requests_091902_manba888'}
headers_put= {'Cookie' :new_cookie['Cookie'],'Content-Type':'application/x-www-form-urlencoded'}
rel_put=requests.put(url_put, headers=headers_put, data =data_put)
print (rel_put.json())

#删除栏目delete
url_delete ='http://182.92.178.83:8081/admin/category/952'
headers_delete ={'Cookie' :new_cookie[' Cookie' ]}
rel_delete = requests.delete(url_delete, headers=headers_delete)
print (rel_delete.json())

#教育平台登录post
url_login_exam ='http://182.92.178.83:8088/api/user/login'
body_exam ={"userName" :" student" ," password" :" 123456" ," remember" : False}
headers_login_exam= {'Content-Type' :'application/json'}
rel_login_exam = requests.post(url_login_exam,headers=headers_login_exam, json=body_exam)
print (rel_login_exam.json())




