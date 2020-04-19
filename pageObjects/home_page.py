from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:

    cookie_banner = (By.ID, "onetrust-banner-sdk")
    cookie_accept_btn = (By.ID, "onetrust-accept-btn-handler")
    header_bar = (By.ID, "global-nav")
    stats_link = (By.LINK_TEXT, "Stats")
    stats_guru_link = (By.LINK_TEXT, "Statsguru")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def get_cookie_banner_displayed(self):
        return self.wait.until(EC.presence_of_element_located(HomePage.cookie_banner))

    def get_cookie_banner_not_displayed(self):
        banner = self.wait.until(EC.presence_of_element_located(HomePage.cookie_banner))
        return banner.is_displayed()

    def get_accept_btn(self):
        return self.driver.find_element(*HomePage.cookie_accept_btn)

    def get_navigation_bar(self):
        return self.driver.find_element(*HomePage.header_bar)

    def get_stats_link(self):
        return self.wait.until(EC.presence_of_element_located(HomePage.stats_link))

    def get_statsguru_link(self):
        return self.wait.until(EC.presence_of_element_located(HomePage.stats_guru_link))
