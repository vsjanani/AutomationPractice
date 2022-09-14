import inspect
import logging
import pytest
# from behave.formatter import null
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
explicit_wait = None

from page_objects.locators import SummerDressPageLocators


@pytest.mark.usefixtures("begin_end")
class Utilities:
    def element_visible(self, locator):
        global explicit_wait
        explicit_wait = WebDriverWait(self.webdriver_obj, 5)
        return explicit_wait.until(expected_conditions.visibility_of_element_located(locator))

    def alert_exists(self):
        try:
            explicit_wait.until(expected_conditions.alert_is_present())
            self.webdriver_obj.switch_to.alert.accept()
            print("alert accepted")

        except Exception as e:
            print("alert not found", e)

    def mouse_hover_to(self, locator):
        return self.mouse_hover.move_to_element(locator).perform()

    def logging(self):
        logObj = logging.getLogger(inspect.stack()[1][3])
        fileHandlerObj = logging.FileHandler("logfile.log")
        formatterObj = logging.Formatter("%(asctime)s, %(levelname)s, %(name)s, %(message)s")
        logObj.addHandler(fileHandlerObj)
        fileHandlerObj.setFormatter(formatterObj)
        logObj.setLevel(logging.DEBUG)
        return logObj

