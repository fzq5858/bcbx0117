from appium import webdriver
import time
import unittest
import os
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
desired_caps['appActivity'] = '.ui.base.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(40)
try:
 driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvConfirmWithBg").click()  #点击我知道了（青少年模式）
 time.sleep(5)
except:
 pass
driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/iconTabItem")[1].click()   #点击动态
