#多窗口
from selenium import webdriver
import time

driver=webdriver.Firefox()

driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('123')
driver.find_element_by_id('su').click()
driver.maximize_window()
print(driver.window_handles)

time.sleep(3)
driver.find_element_by_partial_link_text('123网址').click()
time.sleep(3)
dd=driver.window_handles
print(driver.window_handles)
print(driver.current_window_handle)
#调回窗口
print(type(driver.window_handles[1]))
driver.switch_to.window(driver.window_handles[1])              #有些火狐版本会报错
print(driver.window_handles[1])
time.sleep(3)

driver.close()
driver.quit()