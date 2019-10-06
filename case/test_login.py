import sys
import os

import allure

sys.path.append(os.getcwd())
# 导包
import time
import pytest
from page.page_in import PageIn
from tool.read_yaml import read_yaml
from tool.tools import GetDriver


def build_data():
    return read_yaml("login.yaml")


class TestLogin:

    def setup_class(self):
        """初始化页面对象"""
        self.login = PageIn().get_page_login()
        self.login.click_op()
        self.login.go_to_login()

    def teardown_class(self):
        """关闭driver对象"""
        GetDriver.quit_driver()

    @allure.step(title="登录测试方法")
    @pytest.mark.parametrize("username,pwd,expect,succeed", build_data())
    def test_login(self, username, pwd, expect, succeed):
        """登录测试方法"""
        self.login.page_login(username, pwd)
        time.sleep(3)
        if succeed:
            try:
                nickname = self.login.get_nickname()
                assert nickname == expect
            except Exception as e:
                self.login.base_get_img()
                raise e
            finally:
                self.login.page_quit()
                self.login.go_to_login()
        else:
            try:
                toast = self.login.get_toast(expect)
                assert toast == expect
            except Exception as e:
                self.login.base_get_img()
                raise e
