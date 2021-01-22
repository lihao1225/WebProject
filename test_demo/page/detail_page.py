import os
from time import sleep

from test_demo.common.handle_path import Data
from test_demo.page.addhomework_page import AddHomeWorkPage
from test_demo.page.base_page import BasePage
from test_demo.page.private_letter_page import PrivateLetterPage


class DetailPage(BasePage):

    def goto_homework_tab(self):
        file_path = os.path.join(Data, "detail.yaml")
        self.parse_yaml(file_path, "goto_homework_tab")
        return AddHomeWorkPage(self.driver)

    def goto_private_letter(self):
        file_path = os.path.join(Data, "detail.yaml")
        self.parse_yaml(file_path, "goto_private_letter")
        sleep(5)
        return PrivateLetterPage(self.driver)









