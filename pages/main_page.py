import requests
from data import Ingredients, ApiEndpoints
from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    def click_personal_account_button(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT)

    def click_personal_account_button_to_login_on_main_page(self):
        self.click(MainPageLocators.ACCOUNT_LOGIN_BUTTON)

    def click_construction_button(self):
        self.click(MainPageLocators.CONSTRUCTOR)

    def click_order_feed_button(self):
        self.click(MainPageLocators.ORDER_FEED)

    def click_bun(self):
        self.click(MainPageLocators.CRATOR_BUN)

    def check_constructor_section(self):
        return self.check_element(MainPageLocators.CONSTRUCTOR_SECTION)

    def check_order_feed_section(self):
        return self.check_element(MainPageLocators.ORDER_FEED_SECTION)

    def check_order_form_is_displayed(self):
        return self.check_element(MainPageLocators.ORDER_FEED_FORM)

    def check_bun_details(self):
        return self.check_element(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    def close_bun_details_window_icon(self):
        self.click(MainPageLocators.CLOSE_ICON_BUTTON_IN_INGREDIENT_DETAILS)

    def check_bun_details_window_is_closed(self):
        return self.element_is_absent(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    def check_visibility_of_create_order_button(self):
        self.wait_for_element_to_be_visible(MainPageLocators.CREATE_ORDER_BUTTON)

    def click_create_order_button(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

    def add_ingredient_to_basket(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT_BUN1, MainPageLocators.ORDER_BASKET)

    def get_number_of_ingredients_from_counter_in_order(self):
        self.wait_for_element_to_be_visible(MainPageLocators.INGREDIENT_COUNTER_IN_ORDER)
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER_IN_ORDER)

    def get_number_of_ingredients_in_order(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.INGREDIENT_COUNTER_IN_ORDER)
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER_IN_ORDER)

    def create_order(self):
        self.add_ingredient_to_basket()
        self.click_create_order_button()

    def order_creation(self, user_creation):
        token = user_creation[1].json()['accessToken']
        header = {'Authorization': token}
        ingredients = Ingredients.ingredients_for_order_creation
        response = requests.post(ApiEndpoints.ORDER_CREATION_ENDPOINT, headers=header, data=ingredients)
        return response.json()['order']['number']
