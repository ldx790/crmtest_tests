from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from cases.basecase import BaseCase
from pages.know_page import KnowPage
from selenium.webdriver.common.alert import Alert #引入警告
import os
from commons.get_path import *

class EptKnow(BaseCase):
    '''
    导出知识
    '''

    def test_ept_know(self):
        '''
        导出知识成功_验证导出所有知识为 excel格式;CRM-ST-BG-015
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # path= 'C:/Users/40511/Documents/Downloads/5kcrm_knowledge_2020-03-18_1.xls'
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
        # sleep(3)
        #在知识页面 点击知识工具
        kp = KnowPage(self.driver, KNOW_URL)
        kp.open()
        kp.know_tool_click()
        kp.know_ept_click()
        #确认导出
        sleep(3)
        confirm = Alert(self.driver)
        confirm.accept()
        sleep(3)

        #断言
        print(os.path.exists(EPT_KNOW))
        # 断言
        self.assertTrue(os.path.exists(EPT_KNOW))
        os.remove(EPT_KNOW)

# if __name__ == '__main__':
#     unittest.main()