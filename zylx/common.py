#公共
import requests
def get_cookie():
     #登陆V部落
     url_login='http://182.92.178.83:8081/login'
     headers_login={'Content-Type':'application/x-www-form-urlencoded'}
     body_login={'username':'sang','password':'123' }
     rel_login = requests.post(url_login,headers=headers_login, data=body_login)
     #print(rel_login.json())

     #获取最新cookie
     dict_of_cookie=requests.utils.dict_from_cookiejar(rel_login.cookies)
     #{JSESSIONID':’ 274526B88D37F3AD9401A54A20BBCD3E'}
     #print(dict_of_cookie)
     new_cookie = {'Cookie':'JSESSIONID='+dict_of_cookie['JSESSIONID']}
     #print (new_cookie)
     #{’Cookie' : 'JSESSIONID=D4FC775D13731C9FFE4E08ED5CB60EF2’}
     return new_cookie
#get_cookie()

def get_all():
   url_get_all_catenames = 'http://182.92.178.83:8081/admin/category/all'
   headers_all=get_cookie()
   result_all = requests.get(url_get_all_catenames,headers=headers_all)
   #print(result_all.json())
   return result_all.json()




