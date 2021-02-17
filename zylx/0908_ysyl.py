import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://101.133.169.100/yuns/index.php/admin/index/login")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys('admin')
driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('admin')
driver.find_element_by_name('submit').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/ul/a[4]').click()  #点击营销
time.sleep(5)

driver.switch_to.frame('content')  # 切入iframe
driver.find_element_by_link_text("添加优惠券").click()
driver.find_element_by_xpath('//*[@id="form"]/table/tbody/tr[2]/td[2]/input').send_keys('国庆活动')
driver.find_element_by_xpath('//*[@id="form"]/table/tbody/tr[11]/td[2]/input').click()
driver.switch_to.parent_frame()
driver.implicitly_wait(3)

driver.find_element_by_xpath('/html/body/div[6]/span')

driver.close()
