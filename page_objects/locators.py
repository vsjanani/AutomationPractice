from selenium.webdriver.common.by import By


class HomePageLocators:
    DressesOption = (By.LINK_TEXT, "DRESSES")
    DressesList = (By.XPATH, '//div[@id= "block_top_menu"]/ul/li[2]/ul/li')
    SummerDress = (By.XPATH, '//div[@id= "block_top_menu"]/ul/li[2]/ul/li[3]')


class SummerDressPageLocators:
    PrintedChiffonDress = (By.XPATH, '//ul[contains(@class, "product_list")] //a[@title = "Printed Chiffon Dress"]')
    MoreInPrintedChiffonDress = (By.XPATH, '//a[@title="Printed Chiffon Dress"]/parent::h5/following-sibling::div[2]/a[2]')


class AddToCartPageLocators:
    AddToCart = (By.CSS_SELECTOR, "#add_to_cart")


class ProceedToCheckoutLocators:
    AddToCartSuccess = (By.XPATH, "//div[@id='layer_cart']/div/div/h2")
    ProceedToCheckout = (By.CSS_SELECTOR, "[title = 'Proceed to checkout']")


class ShoppingCartSummaryLocators:
    TotalProduct = (By.ID, "total_product")
    TotalWrapping = (By.ID, "total_wrapping")
    TotalShipping = (By.ID, "total_shipping")
    TotalDiscount = (By.ID, "total_discount")
    TotalPriceWithoutTax = (By.ID, "total_price_without_tax")
    TotalTax = (By.ID, "total_tax")
    TotalPrice = (By.ID, "total_price_container")