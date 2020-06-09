import os
import sys

from common import Logger,browser_type
from xlrd读取文件.read_eg import ReadExcel
import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt, data, file_data, unpack
from PageObject.login_page import LoginPage
from PageObject.search_page import SearchPage
#添加路径
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('E:\\pycharm')


excel_path = curPath+"../../config/testingdata.xlsx"
sheet_name = "Sheet1"
excel_data = ReadExcel(excel_path, sheet_name)
test_data = excel_data.dict_data()
@ddt
class TestCase(unittest.TestCase):
    index = 1

    def setUp(self) -> None:
        # #利用缓存跳过登录
        # option=webdriver.ChromeOptions()
        # option.add_argument("--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data")
        # self.driver = webdriver.Chrome(options=option)
        self.logger = Logger()
        self.driver=browser_type("chr")
        self.lp = LoginPage(self.driver, LoginPage.url)
        self.lp.login("13800138006", "123456", "1111")  # 使用实例变量self才能调用别的方法内的属性
        self.sp = SearchPage(self.driver, SearchPage.url)

    def tearDown(self) -> None:

        self.sp.quit_browser()


    # # 登录
    # @data(*test_data)
    # @unpack
    # def test_1_login(self, **test_data):
    #     username = test_data['username']
    #     password = test_data['password']
    #     vercode = test_data['vercode']
    #     self.lp.login(username, password, vercode)
    #     sleep(5)
    #     self.assertEqual(self.get_username(), test_data["veridate"], msg="登录失败")
    #     self.logger.log().info("第{0}个用例,参数username:{1},password:{2},vercode:{3}".format(TestCase.index, username, password, vercode))
    #     TestCase.index+=1



    #搜索
    @file_data('data.yaml')
    def test_2_search(self, **kwargs):
        searchtext = kwargs['search']["text"]
        varidata = kwargs["varidata"]
        sleep(5)
        self.sp.search_shop(searchtext)
        self.assertEqual(self.sp.get_search_text(), varidata, msg="搜索失败")
        self.logger.log().info("搜索内容为{}，验证内容为{}，实际结果为{}".format(searchtext, varidata,self.sp.get_search_text()))
if __name__ == '__main__':
    unittest.main()





