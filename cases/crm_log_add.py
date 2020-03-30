'''
@author: liudixuan
@software: SeleniumTest
@file: crm_log_add.py
@time: 2020/3/19 10:06
@desc:
'''
from cases.basecase import BaseCase
from pages.add_log_page import AddLogPage
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.log_page import LogPage
import unittest
from time import sleep
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *

@ddt.ddt
class AddLog(BaseCase):
    '''
    添加日志
    '''
    @ddt.data(*get_data_from_csv("log_add_datas.csv"))
    @ddt.unpack
    def test_add_log(self,logtitle,types,logconten):

        '''
        新建日志成功_验证输入所有项合法;CRM-ST-BG-018
        :return:
        '''
        #登录
        # username = "admin4"
        # password = '123456'
        # logtitle = '劳动日志'
        # types='周报'
        # logconten='劳动'
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username,password)
        # sleep(3)
        # #去到日志页面
        # ip = IndexPage(self.driver)
        # ip.more_button_click()
        # ip.log_button_click()
        #去到添加日志页面

        sleep(4)
        lgp = LogPage(self.driver,LOG_URL)
        lgp.open()
        lgp.add_log_button_click()
        #添加日志内容
        sleep(2)
        ap = AddLogPage(self.driver)
        ap.add_log_title_send(logtitle)
        sleep(3)
        #勾选日志类型
        ap.log_type_click(types)
        sleep(3)
        #输入日志内容
        ap.log_content_send(logconten)
        sleep(3)
        #保存
        ap.log_save_click()
        sleep(3)
        #断言
        text = lgp.add_log_success_get()
        self.assertIn('添加日志成功', text)
# if __name__ == '__main__':
#     unittest.main()

