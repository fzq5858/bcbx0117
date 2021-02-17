import os
import unittest
import time
from appium import webdriver


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'True'  #安装中文输入法
        desired_caps['resetKeyboard'] = 'True'    #重置输入法
        desired_caps['automationName'] = 'Uiautomator2'   #toast

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        #self.driver.quit()
        pass

    def test_element_by_id(self):
        self.driver.implicitly_wait(60)
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title") #默认为第一个
        el.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

    '''定位'''
    def test_elements_by_id(self):
        self.driver.implicitly_wait(60)
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")  # 列表
        el[2].click()

    def test_elements_by_class_name(self):
        self.driver.implicitly_wait(60)
        el = self.driver.find_element_by_class_name("android.widget.TextView")
        time.sleep(5)
        el = self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in range(0,len(el)):
            print('第'+str(i)+'个='+el[i].text)
        el[3].click()

    def test_element_by_xpath(self):
        self.driver.implicitly_wait(60)

        #xpath通过id查找单个元素（定位关注按钮）
        el06 = self.driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/title']")
        '''class既是属性值，又是类型标签'''

        # xpath通过id查找多个元素（定位发布话题按钮）（test_elements_by_xpath不常用）
        el05 = self.driver.find_elements_by_xpath(
        "//android.widget.ImageView[@resource-id='cn.xiaochuankeji.tieba:id/iconTabItem']")
        el05[2].click()

        # xpath通过text文本定位
        el03 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='关注']")
        el03.click()

        # xpath通过text文本定位,无控件属性 //*[@]
        el04 = self.driver.find_element_by_xpath("//*[@text='图文']")
        el04.click()

        # xpath通过class查找单个元素（定位发布话题中的edittext）
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b")
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText").click() #定位标签
        #self.driver.find_element_by_xpath("//*[@class='android.widget.EditText']").click()
        #self.driver.find_element_by_xpath("//android.widget.EditText[@class='android.widget.EditText']").click()

        #组合定位（定位视频，定位搜索）
        self.driver.find_element_by_xpath(
        '//*[@resource-id="cn.xiaochuankeji.tieba:id/title" and @text="视频"]').click()

        #搜索按钮/通过层级（父级找子级）定位
        el = self.driver.find_element_by_xpath("//android.widget.FrameLayout[@resource-id='cn.xiaochuankeji.tieba:id/search_b']/android.widget.ImageView")
        el.click()

        #个人头像/层级（父级找子级定位）
        el01 = self.driver.find_element_by_xpath(
         "//android.widget.RelativeLayout[@resource-id='cn.xiaochuankeji.tieba:id/holder_flow_pmv']/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.View")
        el01.click()

        #视频/层级（父级找子级定位，有多个子级）定位
        el02 = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cn.xiaochuankeji.tieba:id/title_container']/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.TextView")
        el02.click()

        # 我的按钮/从子级定位父级
        xpath="//*[@text='我的']/../android.widget.ImageView"
        self.driver.find_element_by_xpath(xpath).click()

        #最右按钮上的文案信息/先找到父级的父级，然后找到父级的兄弟级的子级
        xpath01="//*[@text='我的']/../../android.view.View[1]/android.widget.TextView"
        print(self.driver.find_element_by_xpath(xpath01).text)

        #用视频定位消息
        self.driver.find_element_by_xpath("//android.widget.TextVuew[@resource-id='cn.xiaochuankeji.tieba:id/textTabltem']/../../android.widget.TextView[5]/android.widget.TextView")


        '''特殊API'''
        #控件点击
        self.driver.find_element_by_xpath('').click()

        #控件输入
        self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/search_input').send_keys('')
        aa=self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/search_input')
        aa.send_keys('123')
        print(aa.text)
        aa.clear()

        #获取手机屏幕分辨率
        height=self.driver.get_window_size()['height']
        width=self.driver.get_window_size()['width']
        print('此手机分辨率是：'+str(height)+'*'+str(width))

        #operateAPI
        #swipe控件点击
        el = self.driver.find_element_by_id("cn. xiaochuankeji. tieba:id/ic_ search. b")
        time.sleep(5)
        self.driver.swipe(500,1000,500,200,3000)   #现页面滑动
        self.driver.swipe(500,200,500,200,100)    #过时间控制实现点击
        self.driver.swipe(500,200,500,200,3000)

        #swipe获取手机屏幕分辨率
        height=self.driver.get_window_size()['height']
        width=self.driver.get_window_size()['width']
        self.driver.swipe(width*0.5,height*0.8,width*0.5,height*0.2,3000)

        # 控件点击
        from appium.webdriver.common.touch_action import TouchAction

        el=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b")
        TouchAction(self.driver).tap(el).perform()

        #坐标点击
        TouchAction(self.driver).tap(x=100,y=160).perform()

        #press某个点
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b")
        time.sleep(2)
        TouchAction(self.driver).press(x=500,y=308).release().perform()
        #长按某个点
        TouchAction(self.driver).long_press(x=500, y=308,duration=5000).release().perform()

        #控件长按
        el=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b")
        TouchAction(self.driver).long_press(el).perform()

        #attribute
        el = self.driver.find_element_by_id(" cn.xiaochuankeji.tieba:id/ic_search_b")
        cur_activity =self.driver.current_activity
        print(cur_activity)
        print(el.get_attribute("className")) #获取控件的属性值
        print(el.get_attribute("resourceld"))
        print(el.is_displayed()) #判断控件是否显示
        print(el.is_enabled()) #判断控件是否可用

        #toast 快速消失的弹出提示
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        toast_loc = ("xpath", './/*[contains(@text,"评论发送成功")]')
        e1 = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        print(e1.text)
        time.sleep(2)


        self.driver.keyevent(4)  #键值对/键盘














'''

zuiyou登陆密码
15127409611
a123456


["20200906150922", "test", "wodetian"]
"123testwodetian"
'''






