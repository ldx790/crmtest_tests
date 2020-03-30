from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from cases.basecase import BaseCase
from pages.day_page import Daypage
from selenium.webdriver.common.alert import Alert #引入警告
import ddt
from commons.tool import *
from commons.logger import Logger

logger = Logger().logger
@ddt.ddt
class DelDay(BaseCase):
    # 删除日程
    @ddt.data(*get_data_from_csv('day_del_datas.csv'))
    @ddt.unpack
    def test_day_del(self,title):
        '''
        删除日程成功_验证指定日程进行删除;CRM-ST-BG-010
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # title = "主题"
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
        #在日程页面
        dp = Daypage(self.driver, DAY_URL)
        dp.open()
        #勾选指定日程

        dp.day_title_click(title)
        #点击删除
        sleep(3)
        dp.day_delete_click()
        #确认删除
        sleep(3)
        confirm = Alert(self.driver)
        confirm.accept()
        #断言
        sleep(3)
        tit = dp.day_title_get()
        logger.info(tit)
        self.assertNotIn(title,tit)

# if __name__ == '__main__':
#     unittest.main()