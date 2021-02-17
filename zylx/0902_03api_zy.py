from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('https://qiye.163.com')  #网易企业邮箱
time.sleep(2)
driver.set_window_size(800,800)
driver.implicitly_wait(5)

'''滚动条'''
js="var q=document.documentElement.scrollTop=0"         #移动到页面顶部
js="var q=document.documentElement.scrollTop=10000"     #移动到页面底部，设置一个很大的值
driver.execute_script(js)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5)")    #高度50%
time.sleep(3)
driver.execute_script("window.scrollBy(0,-200)");             #相对当前坐标移动
time.sleep(3)
driver.execute_script("window.scrollTo(0, 1500)")            #移动到绝对坐标
print(driver.find_element_by_css_selector('.copyright').text)