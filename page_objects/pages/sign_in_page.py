from page_objects.locators import SignInPageLocators


class SignInPage:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.email = self.webdriver_obj.find_element(*SignInPageLocators.Email)
        self.password = self.webdriver_obj.find_element(*SignInPageLocators.Password)
        self.signinbutton = self.webdriver_obj.find_element(*SignInPageLocators.SignInButton)


    def click_email_field(self):
        self.email.clear()
        return self.email

    def click_password_field(self):
        self.password.clear()
        return self.password

    def click_sign_in(self):
        self.signinbutton.click()
        auth_error_obj = AuthError(self.webdriver_obj)
        return auth_error_obj


class AuthError:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.AuthError = self.webdriver_obj.find_element(*SignInPageLocators.AuthError)