'''
@author: liudixuan
@software: SeleniumTest
@file: crm_task_clo.py
@time: 2020/3/19 20:46
@desc:
'''
from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from pages.task_page import TaskPage
from cases.basecase import BaseCase
from pages.rec_task_page import RecTaskPage

import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *

@ddt.ddt
class CloTask(BaseCase):
    '''
    关闭任务
    '''

    @ddt.data(*get_data_from_csv('task_clo_datas.csv'))
    @ddt.unpack
    def test_close_task(self,tasktitle):
        '''
        还原任务_通过回收站关闭任务;CRM-ST-BG-005
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # tasktitle = "主题"
        # # 登录
        # sleep(4)
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username, password)
        # sleep(2)
        # # 去任务页面
        # ip = IndexPage(self.driver)
        # ip.task_button_click()
        # 在任务页面页面
        tp = TaskPage(self.driver, TASK_URL)
        tp.open()
        #关闭任务
        sleep(10)
        tp.task_close_click(tasktitle)
        # 断言
        sleep(4)
        text = tp.task_mesg_get()
        self.assertIn('已成功关闭', text)


# if __name__ == '__main__':
#     unittest.main()