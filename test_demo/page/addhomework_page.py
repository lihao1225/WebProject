import os
from time import sleep

from selenium.webdriver.common.by import By

from test_demo.common.handle_path import Data
from test_demo.page.base_page import BasePage


class AddHomeWorkPage(BasePage):

    def add_homework(self):
        sleep(2)
        file_path = os.path.join(Data, "add_homework.yaml")
        self.parse_yaml(file_path, "add_homework")
        res = self.get_ele_text(By.XPATH,'//div[text()="作业提交成功"]')
        return res


