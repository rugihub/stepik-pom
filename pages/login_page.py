from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # �������� �� ���������� url �����
        assert "login" in self.browser.current_url, "No login sub-string in current_url"

    def should_be_login_form(self):
        # ��������, ��� ���� ����� ������
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form not present"
   
    def should_be_register_form(self):
        # ��������, ��� ���� ����� ����������� �� ��������
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form not present"
   