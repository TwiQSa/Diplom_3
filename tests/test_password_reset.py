from data import UserData, PageUrls
import allure


class TestRecoveryPage:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Проверка успешности перехода на страницу восстановления по URL и наличии формы восстановления')
    def test_password_recovery_button(self, main_page, recovery_page, login_page):
        main_page.click_personal_account_button_to_login_on_main_page()
        login_page.click_on_recovery_button()

        assert (recovery_page.recovery_form_displayed() and
                recovery_page.get_current_url() == PageUrls.PASSWORD_RECOVERY_URL)

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('''Проверка, что при вводе почты и клике по кнопке "Восстановить",
        переходим на страницу восстановления, где есть элемент кнопка "Сохранить"''')
    def test_input_email_and_click_recovery_button(self, main_page, recovery_page, login_page):
        user_data = UserData().user_data_generator_for_tests()
        main_page.click_personal_account_button_to_login_on_main_page()
        login_page.click_on_recovery_button()
        recovery_page.enter_email_address(user_data['email'])
        recovery_page.click_on_recovery_button()

        assert (recovery_page.save_password_button_is_visible() and
                recovery_page.get_current_url() == PageUrls.RESET_PASSWORD_PAGE_URL)

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Проверка, что при нажатии на поле пароля оно подсвечивается и становится активным')
    def test_password_field_glowing_when_active(self, main_page, login_page, recovery_page):
        user_data = UserData().user_data_generator_for_tests()
        main_page.click_personal_account_button_to_login_on_main_page()
        login_page.click_on_recovery_button()
        recovery_page.enter_email_address(user_data.get('email'))
        recovery_page.click_on_recovery_button()

        assert recovery_page.password_field_is_active(user_data.get('password'))
