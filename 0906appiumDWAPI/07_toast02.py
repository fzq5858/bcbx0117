import os
import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from public.loginApp import Mylogin

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['app'] = PATH('E:/zhiyuan/zuiyou518.apk')
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        desired_caps['unicodeKeyboard'] ='True'
        desired_caps['resetKeyboard']= 'True'
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['newCommandTimeout'] = 200


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()
        #pass

    def test_element_by_id(self):
        time.sleep(60)
        Mylogin(self.driver).login()
        time.sleep(5)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/iconTabItem").click()
        time.sleep(6)

        #self.driver.implicitly_wait(60)
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b")
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view").click()
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys('t123')
        time.sleep(2)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        toast_loc = ("xpath", '//*[contains(@text,"评论发送成功")]')
        e1 = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        print(e1.text)
        time.sleep(2)
        self.driver.keyevent(4)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
