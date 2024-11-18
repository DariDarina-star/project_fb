from locators.login_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginPageLocators()

    def click_on_sign_up_for_facebook(self):
        self.driver.find_element(self.locators.sign_up_for_facebook).click()
