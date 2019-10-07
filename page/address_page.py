import page
from base.base import Base


class AddressPage(Base):
    """地址管理页面对象"""

    def click_address_manage(self):
        """点击地址管理"""
        self.click_func(page.address_manage)

    def click_add_address(self):
        """点击新增地址"""
        self.click_func(page.add_address)

    def input_receipt_name(self, receipt):
        """输入收件人"""
        self.input_data(page.receipt_name, receipt)

    def input_phone(self, phone):
        """输入电话"""
        self.input_data(page.mobile, phone)

    def click_address_province(self):
        """点击所在地区"""
        self.click_func(page.address_province)

    def click_area(self, pro, city, area):
        """点击省市区"""
        self.base_click_area(pro)
        self.base_click_area(city)
        self.base_click_area(area)

    def input_address_detail(self, addr):
        """输入详细地址"""
        self.input_data(page.address_detail, addr)

    def input_postcode(self, postcode):
        """输入邮编"""
        self.input_data(page.post_code, postcode)

    def click_address_default(self):
        """点击设为默认地址"""
        self.click_func(page.address_default)

    def click_save(self):
        """点击保存"""
        self.click_func(page.save)

    def click_edit(self):
        """点击编辑"""
        self.click_func(page.edit)

    def click_modify(self):
        """点击修改"""
        self.click_func(page.modify)

    def click_delete(self):
        """点击删除"""
        self.click_func(page.delete)

    def click_confirm_delete(self):
        """确认删除"""
        self.click_func(page.confirm_delete)

    def whether_add_address(self):
        """是否新增地址"""
        return self.base_get_text(page.address_receipt_name_phone)

    def page_go_add_address(self):
        """进入地址管理"""
        self.click_address_manage()
        self.click_add_address()

    def page_add_address(self, receipt, phone, pro, city, area, addr, postcode):
        """新增地址业务方法"""
        self.input_receipt_name(receipt)
        self.input_phone(phone)
        self.click_address_province()
        self.click_area(pro, city, area)
        self.input_address_detail(addr)
        self.input_postcode(postcode)
        self.click_address_default()
        self.click_save()

    def page_update_address(self, receipt, phone, pro, city, area, addr, postcode):
        """修改地址业务方法"""
        self.click_edit()
        self.click_modify()
        self.input_receipt_name(receipt)
        self.input_phone(phone)
        self.click_address_province()
        self.click_area(pro, city, area)
        self.input_address_detail(addr)
        self.input_postcode(postcode)
        self.click_save()

    def page_delete_address(self):
        """删除地址业务方法"""
        self.click_edit()
        self.click_delete()
        self.click_confirm_delete()

    def page_address_is_exists(self):
        """判断是否删除成功"""
        try:
            self.find_elements_func(page.address_receipt_name_phone, time=2)
            return False
        except:
            return True
