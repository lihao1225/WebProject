import os
from time import sleep

from selenium.webdriver.common.by import By

from test_demo.common.handle_black import handle_black
from test_demo.common.handle_path import Data
from test_demo.page.base_page import BasePage
from test_demo.page.login_page import LoginPage


class MainPage(BasePage):

    base_url = "https://www.ketangpai.com/"

    @handle_black
    def goto_login(self):
        file_path = os.path.join(Data,"main.yaml")
        self.parse_yaml(file_path,"goto_login")
        sleep(1)
        return LoginPage(self.driver)
