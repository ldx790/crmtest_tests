from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from cases.basecase import BaseCase
from pages.know_page import KnowPage
from commons.tool import *
from commons.logger import Logger
logger = Logger().logger

class RanKnow(BaseCase):
    '''
    知识排序
    '''

    def test_rank_know(self):
        '''
        排序_验证通过修改时间排序；CRM-ST-BG-013
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        #
        # # 登录
        # sleep(4)
        # lp = LoginPage(self.driver)
        # sleep(2)
        # lp.open()
        # lp.login(username, password)
        # sleep(2)
        # # 去知识页面
        # sleep(3)
        # ip = IndexPage(self.driver)
        # ip.know_button_click()
        #在知识页面点击创建时间排序
        sleep(3)
        kp = KnowPage(self.driver,KNOW_URL)
        kp.open()
        kp.know_settime_click()
        sleep(3)
        kp.know_settime_click()
        #断言
        ran = kp.get_settime()  #获取所有创建时间
        logger.info(ran)
        sleep(3)
        rk = kp.settime_sort()   #降序排列时间
        logger.info(rk)
        self.assertEqual(ran,rk)


# if __name__ == '__main__':
#     unittest.main()