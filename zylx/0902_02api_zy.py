
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('https://www.ctrip.com')     #携程网
time.sleep(2)

'''下拉选择框select'''
s=driver.find_element_by_id('J_roomCountList')   #定位房间选择框
Select(s).select_by_visible_text('2间')          #通过文本select

time.sleep(3)
Select(s).select_by_index(3)                    #通过索引select，index下标从0开始数

time.sleep(3)
Select(s).select_by_value('5')                 #通过属性值select
time.sleep(3)

'''操作时间框'''
time=driver.find_element_by_id('HD_CheckIn')          #定位入住日期框
time.clear()         #清空输入框中默认时间
time.send_keys('2020-08-04')        #input标签的框 ，输入时间（注意格式要正确）

timeout=driver.find_element_by_id('HD_CheckOut')      #定位退房日期
timeout.clear()
timeout.send_keys('2020-09-09')

'''
#客户资源管理里有
#### 特殊时间控件：有readonly=“readonly” 属性，不能进行 .send_keys()
#### 需要通过 js 去掉 readonly ，然后再输入就可以了
#id
js = "document.getElementById('noticeEndTime').removeAttribute('readonly')"
#name
js = "document.getElementsByName('noticeEndTime')[0].removeAttribute('readonly')"
#tagname
js = "document.getElementsByTagName('input')[0].removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element_by_name('noticeEndTime').send_keys('2019-06-21 10:52:52')
'''