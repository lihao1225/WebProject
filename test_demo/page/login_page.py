import os
from time import sleep

from selenium.webdriver.common.by import By

from test_demo.common.handle_path import Data
from test_demo.page.base_page import BasePage
from test_demo.page.course_page import CoursePage


class LoginPage(BasePage):
    # login = (By.ID, "login")
    # user_name = (By.NAME, "account")

    def login(self):
        # self.wait_for_visible(time=5,locator=self.login)
        # self.wait_for_visible(time=5,locator=self.user_name)
        file_path = os.path.join(Data, "login.yaml")
        self.parse_yaml(file_path, "login")
        return CoursePage(self.driver)


