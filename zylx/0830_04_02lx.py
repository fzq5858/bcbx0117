#显式等待时间（until_not）
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time

#driver=webdriver.Firefox()
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/')
time.sleep(2)

print('云商页面',driver.window_handles)

driver.find_element_by_link_text('秒杀').click()
time.sleep(3)
print('点击秒杀后全部窗口',driver.window_handles)
print('当前窗口',driver.current_window_handle)
driver.switch_to.window(driver.window_handles[1])
print('调回后窗口',driver.current_window_handle)
#现在是秒杀窗口焦点

# 注：“水果” 控件在云商页面和秒杀页面都存在
'''   
#until_not 直到没有此控件
driver.switch_to.window(driver.window_handles[0])
print('云商窗口焦点',driver.current_window_handle)
ele = WebDriverWait(driver,15,0.5).until_not(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div[1]/div/dl[3]/dt/div/span/a")))    #水果
print('without水果控件')
#预期：失败报错    实际结果：报错
'''

#注：秒杀页面有 ‘暂时无抢购’ 控件，云商页面没有这个控件
driver.switch_to.window(driver.window_handles[0])
print('云商窗口焦点',driver.current_window_handle)
ele = WebDriverWait(driver,15,0.5).until_not(EC.presence_of_element_located((By.CSS_SELECTOR,".nomsg")))    #暂时无抢购
print('ok')