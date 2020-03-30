from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from pages.add_task_page import Addtaskpage
from pages.task_page import TaskPage
from cases.basecase import BaseCase
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *
from commons.logger import Logger

logger = Logger().logger
@ddt.ddt
class Addtask(BaseCase):
    # 添加任务

    # 导入任务必填项数据
    @ddt.data(*get_data_from_csv('task_add_datas.csv'))
    @ddt.unpack
    def test_add_task(self,title):
        '''
        添加任务成功_验证必填项;CRM-ST-BG-001
        :return:
        '''
        # username = "xuan"
        # password = "123456"
        # title = "主题3"
        #登录
        # sleep(4)
        # lp = LoginPage(self.driver)
        # lp.open()
        # lp.login(username, password)
        # sleep(2)
        # #去任务页面
        # ip = IndexPage(self.driver)
        # ip.task_button_click()
        sleep(2)
        #去添加任务页面
        tp = TaskPage(self.driver,TASK_URL)
        tp.open()
        tp.task_add_button_click()
        sleep(4)
        #添加任务内容
        ap = Addtaskpage(self.driver)

        ap.task_title_click(title)

        ap.task_owner_click()
        sleep(4)
        ap.task_all_click()
        sleep(2)
        ap.task_ok_click()
        sleep(2)
        ap.save_click()
        sleep(2)
        #判断是否成功
        text = tp.task_title_get()
        self.assertIn(title,text)
        mesg = tp.task_mesg_get()
        logger.info(mesg)
        self.assertIn("添加成功",mesg)

    @ddt.data(*get_data_from_csv('task_addall_datas.csv'))
    @ddt.unpack
    def a_test_alladd_task(self,title,roles,apartment):
        '''
        添加任务成功_验证输入所有项合法;CRM-ST-BG-008
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # title = "主题二"
        # roles = 'admin4【CEO】'
        # apartment = '办公室'
        #登录
        # sleep(4)
        # lp = LoginPage(self.driver)
        #
        # lp.open()
        # lp.login(username, password)
        # sleep(2)
        # #去任务页面
        # ip = IndexPage(self.driver)
        # ip.task_button_click()
        # sleep(2)
        #去添加任务页面
        tp = TaskPage(self.driver, TASK_URL)
        tp.open()
        tp.task_add_button_click()
        sleep(4)
        #添加任务内容
        ap = Addtaskpage(self.driver)

        ap.task_title_click(title)
        #添加负责人
        ap.task_owner_click()
        sleep(4)
        ap.task_all_click()
        sleep(2)
        ap.task_ok_click()
        sleep(10)
        #点击任务相关人
        ap.task_role_click()
        sleep(5)
        #选择部门
        ap.task_apartment_click(apartment)
        #选择任务相关人
        ap.task_check_role_click(roles)
        sleep(2)
        #确认
        ap.task_role_ok_click()
        sleep(2)
        #保存
        ap.save_click()
        sleep(2)
        #判断是否成功
        text = tp.task_title_get()
        self.assertIn(title,text)
        mesg = tp.task_mesg_get()
        logger.info(mesg)
        self.assertIn("添加成功",mesg)

# if __name__ == '__main__':
#     unittest.main()