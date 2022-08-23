import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_objects.pages import HomePage
homepage_obj = None


@pytest.mark.usefixtures("begin_end")
class TestShopping:
    def test_f2208_ap_url_title(self):
        assert(self.webdriver_obj.title == "My Store")

    def test_f2208_ap_dressed_menu(self):
        global homepage_obj
        homepage_obj = HomePage(self.webdriver_obj)
        self.mouse_hover.move_to_element(homepage_obj.DressesOption).perform()
        each_dress_type = set["CASUAL DRESSES", "EVENING DRESSES", "SUMMER DRESSES"]
        for each_dress_option in homepage_obj.DressesList:
            print(each_dress_option.text)


    def test_f2208_ap_product_display(self):
        homepage_obj.SummerDress.click()




