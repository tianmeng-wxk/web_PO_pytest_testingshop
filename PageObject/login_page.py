from Chaojiying_Python.chaojiying import Chaojiying_Client
from BasePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from common.common import ivercode,ivercode2
# from PIL import Image
# import pytesseract
# import requests

class LoginPage(BasePage):

    uname = (By.XPATH, '//*[@id="username"]')
    upwd = (By.XPATH, '//*[@id="password"]')
    vcode = (By.XPATH, '//*[@id="verify_code"]')
    vcodeimg = (By.XPATH, '//*[@id="verify_code_img"]')
    loginbt = (By.XPATH, '//*[@id="loginform"]/div/div[6]/a')
    get_uname=(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/a[1]')
    url = "http://www.testingedu.com.cn:8000/Home/user/login.html"

    def input_username(self, username):
        self.loc(self.uname).send_keys(username)

    def input_password(self, password):
        self.loc(self.upwd).send_keys(password)

    def input_vercode(self, vercode):
        self.loc(self.vcode).send_keys(vercode)

    def click_loginbt(self):
        self.loc(self.loginbt).click()

    def assert_text(self):
        return self.loc(self.get_uname).text

    def login(self, username, password,vercode):
        self.maximize_window()
        self.open_url()
        sleep(3)
        self.input_username(username)
        self.input_password(password)
        # 调用识别验证码接口
        #vercode = ivercode2(driver)
        self.input_vercode(vercode)
        sleep(2)
        self.click_loginbt()
        sleep(3)







if __name__ == '__main__':
    url = "http://www.testingedu.com.cn:8000/Home/user/login.html"
    username = "13800138006"
    password = "123456"
    vercode = "1111"
    driver = webdriver.Chrome()
    lp = LoginPage(driver,LoginPage.url)
    lp.login(username, password,vercode)








