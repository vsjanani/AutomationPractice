import pytest
from selenium import webdriver

from page_objects.pages import HomePage


@pytest.mark.usefixtures("begin_end")
class TestShopping:
    def test_f2208_ap_url_title(self):
        assert(self.webdriver_obj.title == "My Store")

    def test_f2208_ap_dressed_menu(self):
        homepage = HomePage(self.webdriverObj)
        print("start hovering")
        self.mouse_hover.move_to_element(homepage.DressesOption).perform()
        print("mousehovered")





