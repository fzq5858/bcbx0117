#鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver=webdriver.Firefox()

driver.get('http://101.133.169.100/yuns/')
print(driver.current_window_handle)

contral=driver.find_element_by_link_text('水果')            #
print(contral)

ActionChains(driver).move_to_element(contral).perform()    #移动鼠标到控件上
time.sleep(2)
driver.find_element_by_link_text('水果').click()
time.sleep(2)
print(driver.current_window_handle)
driver.back()
time.sleep(2)
print(driver.current_window_handle)

driver.refresh()                                       #页面刷新后，上一条命令不生效，会报错
print(driver.current_window_handle)
contral=driver.find_element_by_link_text('水果')         #
ActionChains(driver).context_click(contral).perform()   #右击
ActionChains(driver).double_click(contral).perform()    #双击