from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#@pytest.mark.usefixtures("setup")
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

    # def confirmCookieBanner(self):
    #     self.wait.until(EC.presence_of_element_located((By.ID, "onetrust-banner-sdk")))
    #     cookie_banner = self.driver.find_element_by_id("onetrust-accept-btn-handler")
    #     cookie_banner.click()
    #
    # def selectStatsGuru(self):
    #     action = ActionChains(self.driver)
    #     nav_bar = self.driver.find_element_by_id("global-nav")
    #     self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Stats")))
    #     stats_menu = nav_bar.find_element_by_link_text("Stats")
    #     action.move_to_element(stats_menu).perform()
    #     self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Statsguru")))
    #     statsguru = self.driver.find_element_by_link_text("Statsguru")
    #     action.move_to_element(statsguru).perform()
    #     statsguru.click()

# if __name__ == "__main__":
#     homepage = HomePage()
#     homepage.confirmCookieBanner()
#     homepage.selectStatsGuru
