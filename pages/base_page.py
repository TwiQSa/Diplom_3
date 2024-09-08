from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_element_to_be_clickable(self, locator, timeout=15):
        return WebDriverWait(self.browser, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator, timeout=15):
        return WebDriverWait(self.browser, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def click_after_visibility(self, locator, timeout=15):
        clickable_element = self.wait_for_element_to_be_visible(locator, timeout)
        clickable_element.click()

    def check_element(self, locator):
        self.wait_for_element_to_be_visible(locator)
        return self.browser.find_element(*locator)

    def drag_and_drop(self, element_first, element_second):
        ingredient = self.check_element(element_first)
        basket = self.check_element(element_second)
        drag_and_drop(self.browser, ingredient, basket)

    def get_current_url(self):
        return self.browser.current_url

    def input_text(self, locator, input_value, timeout=15):
        self.wait_for_element_to_be_clickable(locator, timeout)
        field = self.browser.find_element(*locator)
        field.send_keys(input_value)

    def retrieve_elements(self, locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))
        return self.browser.find_elements(*locator)

    def get_text_from_element(self, locator, timeout=15):
        element = self.wait_for_element_to_be_visible(locator, timeout)
        return element.text

    def click(self, locator):
        element = self.wait_for_element_to_be_visible(locator)
        self.browser.execute_script("arguments[0].click();", element)

    def element_is_absent(self, locator, timeout=5):
        WebDriverWait(self.browser, timeout).until(expected_conditions.invisibility_of_element_located(locator))
        return self.browser.find_element(*locator)
