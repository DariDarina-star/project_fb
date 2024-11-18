from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    first_name = (By.CSS_SELECTOR, "#u_0_8_oh")
    last_name = (By.CSS_SELECTOR, "#u_0_a_O6")
    email = (By.CSS_SELECTOR, "#u_0_h_Ch")
    password = (By.CSS_SELECTOR, "#password_step_input")
    female_radio_button = (By.CSS_SELECTOR, "#sex")
    year = (By.CSS_SELECTOR, "#year")
    year_twenty_five = (By.CSS_SELECTOR, "#year > option:nth-child(20)")
    sign_up_button = (By.CSS_SELECTOR, "#u_0_n_De")

    continue_button = (By.CSS_SELECTOR, "#scrollview > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x1qjc9v5.x78zum5.xl56j7k.x193iq5w.x1t2pt76 > div > div > div.x14lw9ws.xh8yej3 > div > div > div > div > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x2lah0s.x193iq5w.x5ib6vp.xc73u3c.xw7yly9.x1yztbdb.xzboxd6.x14l7nz5 > div > div > div:nth-child(2) > div > div > div > div > div.x6s0dn4.x78zum5.xl56j7k.x1608yet.xljgi0e.x1e0frkt > div > span > span")