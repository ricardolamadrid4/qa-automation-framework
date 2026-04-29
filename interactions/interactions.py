import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageInteractions:

    def __init__(self, context):
        self.driver = context.driver


    def click(self, locator, wait_time=0):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(locator)
            )

            element.click()

            if wait_time > 0:
                time.sleep(wait_time)

        except Exception as e:
            raise Exception(
                f"Could not click element {locator}. Error: {e}"
            )


    def enter_text(self, locator, text, wait_time=0):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(locator)
            )
            element.send_keys(text)

            if wait_time > 0:
                time.sleep(wait_time)

        except Exception as e:
            raise Exception(
                f"Could not enter text in {locator}. Error: {e}"
            )


    def get_text(self, locator, wait_time=5):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(
                    locator
                )
            )

            return element.text

        except Exception as e:
            raise Exception(
                f"Could not get text from element {locator}. "
                f"Error: {e}"
            )