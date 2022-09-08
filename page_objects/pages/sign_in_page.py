from page_objects.locators import SignInPageLocators


class SignInPage:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.email = self.webdriver_obj.find_element(*SignInPageLocators.Email)
        self.password = self.webdriver_obj.find_element(*SignInPageLocators.Password)
        self.signinbutton = self.webdriver_obj.find_element(*SignInPageLocators.SignInButton)

