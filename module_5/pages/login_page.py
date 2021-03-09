from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"

    def register_new_user(self, email, password):
        mail_input = self.browser.find_element(*LoginPageLocators.REGISTER_MAIL_FIELD)
        mail_input.click()
        mail_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        password_input.click()
        password_input.send_keys(password)
        password2_input = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTER_PASSWORD_FIELD)
        password2_input.click()
        password2_input.send_keys(password)
        log_in_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        log_in_btn.click()

