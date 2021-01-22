from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestClick:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        # sleep(3)
        # self.driver.quit()
        pass

    def test_click(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID,"kw").send_keys("课堂派")
        self.driver.find_element(By.ID, "su").click()
        self.driver.find_element(By.XPATH,"//div//a[text()='www.ketangpai.com/']").click()
        window_handle = self.driver.window_handles
        self.driver.switch_to.window(window_handle[-1])
        self.driver.find_element(By.XPATH,"//div[@id = 'layui-layer1']/span/a").click()
        self.driver.find_element(By.XPATH,"//a[text() = '登录']").click()
        sleep(1)
        login = (By.ID, "login")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(login))
        user_name=(By.NAME,"account")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(user_name))
        self.driver.find_element(By.NAME,"account").send_keys("13810752514")
        password = (By.NAME,"pass")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(password))
        self.driver.find_element(By.NAME,"pass").send_keys("lh969900918")
        self.driver.find_element(By.XPATH,"//div[@class = 'padding-cont pt-login']//a[text()='登录']").click()
        self.driver.find_element(By.ID,"user").click()
        quit_user =(By.XPATH,"//a[text()='退出账户']")
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(quit_user))
        self.driver.find_element(*quit_user).click()
