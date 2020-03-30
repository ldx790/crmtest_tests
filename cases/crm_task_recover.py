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
class RecTask(BaseCase):
    '''
    还原任务
    '''

    @ddt.data(*get_data_from_csv('task_del_datas .csv'))
    @ddt.unpack
    def test_rec_task(self,tasktitle):
        '''
        还原任务_通过回收站还原任务;CRM-ST-BG-004
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # rec_title = "任务二"
        # #登录
        # sleep(4)
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username, password)
        # sleep(2)
        # #去任务页面
        # ip = IndexPage(self.driver)
        # ip.task_button_click()
        # 去回收站页面
        tp = TaskPage(self.driver, TASK_URL)
        tp.open()
        tp.task_rec_button_click()
        sleep(7)
        #还原被删除的任务
        rp = RecTaskPage(self.driver)
        rp.task_rec_title_click(tasktitle)
        #断言
        sleep(4)
        text = rp.task_rec_mesg_get()
        self.assertIn('还原成功',text)

# if __name__ == '__main__':
#     unittest.main()