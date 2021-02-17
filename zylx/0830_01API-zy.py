
'''
特殊api场景处理
1.获取验证信息     driver.title               driver.current_url
2.控制浏览器       driver.refresh              driver.back        driver.forward
3.设置浏览器尺寸    driver.maxmize_window()      driver.set_window_size(1200,800)
4.动作事件         .send_keys('女装')        .clear                     .click
5.属性获取        .size    .text        .get_attribute('href')         .is_displayed()
6.鼠标事件       move_to_element()      .context_click()               .double_click()
7.键盘事件         .send_keys('女装')    .send_keys(Keys.BACK_SPACE)   .send_keys(Keys.CONTROL,'a')
8.三种等待时间     time.sleep(3)        driver.implicitly_wait(10)      WebDriverWait(driver,15,0.5)
9.多窗口切换       print(driver.window_handles)           print(driver.current_window_handle)
                 driver.switch_to.window(driver.window_handles[1])
                 driver.close()            driver.quit()
'''


#from selenium.webdriver.common.action_chains import ActionChains    #鼠标
from selenium import webdriver
import time

driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#driver.get(' https://www.baidu.com')
driver.get(' http://101.133.169.100/yuns/')

time.sleep(2)

#获取验证信息
title=driver.title
print(title)

driver.find_element_by_link_text('联系客服').click()
url=driver.current_url
print(url)

#控制浏览器
driver.find_element_by_link_text('口红').click()
driver.refresh()
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)


#设置浏览器尺寸
driver.maximize_window()
time.sleep(2)
driver.set_window_size(1200,800)
time.sleep(2)


#动作事件
driver.find_element_by_xpath('//input[@class="but1"]').clear()
driver.find_element_by_xpath('//input[@class="but1"]').send_keys('双十一')
time.sleep(2)
driver.find_element_by_xpath('//input[@class="but1"]').clear()
time.sleep(2)
driver.find_element_by_link_text('口红').click()
time.sleep(2)


#属性获取
size=driver.find_element_by_xpath('//input[@class="but1"]').size
print(type(size))
print(size)
print(size['height'])

text=driver.find_element_by_link_text('口红').text
print(text)

a=text=driver.find_element_by_link_text('口红').get_attribute('href')
print(a)
inputbutton=driver.find_element_by_css_selector('.but2').get_attribute('value')
print(inputbutton)
dis=driver.find_element_by_css_selector('.but2').is_displayed()
print(dis)

     #查看回显
if dis==True:
    driver.find_element_by_css_selector('.but1').send_keys('男装')
    text=driver.find_element_by_css_selector('.but2').get_attribute('value')
    print(text)
else:
    time.sleep(3)
    driver.find_element_by_css_selector('.but1').send_keys('男装')


#鼠标事件
from selenium.webdriver.common.action_chains import ActionChains

driver.maximize_window()
time.sleep(2)
driver.back()
time.sleep(2)
contral=driver.find_element_by_link_text('水果')

ActionChains(driver).move_to_element(contral).perform()    #移动鼠标到控件上
'''调用ActionChains类中的方法move_to_element, 其中类后面
的driver是将其传到ActionChains类的init方法中（初始化方法），
通知底层要对哪一个窗口进行操作。将母婴玩具控件定位传到方法中，就
可以将鼠标移到控件上了；在调用.perform（）方法使前面的动作生效。'''
#总结：定位要放在哪个控件上，把控件定位传到element中，（ele），driver会调用类的init，告知操作那个窗口
time.sleep(2)
driver.find_element_by_link_text('水果').click()
time.sleep(2)

driver.back()
contral=driver.find_element_by_link_text('水果')
ActionChains(driver).context_click(contral).perform()   #右击
ActionChains(driver).double_click(contral).perform()    #双击



#键盘事件
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get(' http://101.133.169.100/yuns/')
time.sleep(2)

driver.find_element_by_css_selector('.but1').send_keys('双十一活动')
driver.find_element_by_css_selector('.but1').send_keys(Keys.BACK_SPACE)
driver.find_element_by_css_selector('.but1').send_keys(Keys.SPACE)
driver.find_element_by_css_selector('.but1').send_keys(Keys.CONTROL,'a')
print('qx')
driver.find_element_by_css_selector('.but1').send_keys(Keys.CONTROL,'c')
print('fz')
driver.find_element_by_css_selector('.but1').click()     #
time.sleep(2)
driver.find_element_by_css_selector('.but1').send_keys(Keys.BACK_SPACE)
time.sleep(2)
driver.find_element_by_css_selector('.but1').send_keys(Keys.CONTROL,'v')
print("zt")
driver.find_element_by_css_selector('.but1').send_keys(Keys.CONTROL,'v')


# from time import sleep
#
# sleep(3)

#隐式等待
driver.implicitly_wait(10)
driver.find_element_by_css_selector('.but1').send_keys('双十一活动')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#显式等待时间
ele = WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='schbox']/form/input[1]")))
ele.send_keys('123456')




#多窗口切换
from selenium import webdriver
import time

driver=webdriver.Firefox()

driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('123')
driver.find_element_by_id('su').click()
driver.maximize_window()
print(driver.window_handles)   #打印当前窗口焦点

time.sleep(3)
driver.find_element_by_partial_link_text('123网址').click()
time.sleep(3)
dd=driver.window_handles
print(driver.window_handles)    #打印全部窗口焦点
print(driver.current_window_handle)     #打印当前窗口

print(type(driver.window_handles[1]))      #打印类型
driver.switch_to.window(driver.window_handles[1])       #调回窗口焦点到第二个    #有些火狐版本会报错
print(driver.window_handles[1])
time.sleep(3)

driver.close()
driver.quit()

