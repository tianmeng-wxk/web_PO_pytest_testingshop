from HTMLTestRunner import HTMLTestRunner
import unittest,os
from test_case.test_cases import TestCase
curPath = os.path.abspath(os.path.dirname(__file__))

# path = curPath+"../../test_case"
# discover = unittest.defaultTestLoader.discover(start_dir=path, pattern="read_*.py")#在path目录下运行以read开头的文件,运行discover

suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
dir = curPath+"../../config/report/report.html"

with open(dir,'wb')as file:
    runner = HTMLTestRunner(stream=file, title="特斯汀商城測試報告", description="特斯汀商城web测试")
    runner.run(suite)