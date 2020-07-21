import os
import sys
from common.common import Logger,browser_type
from common.common import ReadExcel,read_excel
import unittest,pytest
from selenium import webdriver
from time import sleep
from ddt import ddt, data, file_data, unpack
from PageObject.login_page import LoginPage
from PageObject.search_page import SearchPage
from PageObject.order_list_page import OrderList



excel_data = ReadExcel("../config/login.xlsx", "Sheet1")
test_data = excel_data.dict_data()

excel_data2 = read_excel("../config/order_check.xlsx", "Sheet1")







@ddt
class TestCase:

    index = 1
    def setup(self):
        # #利用缓存跳过登录
        # option=webdriver.ChromeOptions()
        # option.add_argument("--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data")
        # self.driver = webdriver.Chrome(options=option)
        self.logger = Logger()
        self.driver = browser_type("chr")
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver, LoginPage.url)
        self.sp = SearchPage(self.driver, SearchPage.url)
        self.cp = OrderList(self.driver, OrderList.url)
        self.lp.login(13800138006, 123456, 1111)
    def teardown(self):
        self.driver.quit()



    #登录模块
    @data(*test_data)
    @unpack
    def test_1_login(self, **test_data):
        username = test_data['username']
        password = test_data['password']
        vercode = test_data['vercode']
        self.lp.login(username, password, vercode)
        sleep(3)
        self.logger.log().info("第{0}个用例,参数username:{1},password:{2},vercode:{3}".format(TestCase.index, username, password, vercode))
        TestCase.index += 1
        assert self.lp.assert_text() == test_data["veridate"]





    #搜索模块
    @file_data('../config/search.yaml')
    def test_2_search(self,**kwargs):
        self.lp.login("13800138006", "123456", "1111")  # 使用实例变量self才能调用别的方法内的属性
        searchtext = kwargs["text"]
        varidata = kwargs["varidata"]
        sleep(3)
        self.sp.search_shop(searchtext)
        self.logger.log().info("搜索内容为{}，验证内容为{}，实际结果为{}".format(searchtext, varidata,self.sp.assert_text()))
        assert self.sp.assert_text() == varidata




    #订单号查询
    @pytest.mark.parametrize("order, expect", excel_data2)
    def test_03_check(self,order,expect):
        self.cp.check_shop(order)
        assert expect == self.cp.assert_text()



if __name__ == '__main__':
    pytest.main()
    # 生成allure测试报告
    #import os
    #pytest.main(['-s','-q','./test_cases.py','--alluredir=../config/report/xml'])#生成alure缓存文件
    #os.system('allure serve ../config/report')
    # 命令行
    # allure generate --clean ../config/report/xml/ -o ../config/report/allure_html





