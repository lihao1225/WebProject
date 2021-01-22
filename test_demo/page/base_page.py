from time import sleep

import allure
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_demo.common.handle_black import handle_black


class BasePage:
    base_url = ''
    black_list = [(By.XPATH, "//div[@id = 'layui-layer1']/span/a")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)

    def save_screenshot(self):
        """
        电脑截屏通过allure打开
        :return:
        """
        # 截屏操作
        self.driver.save_screenshot("tmp.png")
        with open("tmp.png", "rb") as f:
            content = f.read()
        # 通过allure的的attach的方法来进行上传allure报告中
        allure.attach(content, attachment_type=allure.attachment_type.PNG)

    @handle_black
    def find(self, by, locator):
        """
        查找元素
        :param by:
        :param locator:
        :return:
        """
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    @handle_black
    def find_eles(self, by, locator):
        """
        查找多个元素
        :param by:
        :param locator:
        :return:
        """
        if locator is None:
            result = self.driver.find_elements(*by)
        else:
            result = self.driver.find_elements(by, locator)
        return result

    @handle_black
    def find_and_click(self, by, locator):
        """
        查找元素并进行点击
        :param by:
        :param locator:
        :return:
        """
        if locator is None:
            result = self.driver.find_element(*by).click()
        else:
            result = self.driver.find_element(by, locator).click()
        return result

    def get_ele_text(self, by, locator):
        """
        获取元素文本信息
        :return:
        """
        result = self.find(by, locator).text
        return result

    def time_sleep(self, time):
        """
        强制等待
        :param time:
        :return:
        """
        sleep(time)

    def switch_to_window(self):
        """
        窗口跳转
        :return:
        """
        windows_handle = self.driver.window_handles
        self.driver.switch_to.window(windows_handle[-1])

    def enter(self):

        action = ActionChains(self.driver)
        action.send_keys(Keys.CONTROL).send_keys(Keys.ENTER).perform()

    def wait_for_click(self, locator, time):
        """
        显示等待并点击
        :param locator:
        :param time: 超时时间
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout=time).until(
                expected_conditions.element_to_be_clickable(locator))
            return result
        except Exception as e:
            self.save_screenshot()
            raise e

    def wait_for_visible(self, locator, time):
        """
        显示等待元素可见
        :param locator:
        :param time: 超时时间
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout=time).until(
                expected_conditions.visibility_of_element_located(locator))
            return result
        except Exception as e:
            self.save_screenshot()
            raise e

    def move_to_ele_and_click(self, *args, **kwargs):
        action = ActionChains(self.driver)
        action.move_to_element(self.find(*args, **kwargs)).click().perform()

    def parse_yaml(self, path, func_name):
        """
        读取yaml文件
        :return:
        """
        with open(path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])

    def parse(self, steps):
        """
        解析yaml文件
        :param steps:
        :return:
        """
        for step in steps:
            if "click" == step["action"]:
                self.find(step["by"], step["locator"]).click()
            elif "send_key" == step["action"]:
                self.find(step["by"], step["locator"]).send_keys(step["text"])
            elif "visibility_ele" == step["action"]:
                self.wait_for_visible(time=step['time'], locator=eval(step['visible']))
            elif "click_able" == step["action"]:
                self.wait_for_click(time=step["time"], locator=eval(step["click_ele"]))
            elif "move_and_click" == step["action"]:
                self.move_to_ele_and_click(step["by"], step["locator"])
            elif "get_text" == step["action"]:
                res = self.get_ele_text(step["by"], step["locator"])
                return res
            elif "time_sleep" == step["action"]:
                self.time_sleep(step["time"])
            elif "switch_to_window" == step["action"]:
                self.switch_to_window()
            elif "enter" == step["action"]:
                self.enter()