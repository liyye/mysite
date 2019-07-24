from selenium import webdriver
import time
import urllib

driver = webdriver.Chrome(r'F:\pachon2\无界面浏览器\chromedriver.exe')

driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("微博")

##id="su"是百度搜索按钮，click()是模拟点击
driver.find_element_by_id("su").click()


time.sleep(13)  #这个时间表示服务器响应时间
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()

time.sleep(13)
driver.switch_to_window(driver.window_handles[1])

driver.find_element_by_xpath('//*[@id="weibo_top_public"]/div/div/div[2]/input').send_keys("刘亦菲")

##id="su"是百度搜索按钮，click()是模拟点击
driver.find_element_by_xpath('//*[@id="weibo_top_public"]/div/div/div[2]/a').click()

# driver.get("http://ww3.sinaimg.cn/bmiddle/71482140ly1g4xwi5nmznj20qe10yqv5.jpg")
# time.sleep(3)
# driver.save_screenshot('03.png')






