from cases.basecase import BaseCase
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.task_page import TaskPage
import unittest
from time import sleep
import os
from selenium.webdriver.common.alert import Alert #引入警告
from commons.get_path import *
class EptTask(BaseCase):
    '''
            导出任务任务
            :return:
            '''

    def test_ept_task(self):
        '''
        导出任务成功_验证导出所有任务为excel格式；CRM-ST-BG-006
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # path='C:/Users/40511/Documents/Downloads/5kcrm_task_2020-03-18_1.xls'
        #
        # #登录
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username,password)
        # #去到任务页面
        # sleep(4)
        # ip = IndexPage(self.driver)
        # ip.task_button_click()
        #去到任务页面导出任务
        sleep(4)
        tp = TaskPage(self.driver, TASK_URL)
        tp.open()
        tp.task_tool_button_click()
        tp.task_export_button_click()
        #提示框点击确认
        sleep(4)
        confirm = Alert(self.driver)
        confirm.accept()
        sleep(4)
        #断言
        print(os.path.exists(EPT_TASK)) #查看是否成功
        self.assertTrue(os.path.exists(EPT_TASK))
        os.remove(EPT_TASK)             #删除数据

# if __name__ == '__main__':
#     unittest.main()
