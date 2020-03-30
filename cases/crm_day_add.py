from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from pages.base_page import BasePage
from pages.add_day_page import Adddaykpage
from cases.basecase import BaseCase
from pages.day_page import Daypage
import ddt
from commons.tool import *
from commons.get_path import *
from commons.logger import Logger

logger = Logger().logger
@ddt.ddt
class Addday(BaseCase):
    # 添加日程
    @ddt.data(*get_data_from_csv('day_add_datas.csv'))
    @ddt.unpack
    def test_day_add(self,title):
        '''
        新建日程成功_验证输入所有项合法；CRM-ST-BG-009
        :return:
        '''

        dp = Daypage(self.driver,DAY_URL)
        dp.open()
        #去到添加日程页面
        dp.add_day_button_click()
        sleep(3)

        # 添加日程内容
        ap = Adddaykpage(self.driver)

        # #保存
        sleep(3)
        ap.day_title_click(title)
        ap.save_click()
        sleep(3)
        # 判断是否成功
        text = dp.day_title_get()
        logger.info(text)
        self.assertIn(title, text)

# if __name__ == '__main__':
#     unittest.main()