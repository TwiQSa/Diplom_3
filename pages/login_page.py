from pages.base_page import BasePage
from locators import AuthorizationPageLocators


class LoginPage(BasePage):

    def login_into_account(self, email_address, password):
        self.enter_email(email_address)
        self.enter_password(password)
        self.submit_login()

    def enter_email(self, email_address):
        self.input_text(AuthorizationPageLocators.EMAIL_INPUT, email_address)

    def enter_password(self, password):
        self.input_text(AuthorizationPageLocators.PASSWORD_INPUT, password)

    def authorization_form_is_on_login_page(self):
        return self.check_element(AuthorizationPageLocators.AUTHORIZATION_FORM)

    def click_on_recovery_button(self):
        self.click(AuthorizationPageLocators.RECOVERY_BUTTON)

    def submit_login(self):
        self.click(AuthorizationPageLocators.LOGIN_BUTTON)
