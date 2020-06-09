from BasePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.login_page import LoginPage
from time import sleep



class SearchPage(BasePage):
    search = (By.XPATH, '//*[@id="q"]')
    searchbt = (By.XPATH, '//*[@id="sourch_form"]/a')
    searchtext=(By.XPATH, '/html/body/div[2]/div/div[1]/a[2]')

    url="http://www.testingedu.com.cn:8000/index.php/Home/User/index.html"

    def input_search(self, searchtext):
        self.loc(self.search).send_keys(searchtext)

    def click_searchbt(self):
        self.loc(self.searchbt).click()

    def get_search_text(self):
        return self.loc(self.searchtext).text

    def search_shop(self,searchtext):

        self.input_search(searchtext)
        self.click_searchbt()
        sleep(1)
if __name__ == '__main__':
    #同一个driver完整执行登录后搜索流程
    searchtext = "华为"
    username = 13800138006
    password = 123456
    vercode = 1111
    driver = webdriver.Chrome()
    lp = LoginPage(driver,LoginPage.url)
    lp.login(username, password, vercode)

    sp = SearchPage(driver,SearchPage.url)
    sleep(2)
    sp.input_search(searchtext)






