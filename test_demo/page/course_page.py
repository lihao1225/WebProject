import os
from time import sleep

from test_demo.common.handle_path import Data
from test_demo.page.base_page import BasePage
from test_demo.page.detail_page import DetailPage


class CoursePage(BasePage):

    def goto_detail(self):
        file_path = os.path.join(Data, "course.yaml")
        self.parse_yaml(file_path, "goto_detail")
        sleep(2)
        return DetailPage(self.driver)

    def drop_class(self):
        file_path = os.path.join(Data, "course.yaml")
        self.parse_yaml(file_path, "drop_class")
        sleep(2)

    def add_class(self):
        file_path = os.path.join(Data, "course.yaml")
        self.parse_yaml(file_path, "add_class")
        sleep(2)
