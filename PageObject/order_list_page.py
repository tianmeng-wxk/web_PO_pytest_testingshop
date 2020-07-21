from BasePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
class OrderList(BasePage):
    url = 'http://www.testingedu.com.cn:8000/Home/Order/order_list.html'
    check = (By.XPATH,'//*[@id="search_key"]')
    checkbt = (By.XPATH,'//*[@id="search_order"]/input[2]')
    shop = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[1]/div[4]/table[1]/tbody/tr[2]/td[1]/div/div[2]/a')

    def input_check(self,txt):
        self.loc(self.check).send_keys(txt)

    def click_checkbt(self):
        self.loc(self.checkbt).click()

    #查询订单流程
    def check_shop(self,txt):
        self.open_url()
        sleep(2)
        self.input_check(txt)
        self.click_checkbt()

    def assert_text(self):
        return self.loc(self.shop).text