from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class StatsGuruPage:

    cookie_confirm_btn = (By.CSS_SELECTOR, "button.cookie-continue")
    player_name_input = (By.CSS_SELECTOR, "input.guruInput")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def cookie_visible(self):
        return self.wait.until(EC.element_to_be_clickable(StatsGuruPage.cookie_confirm_btn))

    def confirm_cookie(self):
        return self.wait.until(EC.presence_of_element_located(StatsGuruPage.cookie_confirm_btn))


    def input_player_name(self):
        return self.wait.until(EC.presence_of_element_located(StatsGuruPage.player_name_input))
        #return self.driver.find_element(*StatsGuruPage.player_name_input)
