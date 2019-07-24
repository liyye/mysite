from selenium import webdriver
import time
import urllib

driver = webdriver.Chrome(r'F:\pachon2\无界面浏览器\chromedriver.exe')

driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("中国商标网")

##id="su"是百度搜索按钮，click()是模拟点击
driver.find_element_by_id("su").click()


time.sleep(4)  #这个时间表示服务器响应时间
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
#
time.sleep(6)
driver.switch_to_window(driver.window_handles[1])
#
driver.find_element_by_xpath('/html/body/div/div[7]/ul[1]/li[2]').click()
#
driver.switch_to_window(driver.window_handles[2])
'/html/body/div/div[5]/div[1]/div[1]/div/p[4]/a'
driver.find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div/p[4]/a').click()





