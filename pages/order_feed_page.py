from locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def get_order_history(self):
        order_elements = self.retrieve_elements(OrderFeedPageLocators.ALL_ORDER_NUMBERS)
        processed_orders = [order.text[2:] for order in order_elements]
        return processed_orders

    def order_counter_displayed(self, locator):
        return self.get_text_from_element(locator)

    def order_details_displayed(self):
        return self.check_element(OrderFeedPageLocators.ORDER_INFO_INSIDE_ORDER)

    def select_order(self):
        self.click_after_visibility(OrderFeedPageLocators.ORDER_WINDOW_DETAIL)

    def refresh_feed_page(self):
        self.browser.refresh()
        self.wait_for_element_to_be_visible(OrderFeedPageLocators.TOTAL_ORDERS_COUNT)

    def get_orders_in_progress(self):
        in_progress_elements = self.retrieve_elements(OrderFeedPageLocators.IN_PROGRESS_ORDERS_COUNT)
        active_orders = [item.text[1:] for item in in_progress_elements]
        return active_orders
