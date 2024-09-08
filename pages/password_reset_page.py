from pages.base_page import BasePage
from locators import RecoveryPageLocators


class PasswordResetPage(BasePage):

    def enter_email_address(self, email):
        self.input_text(RecoveryPageLocators.EMAIL_RECOVERY_INPUT, email)

    def enter_new_password(self, password):
        self.input_text(RecoveryPageLocators.NEW_PASSWORD_INPUT, password)

    def password_field_is_active(self, password):
        self.enter_new_password(password)
        self.click(RecoveryPageLocators.SHOW_PASSWORD_ICON)
        return self.check_element(RecoveryPageLocators.PASSWORD_INPUT_ACTIVE_GLOWS)

    def recovery_form_displayed(self):
        return self.check_element(RecoveryPageLocators.PASSWORD_RECOVERY_RECOVERY_PAGE)

    def click_on_recovery_button(self):
        self.click(RecoveryPageLocators.RECOVERY_BUTTON)

    def save_password_button_is_visible(self):
        return self.check_element(RecoveryPageLocators.SAVE_PASSWORD_BUTTON)
