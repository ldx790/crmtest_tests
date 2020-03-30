from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from cases.basecase import BaseCase
from pages.day_page import Daypage
from commons.get_path import *
import ddt
from commons.tool import *
from commons.logger import Logger

logger = Logger().logger
@ddt.ddt
class CloDay(BaseCase):
    # 关闭日程

    @ddt.data(*get_data_from_csv('day_clo_datas.csv'))
    @ddt.unpack
    def test_day_close(self,title):
        '''
        验证关闭日程成功;CRM-ST-BG-011
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # title = "123"
        # #登录
        # sleep(4)
        # lp = LoginPage(self.driver)
        # sleep(2)
        # lp.open()
        # lp.login(username, password)
        # sleep(2)
        # #去日程页面
        # ip = IndexPage(self.driver)
        # ip.click_day()
        # sleep(3)
        # #在日程页面

        dp = Daypage(self.driver,DAY_URL)
        dp.open()
        dp.day_close(title)
        #断言
        text = dp.day_close_mark_get()
        logger.info(text)
        self.assertIn('关闭成功',text)

# if __name__ == '__main__':
#     unittest.main()