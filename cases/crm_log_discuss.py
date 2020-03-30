'''
@author: liudixuan
@software: SeleniumTest
@file: crm_log_discuss.py
@time: 2020/3/19 16:55
@desc:
'''
from cases.basecase import BaseCase
from pages.add_log_page import AddLogPage
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.log_page import LogPage
from pages.detail_log_page import DetailLogPage
import unittest
from time import sleep
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *

@ddt.ddt
class DiscussLog(BaseCase):
    '''
    评论下属日志
    '''

    @ddt.data(*get_data_from_csv("log_discuss_datas.csv"))
    @ddt.unpack
    def test_discuss_log(self,logtitle,contenttext,discusstype):
        '''
        评论下属日志成功_验证输入所有项合法;CRM-ST-BG-017
        :return:
        '''
        #登录
        # username = "admin4"
        # password = '123456'
        # logtitle = '2020-03-19 工作日志'
        # contenttext ='很好'
        # discusstype ='站内信'
        #
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username,password)
        # sleep(3)
        # #去到日志页面
        # ip = IndexPage(self.driver)
        # ip.more_button_click()
        # ip.log_button_click()
        #在日志页面
        sleep(4)
        lgp = LogPage(self.driver, LOG_URL)
        lgp.open()
        #点击查看下属日志
        lgp.sub_button_click()
        sleep(4)
        lgp.look_log_click(logtitle)
        #去到下属日志详情页面
        sleep(4)
        #评论日志
        dlp = DetailLogPage(self.driver)
        dlp.discuss_click()
        sleep(4)
        dlp.discuss_content_send(contenttext)
        sleep(2)
        #选择通知方式
        dlp.discuss_type_click(discusstype)
        sleep(2)
        #确认
        dlp.ok_click()
        sleep(2)
        #断言
        text = dlp.success_get()
        self.assertIn('添加评论成功',text)

# if __name__ == '__main__':
#     unittest.main()