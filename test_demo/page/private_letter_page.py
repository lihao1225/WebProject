import os
from time import sleep

from test_demo.common.handle_path import Data
from test_demo.page.base_page import BasePage


class PrivateLetterPage(BasePage):


    def send_message(self):
        file_path = os.path.join(Data, "private_letter.yaml")
        self.parse_yaml(file_path, "send_message")
