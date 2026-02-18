from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This URL is not login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"
        
    def register_new_user(email, password):
        email_field = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        password_field1 = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        password_field2 = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        register = self.browser.find_element(By.CSS_SELECTOR, "#register_form .btn")
        email_field.send_keys(email)
        password_field1.send_keys(password)
        password_field2.send_keys(password)
        time.sleep(2)
        register.click()
        self.should_be_authorized_user()
