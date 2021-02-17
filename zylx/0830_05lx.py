from selenium import webdriver
import time
driver=webdriver.Chrome()
#driver.get('http://101.133.169.100/yuns/')
driver.get('https://www.baidu.com')
time.sleep(2)

'''关于.click()'''

#没蓝   #空白区域  下拉
#driver.find_element_by_xpath('//div[@class="serv_cf"]')
# a=driver.find_element_by_xpath('//div[@class="serv_cf"]').click
# print(a)
#driver.find_element_by_xpath('//div[@class="serv_cf"]').click()                  #报错,不可点击，被拦截


#没蓝  空白区域
driver.find_element_by_css_selector('textarea[id="s_is_result_css"]').click()            #百度    报错：元素不可交互

#页面没蓝
# a=driver.find_element_by_xpath('//style[@type="text/css"]')
# print(a)
#空白区域
#driver.find_element_by_css_selector('body>div.nav_bar>div>div.allcats>div>dl:nth-child(5)>div>div:nth-child(4)').click()   #报错，元素不可交互

'''
#driver.find_element_by_css_selector('form#form span input[type="submit"]').click      #百度
#s_is_result_css不唯一
#driver.find_element_by_id('s_is_result_css')                   #百度
#driver.find_element_by_id('s_is_result_css').click                #百度
#driver.find_element_by_id('s_is_result_css').click()                  #百度   报错：元素不可交互
# tj_login不唯一
#driver.find_element_by_name('tj_login').click()                          #百度   报错：元素不可交互
'''


'''xpath相对路径 and写法'''
# //input[@type='text'and@class='but1']    或  //input[@type='text'][@class='but1']
# //div[@class="mleft menu"and@style="display:block;"]     或 //div[@class="mleft menu"][@style="display:block;"]
# //div[@class="main_bar"and@style="position: relative;"]    或  //div[@class="main_bar"][@style="position: relative;"]

#driver.find_element_by_xpath("//input[@type='text'][@class='but1']").click()
#driver.find_element_by_xpath('//div[@class="mleft menu"][@style="display:block;"]').click()
#driver.find_element_by_xpath('//div[@class="mleft menu"and@style="display:block;"]').click()