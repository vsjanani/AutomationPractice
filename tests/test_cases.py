import pytest
from behave.formatter import null
from selenium.webdriver.common.by import By

from data.expected import Expected
from page_objects.locators import SummerDressPageLocators, ProceedToCheckoutLocators
from page_objects.pages.home_page import HomePage, SummerDress
from utilities.reusable import Utilities
homepage_obj = None
add_to_cart_obj = None
proceed_to_checkout_obj = None


class TestShopping(Utilities):
    # @pytest.mark.skip
    def test_f2208_ap_url_title(self):
        assert(Expected.website_url == self.webdriver_obj.title)

    def test_f2208_ap_dressed_menu(self):
        global homepage_obj
        homepage_obj = HomePage(self.webdriver_obj)
        self.mouse_hover_to(homepage_obj.DressesOption)
        actual_dresses_list = []
        for each_dress_option in homepage_obj.DressesList:
            actual_dresses_list.append(each_dress_option.text)
        assert Expected.dresses_list == actual_dresses_list

    def test_f2208_ap_product_display(self):
        homepage_obj.SummerDress.click()
        assert (self.element_visible(SummerDressPageLocators.PrintedChiffonDress))

    def test_f2208_ap_product_description_display(self):
        global add_to_cart_obj
        summer_dress_obj = SummerDress(self.webdriver_obj)
        self.mouse_hover_to(summer_dress_obj.PrintedChiffonDress)
        print("check1")
        add_to_cart_obj = summer_dress_obj.click_more_in_printedchiffondress()
        print("check7")
        assert(Expected.product_title == self.webdriver_obj.title)
        print(self.webdriver_obj.title)

    def test_f2208_ap_add_to_cart(self):
        global proceed_to_checkout_obj
        print("check8")
        add_to_cart_obj.click_add_to_cart()
        print("check14")
        message = self.webdriver_obj.find_element((By.XPATH, "//h2[contains(text(), 'Product successfully added')]")).text
        add_to_cart_success = "Product successfully added to your shopping cart"
        assert(message in add_to_cart_success)
        self.webdriver_obj.find_element(By.CSS_SELECTOR, "[title = 'Proceed to checkout']").click()
        # self.alert_exists()
        # self.element_visible(ProceedToCheckoutLocators.AddToCartSuccess)
        # assert(Expected.add_to_cart_success == add_to_cart_obj.AddToCartSuccess.text)
        # print("check15")
        # proceed_to_checkout_obj.ProceedToCheckout.click()






