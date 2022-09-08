import time
from data.expected import Expected
from page_objects.locators import SummerDressPageLocators
from page_objects.pages.home_page import HomePage
from page_objects.pages.sign_in_page import SignInPage
from utilities.reusable import Utilities
homepage_obj = None
add_to_cart_obj = None
proceedtocheckoutpage_obj = None
summerdresspage_obj = None
summarypage_obj = None


class TestShopping(Utilities):
    # @pytest.mark.skip
    def test_f2208_ap_url_title(self):
        assert self.webdriver_obj.title == Expected.website_url

    def test_f2208_ap_dressed_menu(self):
        global homepage_obj
        homepage_obj = HomePage(self.webdriver_obj)
        self.mouse_hover_to(homepage_obj.DressesOption)
        actual_dresses_list = []
        for each_dress_option in homepage_obj.DressesList:
            actual_dresses_list.append(each_dress_option.text)
        assert actual_dresses_list == Expected.dresses_list

    def test_f2208_ap_product_display(self):
        global summerdresspage_obj
        summerdresspage_obj = homepage_obj.click_summer_dress()
        assert self.element_visible(SummerDressPageLocators.PrintedChiffonDress)

    def test_f2208_ap_product_description_display(self):
        global add_to_cart_obj
        self.mouse_hover_to(summerdresspage_obj.PrintedChiffonDress)
        add_to_cart_obj = summerdresspage_obj.click_more_in_printedchiffondress()
        assert self.webdriver_obj.title == Expected.product_title

    def test_f2208_ap_add_to_cart(self):
        global proceedtocheckoutpage_obj
        proceedtocheckoutpage_obj = add_to_cart_obj.click_add_to_cart()
        time.sleep(5)
        assert(proceedtocheckoutpage_obj.AddToCartSuccess.text == Expected.add_to_cart_success)

    def test_f2208_ap_shopping_cart_summary(self):
        global summarypage_obj
        summarypage_obj = proceedtocheckoutpage_obj.click_proceed_to_checkout()
        summarypage_obj.expected_total_price_equal_to_actual_total_price()

    def test_f2208_ap_SignInPage(self):
        summarypage_obj.ProceedToCheckout.click()
        assert self.webdriver_obj.title == Expected.sign_in_title

    def test_f2208_ap_invalid_login(self, login_details):
        sign_in_obj = SignInPage(self.webdriver_obj)
        sign_in_obj.email.send_keys(login_details["email"])
        sign_in_obj.password.send_keys(login_details["password"])
        sign_in_obj.signinbutton.click()


