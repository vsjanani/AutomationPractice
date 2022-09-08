import time

from selenium import webdriver

from page_objects.locators import HomePageLocators, SummerDressPageLocators, AddToCartPageLocators, \
    ProceedToCheckoutLocators
from page_objects.pages.summary_page import ShoppingCartSummaryPage


class HomePage:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.DressesOption = self.webdriver_obj.find_element(*HomePageLocators.DressesOption)
        self.DressesList = self.webdriver_obj.find_elements(*HomePageLocators.DressesList)
        self.SummerDress = self.webdriver_obj.find_element(*HomePageLocators.SummerDress)

    def click_summer_dress(self):
        self.SummerDress.click()
        summerdresspage_obj = SummerDressPage(self.webdriver_obj)
        return summerdresspage_obj


class SummerDressPage:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.PrintedChiffonDress = self.webdriver_obj.find_element(*SummerDressPageLocators.PrintedChiffonDress)
        self.MoreInPrintedChiffonDress = self.webdriver_obj.find_element(*SummerDressPageLocators.MoreInPrintedChiffonDress)

    def click_more_in_printedchiffondress(self):
        self.MoreInPrintedChiffonDress.click()
        add_to_cart_obj = AddToCart(self.webdriver_obj)
        return add_to_cart_obj


class AddToCart:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.AddToCart = self.webdriver_obj.find_element(*AddToCartPageLocators.AddToCart)

    def click_add_to_cart(self):
        self.AddToCart.click()
        time.sleep(5)
        proceedtocheckoutpage_obj = ProceedToCheckoutPage(self.webdriver_obj)
        return proceedtocheckoutpage_obj


class ProceedToCheckoutPage:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.AddToCartSuccess = self.webdriver_obj.find_element(*ProceedToCheckoutLocators.AddToCartSuccess)
        self.ProceedToCheckout = self.webdriver_obj.find_element(*ProceedToCheckoutLocators.ProceedToCheckout)

    def click_proceed_to_checkout(self):
        self.ProceedToCheckout.click()
        summarypage_obj = ShoppingCartSummaryPage(self.webdriver_obj)
        return summarypage_obj


