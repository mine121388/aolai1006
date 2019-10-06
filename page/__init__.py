# 导包
from selenium.webdriver.common.by import By

# 登录
# 关闭按钮
close_img = By.ID, "com.yunmall.lc:id/img_close"
# 点击我
click_my = By.ID, "com.yunmall.lc:id/tab_me"
# 点击已有账号,去登陆
click_go_login = By.ID, "com.yunmall.lc:id/textView1"
# 输入账号
input_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 输入密码
input_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 点击登录
click_logon_button = By.ID, "com.yunmall.lc:id/logon_button"
# 获取昵称
get_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 点击设置
click_op = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 修改密码
modify_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 消息推送
notification = By.ID, "com.yunmall.lc:id/setting_notification"
# 点击退出
click_logout = By.ID, "com.yunmall.lc:id/setting_logout"
# 确认退出
confirm_logout = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

# 地址管理
# 地址管理
address_manage = By.ID, "com.yunmall.lc:id/setting_address_manage"
# 新增地址
add_address = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人
receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
# 手机号
mobile = By.ID, "com.yunmall.lc:id/address_add_phone"
# 所在地区
address_province = By.ID, "com.yunmall.lc:id/address_province"
# 详细地址
address_detail = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 邮编
post_code = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
save = By.ID, "com.yunmall.lc:id/button_send"
# 编辑
edit = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
# 修改
modify = By.ID, "com.yunmall.lc:id/modify"
# 删除
delete = By.ID, "com.yunmall.lc:id/delete"
# 确认删除
confirm_delete = By.ID, "com.yunmall.lc:id/ymdialog_left_button"
# 收件人姓名手机号
address_receipt_name_phone = By.ID, "com.yunmall.lc:id/receipt_name"
