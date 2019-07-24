from selenium import webdriver
import time
import urllib

driver = webdriver.Chrome(r'F:\pachon2\无界面浏览器\chromedriver.exe')

# driver.get("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562954340786&di=c9adb388516c7e52be3ded7854c4fe73&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201412%2F16%2F20141216232944_5Gkat.jpeg")
#
# driver.save_screenshot('01.png')


# driver.get("https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%88%98%E4%BA%A6%E8%8F%B2%E5%BE%AE%E5%8D%9A&step_word=&hs=0&pn=1&spn=0&di=51370&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2109658171%2C3898114730&os=49153793%2C3016384000&simid=0%2C0&adpicid=0&lpn=0&ln=1149&fr=&fmq=1562992500824_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201901%2F06%2F20190106111307_ihudu.thumb.700_0.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B17tpwg2_z%26e3Bv54AzdH3Fks52AzdH3F%3Ft1%3D8a9aadccbd&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined")
#
# driver.find_element_by_class_name("bar-btn btn-download").click()
#
# driver.save_screenshot('02.png')

driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("刘亦菲")

##id="su"是百度搜索按钮，click()是模拟点击
driver.find_element_by_id("su").click()
# driver.find_element_by_id("su").click()
time.sleep(3)  #这个时间表示服务器响应时间
driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()
time.sleep(4)
driver.switch_to_window(driver.window_handles[1])
# driver.find_element_by_xpath('//*[@id="imgid"]/div[1]/ul/li[8]/div[1]/a').click()
# sreach_window=driver.current_window_handle
# time.sleep(6)
# driver.find_element_by_xpath('//*[@id="toolbar"]/span[7]').click()

driver.find_element_by_xpath('//*[@id="imgid"]/div[1]/ul/li[7]/div/a/img').click()
time.sleep(4)
driver.switch_to_window(driver.window_handles[2])
driver.find_element_by_xpath('//*[@id="toolbar"]/span[7]').click()


##获取新的页面快照


# driver.save_screenshot('02.png')












