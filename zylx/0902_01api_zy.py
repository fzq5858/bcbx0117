from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://mail.163.com')
driver.maximize_window()
time.sleep(2)

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

'''截图'''
# driver.get_screenshot_as_file("D:/.png")     #路径.png
# driver.quit()

'''切入iframe下的html'''

#第一种方式
#driver.switch_to.frame('x-URS-iframe')   #id或name的属性值不能为空，不能变化

#第二种方式
dd=driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
driver.switch_to.frame(dd)

emailname=driver.find_element_by_name('email')
emailname.send_keys('testiframe')
driver.find_element_by_name('password').send_keys('123456')

## 切回
driver.switch_to.parent_frame()       #从子frame切回到父frame
driver.switch_to.default_content()    #切回主文档



