from selenium import webdriver
import time

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get(' http://101.133.169.100/yuns/')
#driver.get('https://www.baidu.com/index.php?tn=request_1_pg&ch=1')            #定位要考虑到：
time.sleep(3)                                                                   #1.路径唯一
                                                                                #2.控件在当前页面（隐藏页面、下拉滚动条）
'''八大定位方式'''                                                                 #3.iframe
#八种定位方式只能定位地址栏以下的内容,能够定位的均在body内，head内的控件无法定位。             #4.等待时间
                                                                                 #5.跳转后窗口焦点
'''一、find_element_by_id'''
#driver.find_element_by_id('cart_num').click()     #i标签，定位点击购物车
#driver.find_element_by_id('s_is_result_css')      #百度
'''二、find_element_by_name'''
#driver.find_element_by_name('key').send_keys('男士')  #定位输入框
#driver.find_element_by_name('tj_login')              #百度
'''三、find_element_by_class_name'''
#class属性值中间有空格的称为复合类，一般不要用class属性定位，但是要用的话，选择其中一个属性值就可以。（可能出现重复）
#driver.find_element_by_class_name('but2').click()     #搜索键
#driver.find_element_by_class_name('logo').click()
'''四、find_element_by_link_text'''
#by_link_text可以定位有a标签，href属性，并且属性地址是可以跳转的地址
#driver.find_element_by_link_text('秒杀').click()  #a标签，点击文本可跳转
#driver.find_element_by_link_text('口红').click()
'''五、find_element_by_partial_link_text'''
#a标签、可跳转的链接地址、文字控件
#driver.find_element_by_partial_link_text('双十一').click() #文字连续、唯一
#driver.find_element_by_partial_link_text('香').click()
'''六、find_element_by_xpath'''
   #xpath绝对路径：
#driver.find_element_by_xpath('/html/body/div/div/div/div/form/input[1]').send_keys('女士')
#driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/a[4]').click()
#driver.find_element_by_xpath('/html/body/div[3]/div/div/div/dl[3]/dt/div').click()
   #xpath相对路径：
#driver.find_element_by_xpath("//input[@type='text'and@class='but1']").send_keys('口红')    xpath的and关系
#driver.find_element_by_xpath('//*[@id="cart_num"]').click()   # *不管什么标签都可以
#driver.find_element_by_xpath('//div[@class="mleft menu"]').click()
#driver.find_element_by_xpath('//div[@class="mleft menu"and@style="display:block;"]').click()
#driver.find_element_by_xpath('//*[@class="nav_bar"]').click()
#driver.find_element_by_xpath('//div[@class="r"]').click()
#driver.find_element_by_xpath('//div[@class="r"]/..').click()
#driver.find_element_by_xpath('//span[@class="name"]').click()
#driver.find_element_by_xpath('//div[@class="footer_bar"]').click()
#driver.find_element_by_xpath('//div[@class="serv_cf"]/div[4]').click()
   #driver.find_element_by_xpath('//div[@class="serv_cf"]')
   #driver.find_element_by_xpath('//style[@type="text/css"]')
#driver.find_element_by_xpath('//div[@class="main_bar"]').click()
#driver.find_element_by_xpath('//div[@class="main_bar"and@style="position: relative;"]').click()     #@style尽量不要用
#driver.find_element_by_xpath('//div[@class="main_bar"][@style="position: relative;"]').click()   #？？？

 #xpath包含
#driver.find_element_by_xpath('//input[contains(@placeholder,"请")]').send_keys('口红')
#driver.find_element_by_xpath('//a[contains(@href,"双十一")]').click()

'''七、find_element_by_css_selector'''
#css绝对路径
#css     空格或 >  也可以混搭
#driver.find_element_by_css_selector('body>div.nav_bar>div>div.allcats').click()      #class="allcats allcats_show"  因为有空格，复合类型，所以只能取其中一个
#driver.find_element_by_css_selector('body>div.nav_bar>div>div.allcats>div>dl:nth-child(5)>div>div:nth-child(4)')

#driver.find_element_by_css_selector("html body div div div div form input[placeholder='请输入你要查找的关键字']").send_keys('口红')
#driver.find_element_by_css_selector("html>body>div>div>div>div>form>input[placeholder='请输入你要查找的关键字']").send_keys('口红')
#driver.find_element_by_css_selector("html>body>div div div div>form>input[placeholder='请输入你要查找的关键字']").send_keys('口红')
#css相对路径
#driver.find_element_by_css_selector('i#cart_num').click()   #属性为id  也可以#cart_num
#driver.find_element_by_css_selector('input.but1').send_keys('好几个')   #属性为class   也可以  .but1

#driver.find_element_by_css_selector('input[placeholder="请输入你要查找的关键字"]').send_keys('芭比')
    #注意：对于xpath，是相同类型的标签在一起排序，对于css，是将所有类型的标签放在一起排序
#driver.find_element_by_css_selector('div.schbox form input:nth-child(1)').send_keys('芭比')
#driver.find_element_by_css_selector('div[class="schbox"] form input:nth-child(1)').send_keys('芭比')
#driver.find_element_by_css_selector('div[class="schbox"] form input:first-child').send_keys('芭比')
#driver.find_element_by_css_selector('div[class="schbox"] form input:last-child').click()
#driver.find_element_by_css_selector('div[class="schbox"] form input:nth-last-child(2)').send_keys('芭比')

#driver.find_element_by_css_selector('div.r').click()
#driver.find_element_by_css_selector('.brand').click()
#driver.find_element_by_css_selector('.main_bar[style="position: relative;"]').click()
#driver.find_element_by_css_selector('textarea[id="s_is_result_css"]')            #百度
     #driver.find_element_by_xpath('//form[@id="form"]/span[2]/input').click()   #百度
#driver.find_element_by_css_selector('form#form span input[type="submit"]')         #百度

#driver.find_element_by_css_selector('input[class="but1"][type="text"][name="key"]').send_keys('那你')       #css的and关系


''''八、find_element_by_tag_name'''          #通过找标签类型来定位控件
#driver.find_element_by_tag_name('input')
  #bq=driver.find_elements_by_tag_name('dl')
  #bq[12].click()

