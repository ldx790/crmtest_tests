from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from cases.basecase import BaseCase
from pages.day_page import Daypage
from selenium.webdriver.common.alert import Alert #引入警告
import os
from commons.tool import *
import ddt

@ddt.ddt
class EptDay(BaseCase):
    # 导出日程
    def test_day_ept(self):
        '''
        导出日程成功;CRM-ST-BG-012
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # path = "C:/Users/40511/Documents/Downloads/5kcrm_event_2020-03-18_1.xls"
        # #登录
        # sleep(4)
        # lp = LoginPage(self.driver)
        # sleep(2)
        # lp.open()
        # lp.login(username, password)
        # sleep(2)
        # #去日程页面
        # ip = IndexPage(self.driver)
        # ip.click_day()
        # sleep(3)
        # #在日程页面
        # dp = Daypage(self.driver)

        dp = Daypage(self.driver, DAY_URL)
        dp.open()
        #点击日程工具

        dp.day_tool_click()
        #点击导出日程
        sleep(3)
        dp.day_ept_click()
        #确认导出
        sleep(3)
        confirm = Alert(self.driver)
        confirm.accept()
        sleep(3)
        #断言

        self.assertTrue(os.path.exists(EPT_DAY))
        os.remove(EPT_DAY)

# if __name__ == '__main__':
#     unittest.main()