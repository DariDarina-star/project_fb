from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


def test_facebook_login(driver):

    login_page = LoginPage(driver)

    login_page.click_on_sign_up_for_facebook()

    registration_page = RegistrationPage(driver)
    registration_page.enter_first_name()
    registration_page.enter_last_name()
    registration_page.click_gender()
    registration_page.enter_email()
    registration_page.enter_password()
    registration_page.click_sign_up()
