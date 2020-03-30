from time import sleep
import unittest
from pages.login_page import *
from pages.index_page import IndexPage
from cases.basecase import BaseCase
from pages.know_page import KnowPage
from pages.add_know_page import AddKnowPage
import ddt
from commons.tool import get_data_from_csv
from commons.get_path import *

@ddt.ddt
class AddKnow(BaseCase):
    '''
    添加知识
    '''
    @ddt.data(*get_data_from_csv('know_add_datas.csv'))
    @ddt.unpack
    def test_add_know(self,know_title,know_text,know_content):
        '''
        添加知识成功_验证输入所有项合法;CRM-ST-BG-014
        :return:
        '''
        # username = "admin4"
        # password = "123456"
        # know_title="知识7"
        # know_text ='知识分类2'
        # know_content ='知识'
        # 登录
        # sleep(4)
        # lp = LoginPage(self.driver)
        # sleep(2)
        # lp.open()
        # lp.login(username, password)
        # sleep(2)
        # # 去知识页面
        # ip = IndexPage(self.driver)
        # ip.know_button_click()
        #去到添加知识页面
        kp = KnowPage(self.driver, KNOW_URL)
        kp.open()
        kp.add_know_button_click()
        #添加知识内容
        sleep(3)
        ap = AddKnowPage(self.driver)
        sleep(3)
        ap.know_title_send(know_title)
        sleep(3)
        ap.know_select(know_text)
        sleep(3)
        ap.know_content_send(know_content)
        sleep(3)
        ap.know_ok_click()
        sleep(3)
        #断言
        text = kp.add_know_mark_get()
        self.assertIn('添加成功',text)

# if __name__ == '__main__':
#     unittest.main()