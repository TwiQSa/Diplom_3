from data import PageUrls
import allure


class TestPersonalProfilePage:

    @allure.title('Переход по клику на «Личный кабинет»')
    @allure.description('Проверка, что удалось перейти в личный кабинет')
    def test_click_to_move_to_personal_page(self, main_page, personal_profile_page, user_creation, user_authorization):
        main_page.click_personal_account_button()

        assert (personal_profile_page.check_personal_profile_visible() and
                personal_profile_page.get_current_url() == PageUrls.PROFILE_PAGE_URL)

    @allure.title('Переход в раздел «История заказов»')
    @allure.description('Проверка, что страница истории заказов открывается')
    def test_click_to_move_to_order_history_page(self, main_page, personal_profile_page, user_creation,
                                                 user_authorization):
        main_page.click_personal_account_button()
        personal_profile_page.click_order_history_personal_page()

        assert (personal_profile_page.check_order_history_form() and
                personal_profile_page.get_current_url() == PageUrls.ORDER_HISTORY_PAGE_URL)

    @allure.title('Выход из аккаунта')
    @allure.description('Проверка, что можно выйти из аккаунта')
    def test_log_out_from_personal_page(self, main_page, login_page, personal_profile_page, user_creation,
                                        user_authorization):
        main_page.click_personal_account_button()
        personal_profile_page.logout_from_account()

        assert (login_page.authorization_form_is_on_login_page() and
                login_page.get_current_url() == PageUrls.LOGIN_PAGE_URL)
