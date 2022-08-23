from selenium import webdriver

from page_objects.locators import HomePageLocators


class HomePage:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.DressesOption = self.webdriver_obj.find_element(*HomePageLocators.DressesOption)
        self.DressesList = self.webdriver_obj.find_elements(*HomePageLocators.DressesList)
        self.SummerDress = self.webdriver_obj.find_elements(*HomePageLocators.SummerDress)