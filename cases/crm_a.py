'''
@author: liudixuan
@software: SeleniumTest
@file: crm_a.py
@time: 2020/3/21 10:24
@desc:
'''
# from time import sleep
# import unittest
# from pages.login_page import *
# from pages.index_page import IndexPage
# from pages.base_page import BasePage
# from pages.add_day_page import Adddaykpage
# from cases.basecase import BaseCase
# from pages.day_page import Daypage
# import ddt
# from commons.tool import get_data_from_csv
# from commons.driver import chrome
# @ddt.ddt
# class Addday(unittest.TestCase):
#     # 添加日程
#     def setUp(self):
#         self.driver = chrome()
#
#     # @ddt.data(*get_data_from_csv('day_add_datas.csv'))
#     # @ddt.unpack
#     def test_day_add(self):
#         '''
#         新建日程成功_验证输入所有项合法；CRM-ST-BG-009
#         :return:
#         '''
#         username = "admin4"
#         password = "123456"
#         title = "主题"
#         # 登录
#         sleep(4)
#         lp = LoginPage(self.driver)
#         sleep(2)
#         lp.open()
#         lp.login(username, password)
#         sleep(2)
#         # 去日程页面
#         ip = IndexPage(self.driver)
#         ip.click_day()
#         sleep(3)
#         # 去添加日程页面
#         # day_url = 'http://192.168.1.134/crm/index.php?m=event'
#         tp = Daypage(self.driver)
#         tp.add_day_button_click()
#         sleep(3)
#         # 添加日程内容
#
#         ap = Adddaykpage(self.driver)
#
#         # #保存
#         sleep(3)
#         ap.day_title_click(title)
#         ap.save_click()
#         sleep(3)
#         # 判断是否成功
#         text = tp.day_title_get()
#         print(text)
#         self.assertIn(title, text)
#     def tearDown(self):
#         self.driver.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()