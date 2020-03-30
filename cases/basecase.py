import unittest #引入unitest
from commons.driver import chrome
from commons import gloabalvar as gl
from commons.get_path import *
from time import sleep
class BaseCase(unittest.TestCase):
    def setUp(self):           #每条用例执行前都会调用这个方法，写在前面，前置条件
        self.driver = chrome()
        self.driver.get(HOST)
        sleep(3)
        self.driver.add_cookie(gl.get_global()) #添加获取到cookie
        sleep(3)
    def tearDown(self):        #每条用例执行前都会调用这个方法，写在后面，清除环境等操作
        return self.driver.quit()