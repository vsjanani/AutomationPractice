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


class SummerDress:
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
        proceed_to_checkout_obj = ProceedToCheckout(self.webdriver_obj)
        return proceed_to_checkout_obj


class ProceedToCheckout:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.AddToCartSuccess = self.webdriver_obj.find_element(*ProceedToCheckoutLocators.AddToCartSuccess)
        self.ProceedToCheckout = self.webdriver_obj.find_element(*ProceedToCheckoutLocators.ProceedToCheckout)

    def click_proceed_to_checkout(self):
        self.ProceedToCheckout.click()
        summary_obj = ShoppingCartSummaryPage(self.webdriver_obj)
        return summary_obj


