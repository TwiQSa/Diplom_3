from data import PageUrls
import allure


class TestMainPage:

    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Проверка, что происходит переход к конструктору, если кликнуть на Конструктор')
    def test_move_to_constructor(self, main_page):
        main_page.click_personal_account_button_to_login_on_main_page()
        main_page.click_construction_button()

        assert main_page.check_constructor_section() and main_page.get_current_url() == PageUrls.MAIN_PAGE_URL
#
    @allure.title('Переход по клику на «Лента заказов»')
    @allure.description('Проверка, что происходит переход к Ленте заказов, если кликнуть на «Лента заказов»')
    def test_move_to_order_feed(self, main_page):
        main_page.click_order_feed_button()

        assert main_page.check_order_feed_section() and main_page.get_current_url() == PageUrls.ORDER_FEED_URL

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Проверка, что после клика на ингредиент, появляется окно с деталями этого ингредиента')
    def test_bun_details_window_appeared(self, main_page):
        main_page.click_bun()

        assert main_page.check_bun_details()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @allure.description('Проверка, что после появления окна с деталями ингредиента, окно закрывается по крестику')
    def test_bun_details_window_is_closed(self, main_page):
        main_page.click_bun()
        main_page.close_bun_details_window_icon()

        assert main_page.check_bun_details_window_is_closed()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('Проверка, что счётчик ингридиента увеличивается при добавлении в заказ')
    def test_ingredient_counter_increases(self, main_page):
        main_page.add_ingredient_to_basket()

        assert int(main_page.get_number_of_ingredients_from_counter_in_order()) > 0

#
    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Проверка, что будучи залогиненным можно оформить заказ')
    def test_order_creation_by_authorized_user(self, main_page, user_creation, user_authorization, new_order_creation):
        main_page.click_construction_button()
        created_order_number = new_order_creation
        main_page.click_create_order_button()

        assert main_page.check_order_form_is_displayed()
