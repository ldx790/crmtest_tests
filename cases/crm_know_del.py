from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from cases.basecase import BaseCase
from pages.know_page import KnowPage
from selenium.webdriver.common.alert import Alert #引入警告
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *

@ddt.ddt
class DelKnow(BaseCase):
    '''
    删除知识
    '''

    @ddt.data(*get_data_from_csv('know_del_datas.csv'))
    @ddt.unpack
    def test_del_know(self,title):
        '''
        删除知识成功_验证指定知识标题进行删除；CRM-ST-BG-016
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # title = '123'
        # # 登录
        # sleep(4)
        # lp = LoginPage(self.driver)
        # sleep(2)
        # lp.open()
        # lp.login(username, password)
        #
        # # 去知识页面
        # sleep(3)
        # ip = IndexPage(self.driver)
        # ip.know_button_click()
        # sleep(6)
        #在知识页面
        kp = KnowPage(self.driver, KNOW_URL)
        kp.open()
        kp.get_title_click(title)
        kp.know_del_click()
        #确认删除
        sleep(3)
        confirm = Alert(self.driver)
        confirm.accept()
        #断言
        text = kp.get_know_title()
        self.assertNotIn(title,text)


# if __name__ == '__main__':
#     unittest.main()
