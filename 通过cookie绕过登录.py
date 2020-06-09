#通过cookie绕过登录
from selenium import webdriver
from time import sleep
# def cookie():
#     self.driver = webdriver.Chrome()
#     driver.get("http://www.testingedu.com.cn:8000")
#     # 添加Cookie
#     #driver.add_cookie({'name': 'PHPSESSID', 'value': '8tvolhi2piuqdg4q44h6bdqg16'})
#
#     driver.add_cookie({'name': 'is_distribut', 'value': '0'})
#     driver.add_cookie({'name': 'parent_region', 'value': '%5B%7B%22id%22%3A3%2C%22name%22%3A%22%u4E1C%u57CE%u533A%22%7D%2C%7B%22id%22%3A14%2C%22name%22%3A%22%u897F%u57CE%u533A%22%7D%2C%7B%22id%22%3A22%2C%22name%22%3A%22%u5D07%u6587%u533A%22%7D%2C%7B%22id%22%3A30%2C%22name%22%3A%22%u5BA3%u6B66%u533A%22%7D%2C%7B%22id%22%3A39%2C%22name%22%3A%22%u671D%u9633%u533A%22%7D%2C%7B%22id%22%3A83%2C%22name%22%3A%22%u4E30%u53F0%u533A%22%7D%2C%7B%22id%22%3A105%2C%22name%22%3A%22%u77F3%u666F%u5C71%u533A%22%7D%2C%7B%22id%22%3A115%2C%22name%22%3A%22%u6D77%u6DC0%u533A%22%7D%2C%7B%22id%22%3A145%2C%22name%22%3A%22%u95E8%u5934%u6C9F%u533A%22%7D%2C%7B%22id%22%3A159%2C%22name%22%3A%22%u623F%u5C71%u533A%22%7D%2C%7B%22id%22%3A188%2C%22name%22%3A%22%u901A%u5DDE%u533A%22%7D%2C%7B%22id%22%3A204%2C%22name%22%3A%22%u987A%u4E49%u533A%22%7D%2C%7B%22id%22%3A227%2C%22name%22%3A%22%u660C%u5E73%u533A%22%7D%2C%7B%22id%22%3A245%2C%22name%22%3A%22%u5927%u5174%u533A%22%7D%2C%7B%22id%22%3A264%2C%22name%22%3A%22%u6000%u67D4%u533A%22%7D%2C%7B%22id%22%3A281%2C%22name%22%3A%22%u5E73%u8C37%u533A%22%7D%5D'})
#     driver.add_cookie({'name': 'is_mobile', 'value': '0'})
#     driver.add_cookie({'name': 'province_id', 'value': '1'})
#     driver.add_cookie({'name': 'city_id', 'value': '2'})
#     driver.add_cookie({'name': 'district_id', 'value': '3'})
#     driver.add_cookie({'name': 'PHPSESSID', 'value': '13o403j9pmjr5da092npibn836'})
#     driver.add_cookie({'name': 'user_id', 'value': '8'})
#     driver.add_cookie({'name': 'uname', 'value': 'KEY'})
#
#     # 刷新页面
#     driver.refresh()
#     # 等待两秒
#     sleep(2)
#     # 获取登录用户名并打印
#     username = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/a[1]").text
#     print(username)
    #关闭浏览器

#自动获取cookie
def get_cookie():
    driver1 = webdriver.Chrome()
    driver1.maximize_window()
    driver1.get('http://www.testingedu.com.cn:8000/index.php/Home/user/login.html')
    driver1.find_element_by_xpath('//*[@id="username"]').send_keys('13800138006')
    driver1.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
    driver1.find_element_by_xpath('//*[@id="verify_code"]').send_keys('1111')
    sleep(1)
    driver1.find_element_by_xpath('//*[@id="loginform"]/div/div[6]/a').click()
    sleep(5)
    save_cookie = driver1.get_cookies()  # 列表里面有两个字典cookie信息，一个是登录之前的，一个是登录之后的
    print(save_cookie)
    driver1.quit()
    driver2 = webdriver.Chrome()
    driver2.maximize_window()
    # 必须首先加载网站，这样selenium才知道cookie是属于哪个网站的
    driver2.get('http://www.testingedu.com.cn:8000/index.php')
    print(driver2.get_cookies())
    driver2.delete_all_cookies()  # 一旦加载网站，即使没登录，也会产生一个cookie，需要删除cookie
    for cookie in save_cookie:
        driver2.add_cookie(cookie) # 添加driver1登录成功之后的cookie

    driver2.get('http://www.testingedu.com.cn:8000/index.php')
    print(driver2.get_cookies())
    sleep(3)

#另一种方法
#https://www.jb51.net/article/138046.htm

#另一种方法
#  1 # coding:utf-8
#  2 import requests
#  3 # 先打开登录首页，获取部分cookie
#  4 url = "https://passport.cnblogs.com/user/signin"
#  5 headers = {
#  6             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
#  7            }  # get方法其它加个ser-Agent就可以了
#  8 s = requests.session()
#  9 r = s.get(url, headers=headers,verify=False)
# 10 print s.cookies
# 11 # 添加登录需要的两个cookie
# 12 c = requests.cookies.RequestsCookieJar()
# 13 c.set('.CNBlogsCookie', 'xxx')  # 填上面抓包内容
# 14 c.set('.Cnblogs.AspNetCore.Cookies','xxx')  # 填上面抓包内容
# 15 s.cookies.update(c)
# 16 print s.cookies
# 17 # 登录成功后保存编辑内容
# 18 url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
# 19 body = {"__VIEWSTATE": "",
# 20         "__VIEWSTATEGENERATOR":"FE27D343",
# 21         "Editor$Edit$txbTitle":"这是绕过登录的标题：北京-宏哥",
# 22         "Editor$Edit$EditorBody":"<p>这里是中文内容：http://www.cnblogs.com/duhong/</p>",
# 23         "Editor$Edit$Advanced$ckbPublished":"on",
# 24         "Editor$Edit$Advanced$chkDisplayHomePage":"on",
# 25         "Editor$Edit$Advanced$chkComments":"on",
# 26         "Editor$Edit$Advanced$chkMainSyndication":"on",
# 27         "Editor$Edit$lkbDraft":"存为草稿",
# 28          }
# 29 r2 = s.post(url2, data=body, verify=False)
# 30 print r.content