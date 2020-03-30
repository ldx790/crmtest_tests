from cases.basecase import BaseCase
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.task_page import TaskPage
import unittest
from time import sleep
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *
from commons.logger import Logger

logger = Logger().logger
@ddt.ddt
class SeaTask(BaseCase):
    '''
    搜索任务功能
    '''

    @ddt.data(*get_data_from_csv('task_search_datas.csv'))
    @ddt.unpack
    def test_sea_task(self,visible_text_one,visible_text_two,visible_text_thr):
        '''
        搜索统计任务成功_搜索条件所有项合法;CRM-ST-BG-007
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # visible_text_one="任务主题"
        # visible_text_two='包含'
        # visible_text_thr='任务'
        # #登录
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username,password)
        # #去到任务页面
        # sleep(4)
        # ip = IndexPage(self.driver)
        # ip.task_button_click()
        #去到任务搜索页面
        sleep(4)
        tp = TaskPage(self.driver, TASK_URL)
        tp.open()
        #指定搜索
        sleep(4)
        #指定第一个下拉框
        tp.sea_one_select(visible_text_one)
        sleep(4)
        # 指定第二个下拉框
        tp.sea_two_select(visible_text_two)
        sleep(4)
        #指定第三个搜索条件
        tp.sea_thr_send(visible_text_thr)
        sleep(4)
        #点击搜索
        tp.sea_click()
        sleep(4)
        #断言
        text = tp.task_title_get()
        logger.info(text)
        for i in text:
            logger.info(i)
            self.assertIn(visible_text_thr,i)
            continue




# if __name__ == '__main__':
#     unittest.main()

