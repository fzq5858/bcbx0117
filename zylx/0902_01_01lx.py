from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
time.sleep(2)
a=driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(a).perform()    #移动鼠标到控件上
driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()
time.sleep(5)
driver.switch_to.alert.accept()         #确认
time.sleep(5)
driver.close()
driver.quit()


'''alert弹出框，右击点不动，不会出现查看元素'''
# print(driver.window_handles)
# driver.switch_to.alert.send_keys('45351')   #输入
# time.sleep(3)
# print(driver.switch_to.alter.text)
# driver.switch_to.alert.accept()             #确定/保存（所有的正向按钮）
# print(driver.switch_to.alert.text)          #获取文本信息
# time.sleep(4)
#
# driver.switch_to.alear.dismiss()            #取消/不保存
# driver.close()
# driver.quit()