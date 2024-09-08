from faker import Faker
import random


class PageUrls:
    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'
    ORDER_FEED_URL = 'https://stellarburgers.nomoreparties.site/feed'
    REGISTRATION_PAGE_URL = 'https://stellarburgers.nomoreparties.site/register'
    PROFILE_PAGE_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'
    RESET_PASSWORD_PAGE_URL = 'https://stellarburgers.nomoreparties.site/reset-password'
    PASSWORD_RECOVERY_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    ORDER_HISTORY_PAGE_URL = 'https://stellarburgers.nomoreparties.site/account/order-history'


class ApiEndpoints:
    USER_REGISTRATION_ENDPOINT = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    ORDER_CREATION_ENDPOINT = 'https://stellarburgers.nomoreparties.site/api/orders'
    USER_DELETION_ENDPOINT = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    ORDER_RETRIEVAL_ENDPOINT = 'https://stellarburgers.nomoreparties.site/api/orders'


class Ingredients:
    ingredients_for_order_creation = {"ingredients": ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa79"]}


class UserData:

    @staticmethod
    def user_data_generator_for_tests():
        faker_en = Faker('en_US')
        faker_ru = Faker('ru_RU')
        faker = random.choice([faker_en, faker_ru])

        data = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.first_name()
        }
        return data
