# 导包
import time

import page
from base.base import Base


class LoginPage(Base):
    """对象库层"""

    def click_op(self):
        """关闭更新"""
        self.click_func(page.close_img)

    def click_my(self):
        """点击我"""
        self.click_func(page.click_my)

    def click_go_login(self):
        """点击已有账号,去登陆"""
        self.click_func(page.click_go_login)

    def input_username(self, username):
        """输入用户名"""
        self.input_data(page.input_username, username)

    def input_pwd(self, pwd):
        """输入密码"""
        self.input_data(page.input_pwd, pwd)

    def click_login_button(self):
        """点击登录"""
        self.click_func(page.click_logon_button)

    def get_nickname(self):
        """获取昵称"""
        return self.get_text(page.get_nickname)

    def get_toast(self, msg):
        """获取toast信息"""
        return self.get_toast_msg(msg)

    def click_opt(self):
        """点击设置"""
        self.click_func(page.click_op)

    def page_scroll(self):
        """消息推送滑动到修改密码"""
        self.base_scroll(page.notification, page.modify_pwd)

    def click_quit(self):
        """点击退出"""
        self.click_func(page.click_logout)

    def click_confirm_quit(self):
        """确认退出"""
        self.click_func(page.confirm_logout)

    def page_login(self, username, pwd):
        """登录业务"""
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_login_button()

    def go_to_login(self):
        """点击我去登陆"""
        self.click_my()
        self.click_go_login()

    def page_quit(self):
        """退出登录业务"""
        self.click_opt()
        self.page_scroll()
        self.click_quit()
        self.click_confirm_quit()

    def page_login_address(self):
        """登录进入设置"""
        self.click_op()
        self.go_to_login()
        self.page_login(username="13478603122", pwd="123456")
        time.sleep(1)
        self.click_opt()
