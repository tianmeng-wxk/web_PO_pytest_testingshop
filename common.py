from PIL import Image
import requests,logging,time
import yaml
from selenium import webdriver
from Chaojiying_Python.chaojiying import Chaojiying_Client
#第三方接口识别验证码方法一
def ivercode(driver):
    driver.save_screenshot("E:\\pycharm\\testingshop\\vercode_img\\page.png")
    vcode = driver.find_element_by_xpath("//*[@id='verify_code_img']")
    loc = vcode.location
    size = vcode.size
    left = loc['x']
    top = loc['y']
    right = (loc['x'] + size['width'])
    button = (loc['y'] + size['height'])
    page_pic = Image.open("E:\\pycharm\\testingshop\\vercode_img\\page.png")
    v_code_pic = page_pic.crop((left, top, right, button))
    v_code_pic.save("E:\\pycharm\\testingshop\\vercode_img\\vercode.png")
    chaojiying = Chaojiying_Client('qq121292679', 'a546245426', '904603')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('E:\\pycharm\\testingshop\\vercode_img\\vercode.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    res = chaojiying.PostPic(im, 1902)
    vercode = res['pic_str']
    return vercode
#第三方接口识别验证码方法二
def ivercode2(driver):
    ele = driver.find_element_by_xpath("//*[@id='verify_code_img']")
    ele.screenshot("E:\\pycharm\\testingshop\\vercode_img\\verify.png")
    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
    }
    data = {
        'user': 'wuqingfqng',
        'pass2': '6e8ebd2e301f3d5331e1e230ff3f3ca5',#密碼：wuqing&fqng
        "softid": "904357",
        "codetype": "1902"
    }
    userfile = open("E:\\pycharm\\testingshop\\vercode_img\\verify.png","rb").read()
    userfile = {"userfile": ("E:\\pycharm\\testingshop\\vercode_img\\verify.png", userfile)}
    res = requests.post("http://upload.chaojiying.net/Upload/Processing.php",data=data,files=userfile,headers=headers)
    res = res.json()
    vercode = res["pic_str"]
    return vercode


def read_yaml(file_path):
    file = open(file_path, encoding='utf-8')
    testdata = yaml.load(file, Loader=yaml.FullLoader)  # 或者yaml.full_load()
    return testdata


class Logger:
    def log(self):
        logger=logging.getLogger("logger")
        logger.setLevel(logging.DEBUG)
        sh=logging.StreamHandler()
        fh=logging.FileHandler(filename="../config/log/{}_log".format(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())),encoding="utf-8")
        formator=logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(msg)s", datefmt="%Y/%m%d%X")
        sh.setFormatter(formator)
        fh.setFormatter(formator)
        logger.addHandler(fh)
        logger.addHandler(sh)
        return logger

def browser_type(type):
    type=type.upper()
    if type == "CHR":
        driver = webdriver.Chrome()
    elif type == "IE":
        driver = webdriver.Ie()
    elif type == "FF":
        driver = webdriver.Firefox()
    return driver







