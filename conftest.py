from selenium import webdriver
import pytest
import requests
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_reset_page import PasswordResetPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalPage
from data import UserData, Ingredients, PageUrls, ApiEndpoints


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(PageUrls.MAIN_PAGE_URL)
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(PageUrls.MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def user_creation():
    payload = UserData.user_data_generator_for_tests()
    response = requests.post(ApiEndpoints.USER_REGISTRATION_ENDPOINT, data=payload)
    yield payload, response
    token = response.json()['accessToken']
    header = {'Authorization': token}
    requests.delete(ApiEndpoints.USER_DELETION_ENDPOINT, headers=header)

@pytest.fixture
def user_authorization(driver, user_creation):
    user_data = user_creation[0]
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    main_page.click_personal_account_button_to_login_on_main_page()
    login_page.login_into_account(user_data['email'], user_data['password'])
    main_page.check_visibility_of_create_order_button()

@pytest.fixture
def new_order_creation(user_creation):
    token = user_creation[1].json()['accessToken']
    header = {'Authorization': token}
    ingredients = Ingredients.ingredients_for_order_creation
    response = requests.post(ApiEndpoints.ORDER_CREATION_ENDPOINT, headers=header, data=ingredients)
    return response.json()['order']['number']


@pytest.fixture
def get_orders_of_a_specific_user(user_creation):
    token = user_creation[1].json()['accessToken']
    header = {'Authorization': token}
    response = requests.get(ApiEndpoints.ORDER_RETRIEVAL_ENDPOINT, headers=header)
    return response.json()['orders'][0]['number']


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def recovery_page(driver):
    return PasswordResetPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def feed_order_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def personal_profile_page(driver):
    return PersonalPage(driver)
