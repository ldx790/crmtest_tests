'''
@author: liudixuan
@software: SeleniumTest
@file: crm_notice_del.py
@time: 2020/3/19 22:14
@desc:
'''
from cases.basecase import BaseCase
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.notice_page import NoticePage
import unittest
from time import sleep
from selenium.webdriver.common.alert import Alert
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *
from commons.logger import Logger

logger = Logger().logger
@ddt.ddt
class DelNotice(BaseCase):
    '''
    删除公告管理
    '''

    @ddt.data(*get_data_from_csv("notice_add_datas.csv"))
    @ddt.unpack
    def test_del_notice(self,title):
        '''
        删除公告管理;CRM-ST-BG-022
        :return:
        '''
        #登录
        # username = "admin4"
        # password = "123456"
        # noticetitle = "公告2"
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username,password)
        # #去到公告管理页面
        # sleep(3)
        # ip = IndexPage(self.driver)
        # ip.username_click()
        # sleep(3)
        # ip.notice_click()
        sleep(3)
        #删除公告
        np = NoticePage(self.driver, NOTICE_URL)
        np.open()
        np.notice_del(title)
        np.notice_del_button_click()
        #确认删除
        sleep(3)
        confirm = Alert(self.driver)
        confirm.accept()

        #断言
        text = np.notice_title_get()
        logger.info(text)
        self.assertNotIn(title,text)

        def test_candel_notice(self):
            '''
            取消删除公告管理;CRM-ST-BG-021
            :return:
            '''
            # 登录
            username = "admin4"
            password = "123456"
            noticetitle = "公告"
            lp = LoginPage(self.driver)
            lp.open()
            lp.login(username, password)
            # 去到公告管理页面
            sleep(3)
            ip = IndexPage(self.driver)
            ip.username_click()
            sleep(3)
            ip.notice_click()
            sleep(3)
            # 删除公告
            np = NoticePage(self.driver)
            np.notice_del(noticetitle)
            np.notice_del_button_click()
            # 确认删除
            sleep(3)
            confirm = Alert(self.driver)
            confirm.dismiss()

            # 断言
            text = np.notice_title_get()
            logger.info(text)
            self.asserttIn(noticetitle, text)

# if __name__ == '__main__':
#     unittest.main()

