import time
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
        assert(self.webdriver_obj.title == Expected.website_url)

    def test_f2208_ap_dressed_menu(self):
        global homepage_obj
        homepage_obj = HomePage(self.webdriver_obj)
        self.mouse_hover_to(homepage_obj.DressesOption)
        actual_dresses_list = []
        for each_dress_option in homepage_obj.DressesList:
            actual_dresses_list.append(each_dress_option.text)
        assert actual_dresses_list == Expected.dresses_list

    def test_f2208_ap_product_display(self):
        homepage_obj.SummerDress.click()
        assert (self.element_visible(SummerDressPageLocators.PrintedChiffonDress))

    def test_f2208_ap_product_description_display(self):
        global add_to_cart_obj
        summer_dress_obj = SummerDress(self.webdriver_obj)
        self.mouse_hover_to(summer_dress_obj.PrintedChiffonDress)
        add_to_cart_obj = summer_dress_obj.click_more_in_printedchiffondress()
        assert(self.webdriver_obj.title == Expected.product_title)
        # print(self.webdriver_obj.title)

    def test_f2208_ap_add_to_cart(self):
        global proceed_to_checkout_obj
        proceed_to_checkout_obj = add_to_cart_obj.click_add_to_cart()
        time.sleep(3)
        assert(proceed_to_checkout_obj.AddToCartSuccess.text == Expected.add_to_cart_success)

    def test_f2208_ap_shopping_cart_summary(self):
        summary_obj = proceed_to_checkout_obj.click_proceed_to_checkout()
        summary_obj.expected_total_price_equal_to_actual_total_price()


