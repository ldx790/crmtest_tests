from cases.basecase import BaseCase
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.add_notice_page import AddNoticePage
from pages.notice_page import NoticePage
import unittest
from time import sleep
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *
from commons.logger import Logger

logger = Logger().logger
@ddt.ddt
class AddNotice(BaseCase):
    '''
    公告管理
    '''

    @ddt.data(*get_data_from_csv("notice_add_datas.csv"))
    @ddt.unpack
    def test_add_notice(self,title):
        '''
        添加公告管理;CRM-ST-BG-020
        :return:
        '''
        #登录
        # username = "admin4"
        # password = "123456"
        # title = "公告"
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username,password)
        # #去到公告管理页面
        # sleep(3)
        # ip = IndexPage(self.driver)
        # ip.username_click()
        # sleep(3)
        # ip.notice_click()
        # sleep(3)
        #去到添加公告管理页面
        np = NoticePage(self.driver,NOTICE_URL)
        np.open()
        np.add_notice_button_click()
        sleep(3)
        #添加公告内容
        ap = AddNoticePage(self.driver)
        ap.notice_title_send(title)
        ap.notice_save_click()
        sleep(3)
        #断言
        text = np.notice_title_get()
        logger.info(text)
        self.assertIn(title,text)

# if __name__ == '__main__':
#     unittest.main()



