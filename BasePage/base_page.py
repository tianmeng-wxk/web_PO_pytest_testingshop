from 通过cookie绕过登录 import get_cookie
class BasePage(object):

    def __init__(self, driver,url):
        self.driver = driver
        self.url = url

    def quit_browser(self):
        self.driver.quit()

    def open_url(self):
        self.driver.get(self.url)

    def loc(self, loc):
        return self.driver.find_element(*loc)

    def maximize_window(self):
        self.driver.maximize_window()

    # def title(self):
    #     self.driver.title




