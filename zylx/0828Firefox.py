from selenium import webdriver
import time

driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#driver.get(' https://www.baidu.com')
driver.get(' http://101.133.169.100/yuns/')
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys('1254')
a=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').get_attribute('value')
print(a)
driver.quit()