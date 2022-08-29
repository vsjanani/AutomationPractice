from selenium.webdriver.common.by import By


class HomePageLocators:
    DressesOption = (By.LINK_TEXT, "DRESSES")
    DressesList = (By.XPATH, '//div[@id= "block_top_menu"]/ul/li[2]/ul/li')
    SummerDress = (By.XPATH, '//div[@id= "block_top_menu"]/ul/li[2]/ul/li[3]')


class SummerDressPageLocators:
    PrintedChiffonDress = (By.LINK_TEXT, "Printed Chiffon Dress")
    MoreInPrintedChiffonDress = (By.XPATH, '//a[@title="Printed Chiffon Dress"]/parent::h5/following-sibling::div[2]/a[2]')


class AddToCartPageLocators:
    AddToCart = (By.CSS_SELECTOR, "#add_to_cart")


class ProceedToCheckoutLocators:
    AddToCartSuccess = (By.XPATH, "//h2[contains(text(), 'Product successfully added')]")
    ProceedToCheckout = (By.CSS_SELECTOR, "[title = 'Proceed to checkout']")
