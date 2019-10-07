import sys
import os
sys.path.append(os.getcwd())
# 导包
from tool.read_yaml import read_yaml1
import pytest
from page.page_in import PageIn
from tool.tools import GetDriver


def build_data(key):
    arr = []
    if key == "address_add":
        arr.append(tuple(read_yaml1("address.yaml").get(key).values()))
        return arr
    else:
        arr.append(tuple(read_yaml1("address.yaml").get(key).values()))
        return arr


class TestAddress:

    def setup_class(self):
        """初始化页面对象"""
        self.address = PageIn().get_page_address()
        self.login = PageIn().get_page_login()
        self.login.page_login_address()

    def teardown_class(self):
        """退出driver对象"""
        GetDriver.quit_driver()

    @pytest.mark.parametrize("receipt, phone, pro, city, area, addr, postcode", build_data("address_add"))
    def test01_add_address(self, receipt, phone, pro, city, area, addr, postcode):
        """新增地址测试方法"""
        self.address.page_go_add_address()
        self.address.page_add_address(receipt, phone, pro, city, area, addr, postcode)
        try:
            expect = receipt + " " + phone
            assert expect in self.address.whether_add_address()
        except:
            self.address.base_get_img()

    @pytest.mark.parametrize("receipt, phone, pro, city, area, addr, postcode", build_data("address_update"))
    def test02_update_address(self, receipt, phone, pro, city, area, addr, postcode):
        """更新地址测试方法"""
        self.address.page_update_address(receipt, phone, pro, city, area, addr, postcode)
        try:
            expect = receipt + " " + phone
            assert expect in self.address.whether_add_address()
        except Exception as e:
            self.address.base_get_img()
            raise e

    def test03_delete_address(self):
        """删除地址测试方法"""
        self.address.page_delete_address()
        try:
            assert self.address.page_address_is_exists()
        except:
            self.address.base_get_img()

