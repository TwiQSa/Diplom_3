from locators import PersonalPageLocators
from pages.base_page import BasePage


class PersonalPage(BasePage):

    def click_order_history_personal_page(self):
        self.click(PersonalPageLocators.ORDER_HISTORY_PERSONAL_PAGE)

    def check_order_history_form(self):
        return self.check_element(PersonalPageLocators.ORDER_HISTORY_SECTION_FROM_PERSONAL_PAGE)

    def check_personal_profile_visible(self):
        return self.check_element(PersonalPageLocators.PROFILE_FORM_PERSONAL_PAGE)

    def logout_from_account(self):
        self.click(PersonalPageLocators.LOGOUT_BUTTON)
