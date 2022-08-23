from selenium.webdriver.common.by import By


class HomePageLocators:
    DressesOption = (By.LINK_TEXT, "DRESSES")
    DressesList = (By.XPATH, '//div[@id= "block_top_menu"]/ul/li[2]/ul/li')
    SummerDress = (By.XPATH, '//div[@id= "block_top_menu"]/ul/li[2]/ul/li[3]')



