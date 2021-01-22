from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAction:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        pass

    @pytest.mark.skip
    def test_action(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        action = ActionChains(self.driver)
        ele_click = self.driver.find_element(By.XPATH, "//input[@value = 'click me']")
        ele_dbl_click = self.driver.find_element(By.XPATH, "//input[@value = 'dbl click me']")
        ele_right_click = self.driver.find_element(By.XPATH, "//input[@value = 'right click me']")
        action.click(ele_click)
        action.double_click(ele_dbl_click)
        action.context_click(ele_right_click)
        action.perform()

    @pytest.mark.skip
    def test_remove_to(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_id('s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()
        sleep(2)

    @pytest.mark.skip
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element_by_id("dragger")
        ele_drop = self.driver.find_element(By.XPATH, "//div[text() = 'Item 1']")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag, ele_drop).perform()
        sleep(2)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele_input1 = self.driver.find_elements(By.XPATH, "//input[@type = 'textbox']")[0]
        ele_input2 = self.driver.find_elements(By.XPATH, "//input[@type = 'textbox']")[1]
        action = ActionChains(self.driver)
        ele_input1.click()
        action.send_keys("username").perform()
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)
        ele_input2.click()
        action.key_down(Keys.CONTROL, ele_input2).send_keys("v").key_up(Keys.CONTROL)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_touchaction(self):
        self.driver.get("http://www.baidu.com")
        ele_input = self.driver.find_element(By.ID, "kw")
        ele_input.send_keys("selenium测试")
        ele_search = self.driver.find_element(By.ID, "su")
        action = TouchActions(self.driver)
        action.tap(ele_search).perform()

        action.scroll_from_element(ele_input, 0, 10000).perform()
        sleep(3)

    @pytest.mark.skip
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag_ele = self.driver.find_element(By.XPATH, "//div[text() = '请拖拽我！']")
        drop_ele = self.driver.find_element(By.XPATH, "//div[text() = '请放置到这里！']")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele, drop_ele).perform()
        sleep(1)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        sleep(2)
        self.driver.find_element_by_id("submitBTN").click()

    @pytest.mark.skip
    def test_js(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        self.driver.execute_script("document.documentElement.scrollTop = 10000")

    def test_demo(self):
        self.driver.get("https://www.baidu.com")
        res = self.driver.find_element(By.XPATH, "//span[text() = '郑州进口冻猪肉外包装标本呈阳性']").text
        print(res)
