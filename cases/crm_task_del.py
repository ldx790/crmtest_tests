from cases.basecase import BaseCase
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.task_page import TaskPage
import unittest
from time import sleep
from selenium.webdriver.common.alert import Alert #引入警告
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *
from commons.logger import Logger

logger = Logger().logger
@ddt.ddt
class DelTask(BaseCase):
    '''
    删除任务、取消删除功能
    '''

    @ddt.data(*get_data_from_csv('task_del_datas .csv'))
    @ddt.unpack
    def test_del_task(self,title):
        '''
        删除任务成功_验证单选第一条进行删除；CRM-ST-BG-002
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # tasktitle="任务二"
        #
        # #登录
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username,password)
        # #去任务页面
        # ip = IndexPage(self.driver)
        # ip.task_button_click()
        #查找指定任务进行删除
        sleep(3)
        tp = TaskPage(self.driver, TASK_URL)
        tp.open()
        sleep(3)
        tp.task_title_click(title)
        sleep(3)
        tp.task_delate_button_click()
        sleep(3)
        #删除弹框确认

        confirm = Alert(self.driver)
        confirm.accept()
        sleep(3)
        self.driver.refresh()
        sleep(2)
        #断言
        text = tp.task_title_get()
        logger.info(text)
        self.assertNotIn(title,text)

    @ddt.data(*get_data_from_csv('task_canceldel_datas .csv'))
    @ddt.unpack
    def test_candel_task(self,title):
        '''
        取消删除任务成功_验证单选第一条进行删除；CRM-ST-BG-003
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # tasktitle="任务二"

        #登录
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username,password)
        # #去任务页面
        # ip = IndexPage(self.driver)
        # ip.task_button_click()
        # #查找指定任务进行删除

        sleep(3)
        tp = TaskPage(self.driver, TASK_URL)
        tp.open()
        tp.task_title_click(title)
        sleep(3)
        tp.task_delate_button_click()
        sleep(3)
        #删除弹框确认
        confirm = Alert(self.driver)
        confirm.dismiss()
        sleep(3)
        #断言
        text = tp.task_title_get()
        logger.info(text)
        self.assertIn(title,text)

# if __name__ == '__main__':
#     unittest.main()
