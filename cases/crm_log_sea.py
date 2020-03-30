'''
@author: liudixuan
@software: SeleniumTest
@file: crm_log_sea.py
@time: 2020/3/19 22:45
@desc:
'''
from cases.basecase import BaseCase
from pages.add_log_page import AddLogPage
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.log_page import LogPage
from pages.notice_page import NoticePage
import unittest
from time import sleep
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *

@ddt.ddt
class SeaLog(BaseCase):
    '''
    搜索日志
    '''

    @ddt.data(*get_data_from_csv("log_sea_datas.csv"))
    @ddt.unpack
    def test_search_log(self,visible_text_one,visible_text_two,visible_text_thr):
        '''
        搜索日志成功_验证通过内容搜索;CRM-ST-BG-019
        :return:
        '''
        #登录
        # username = "admin4"
        # password = '123456'
        # visible_text_one='标题'
        # visible_text_two='包含'
        # visible_text_thr='工作'
        #
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username,password)
        # sleep(3)
        # #去到日志页面
        # ip = IndexPage(self.driver)
        # ip.more_button_click()
        # sleep(3)
        # ip.log_button_click()
        #去到添加日志页面
        sleep(4)
        lgp = LogPage(self.driver, LOG_URL)
        lgp.open()
        # 指定第一个下拉框
        lgp.sea_one_select(visible_text_one)
        sleep(4)
        # 指定第二个下拉框
        lgp.sea_two_select(visible_text_two)
        sleep(4)
        # 指定第三个搜索条件
        lgp.sea_thr_send(visible_text_thr)
        sleep(4)
        # 点击搜索
        lgp.sea_click()
        sleep(4)
        # 断言
        text = lgp.get_log_title()
        for i in text:
            self.assertIn(visible_text_thr,i)
        #判断总数相等
        # self.assertEqual(4 or 1,len(lgp.get_log_title()))

# if __name__ == '__main__':
#     unittest.main()
#