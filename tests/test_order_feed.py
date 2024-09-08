from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators import OrderFeedPageLocators
import pytest
import allure


class TestOrderFeedPage:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Проверка, что открывается окно с деталями заказа')
    def test_order_details_window(self, main_page, feed_order_page):
        main_page.click_order_feed_button()
        feed_order_page.select_order()

        assert feed_order_page.order_details_displayed()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Проверка, что заказы из раздела История заказов отображаются на странице Лента заказов')
    def test_user_order_appears_in_order_history(self, user_creation, new_order_creation, user_authorization,
                                                 feed_order_page, main_page, get_orders_of_a_specific_user):
        main_page.click_order_feed_button()
        user_order = str(get_orders_of_a_specific_user)
        history_of_orders = feed_order_page.get_order_history()

        assert user_order in history_of_orders

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Проверка, что после создания заказа, счётчик Выполнено за все время увеличился')
    def test_total_order_counter(self, main_page, feed_order_page, user_creation):
        main_page.click_order_feed_button()
        current_counter = int(feed_order_page.order_counter_displayed(OrderFeedPageLocators.TOTAL_ORDERS_COUNT))
        main_page.order_creation(user_creation)
        feed_order_page.refresh_feed_page()
        updated_counter = int(feed_order_page.order_counter_displayed(OrderFeedPageLocators.TOTAL_ORDERS_COUNT))

        assert updated_counter > current_counter

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Проверка, что после создания заказа, счётчик Выполнено за сегодня увеличился')
    def test_daily_order_counter(self, main_page, feed_order_page, user_creation):
        main_page.click_order_feed_button()
        current_counter = int(feed_order_page.order_counter_displayed(OrderFeedPageLocators.TODAY_ORDERS_COUNT))
        main_page.order_creation(user_creation)
        feed_order_page.refresh_feed_page()
        updated_counter = int(feed_order_page.order_counter_displayed(OrderFeedPageLocators.TODAY_ORDERS_COUNT))

        assert updated_counter > current_counter

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('Проверка, что появляется номер заказа в разделе В работе, после оформления заказа')
    def test_order_number_appears_in_progress(self, main_page, feed_order_page, user_creation, user_authorization,
                                              new_order_creation, get_orders_of_a_specific_user):
        main_page.click_order_feed_button()
        orders_in_progress = feed_order_page.get_orders_in_progress()
        user_order = str(new_order_creation)

        assert user_order in orders_in_progress
