from locators.registration_locators import RegistrationPageLocators


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = RegistrationPageLocators()

    def enter_first_name(self):
        self.driver.find_element(self.locators.first_name).send_keys("test_first_name")

    def enter_last_name(self):
        self.driver.find_element(self.locators.last_name).send_keys("test_last_name")

    def click_gender(self):
        self.driver.find_element(self.locators.female_radio_button).click()

    def enter_email(self):
        self.driver.find_element(self.locators.female_radio_button).click()

    def enter_password(self):
        self.driver.find_element(self.locators.email).send_keys("test242142@gmail.com")

    def click_sign_up(self):
        self.driver.find_element(self.locators.sign_up_button).click()
