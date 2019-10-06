# 导包
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tool.tools import GetDriver


class Base:
    """奥莱基类"""

    def __init__(self):
        """获取driver对象"""
        self.driver = GetDriver.get_driver()

    def find_element_func(self, location, time=30, poll=0.2):
        """元素定位方法"""
        return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(
            lambda x: x.find_element(*location))

    def find_elements_func(self, location, time=30, poll=0.2):
        """定为一组元素方法"""
        return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(
            lambda x: x.find_element(*location))

    def input_data(self, location, values):
        """输入方法"""
        element = self.find_element_func(location)
        element.clear()
        element.send_keys(values)

    def click_func(self, location):
        """点击方法"""
        self.find_element_func(location).click()

    def get_text(self, location):
        """获取昵称方法"""
        return self.find_element_func(location).text

    def get_toast_msg(self, msg):
        """获取toast消息"""
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
        return self.find_element_func(loc, time=3, poll=0.1).text

    def get_msg(self, loc):
        """获取昵称方法"""
        return self.find_element_func(loc).text

    def base_scroll(self, loc2, loc1):
        """滑动"""
        el1 = self.find_element_func(loc1)
        el2 = self.find_element_func(loc2)
        self.driver.drag_and_drop(el2, el1)

    def base_get_img(self):
        """截图"""
        self.driver.get_screenshot_as_file("../img/err.png")
        self.base_write_img()

    def base_get_text_click(self, text, num):
        """文本的方式获取一组元素默认点击第一个"""
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(text)
        self.find_elements_func(loc)[num].click()

    def base_click_area(self, text):
        """点击省市区"""
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(text)
        self.find_element_func(loc).click()

    def base_get_text(self, loc):
        """获取一组元素的文本方法"""
        return [el.text for el in self.find_elements_func(loc)]

    def base_write_img(self):
        """将图片写入报告"""
        with open("./img/err.png", "rb")as f:
            allure.attach("失败原因: ", f.read(), allure.attach_type.PNG)

