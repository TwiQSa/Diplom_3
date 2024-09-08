from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
    ORDER_FEED = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")
    ACCOUNT_LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    CONSTRUCTOR_SECTION = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    ORDER_FEED_SECTION = (By.XPATH, ".//div[contains(@class, 'OrderFeed_orderFeed')]")
    ORDER_FEED_FORM = (By.XPATH, ".//div[contains(@class, 'Modal_modal__container')]")
    BASKET_TOP_SECTION_ORDER = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    CRATOR_BUN = (By.XPATH, ".//img[@alt = 'Краторная булка N-200i']")
    INGREDIENT_BUN1 = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
    INGREDIENT_COUNTER_IN_ORDER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    ORDER_BASKET = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    ORDER_NUMBER_HEADING = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")
    CLOSE_ICON_BUTTON_IN_INGREDIENT_DETAILS = (By.XPATH, ".//button[contains(@class,'close')]")
    INGREDIENT_DETAILS_HEADER = (By.XPATH, ".//h2[text()= 'Детали ингредиента']")


class RecoveryPageLocators:
    EMAIL_RECOVERY_INPUT = (By.XPATH, ".//input[@name = 'name']")
    RECOVERY_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")
    NEW_PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Введите новый пароль']")
    EMAIL_CODE_INPUT = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    SAVE_PASSWORD_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    PASSWORD_RECOVERY_RECOVERY_PAGE = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")
    SHOW_PASSWORD_ICON = (By.XPATH, ".//div[contains(@class, 'input__icon input__icon-action')]")
    PASSWORD_INPUT_ACTIVE_GLOWS = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")


class AuthorizationPageLocators:
    AUTHORIZATION_FORM = (By.XPATH, ".//div[contains(@class, 'Auth_login')]")
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")
    REGISTER_BUTTON = (By.XPATH, ".//a[text() = 'Зарегистрироваться']")
    RECOVERY_BUTTON = (By.XPATH, ".//a[text() = 'Восстановить пароль']")


class OrderFeedPageLocators:
    ORDER_INFO_INSIDE_ORDER = (By.XPATH, ".//p[text()='Cостав']")
    ORDERS_FEED_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")
    IN_PROGRESS_ORDERS_COUNT = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
    ORDER_WINDOW_DETAIL = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]")
    ALL_ORDER_NUMBERS = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    TOTAL_ORDERS_COUNT = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_ORDERS_COUNT = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")


class PersonalPageLocators:
    PROFILE_FORM_PERSONAL_PAGE = (By.XPATH, ".//div[contains(@class, 'Account_account')]")
    PROFILE_SECTION_BUTTON = (By.XPATH, ".//a[text() = 'Профиль']")
    ORDER_HISTORY_PERSONAL_PAGE = (By.XPATH, ".//a[text() = 'История заказов']")
    ORDER_HISTORY_SECTION_FROM_PERSONAL_PAGE = (By.XPATH, ".//div[contains(@class, 'Account_contentBox')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    CANCEL_BUTTON_PERSONAL_PAGE = (By.XPATH, ".//button[text() = 'Отмена']")
    SAVE_BUTTON_PERSONAL_PAGE = (By.XPATH, ".//button[text() = 'Сохранить']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
