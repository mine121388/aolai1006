#导包
from page.address_page import AddressPage
from page.login_page import LoginPage


class PageIn:
    """统一工厂类"""

    def get_page_login(self):
        """获取page_login对象"""
        return LoginPage()

    def get_page_address(self):
        """获取page_address对象"""
        return AddressPage()