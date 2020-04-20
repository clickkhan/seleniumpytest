from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class StatsGuruPage:

    cookie_confirm_btn = (By.CSS_SELECTOR, "button.cookie-continue")
    input_text_box = (By.CSS_SELECTOR, 'input[class="guruInput"]')
    search_btn = (By.CSS_SELECTOR, 'input[class="guruButton"]')
    player_btn = (By.CSS_SELECTOR, 'li[id="player"]')
    stats_links = (By.CSS_SELECTOR, 'a[class="statsLinks"]')
    opposition_team_dropdown = (By.CSS_SELECTOR, 'select[name="opposition"]')
    venue_label = (By.CSS_SELECTOR, 'label[class="guruCheckboxLabel"]')
    host_country_dropdown = (By.CSS_SELECTOR, 'select[name="host"]')
    ground_dropdown = (By.CSS_SELECTOR, 'select[name="ground"]')
    seasons_dropdown = (By.CSS_SELECTOR, 'select[name="season"]')
    view_format_label = (By.CSS_SELECTOR, 'label[class="guruRadioLabel"]')
    submit_btn = (By.CSS_SELECTOR, 'input[value="Submit query"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def get_cookie_visibility(self):
        return self.wait.until(EC.element_to_be_clickable(StatsGuruPage.cookie_confirm_btn))

    def confirm_cookie(self):
        self.wait.until(EC.presence_of_element_located(StatsGuruPage.cookie_confirm_btn)).click()

    def confirm_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def get_text_box(self):
        return self.wait.until(EC.presence_of_element_located(StatsGuruPage.input_text_box))
        #return self.driver.find_element(*StatsGuruPage.input_text_box)

    def get_search_btn(self):
        return self.driver.find_element(*StatsGuruPage.search_btn)

    def get_player_btn(self):
        return self.driver.find_element(*StatsGuruPage.player_btn)

    def get_stats_links(self):
        #links = self.driver.find_elements(*StatsGuruPage.stats_links)
        for link in self.driver.find_elements(*StatsGuruPage.stats_links):
            if link.text == "Test matches player":
                return link

    def select_venue(self):
        #venues = self.wait.until(EC.presence_of_all_elements_located(StatsGuruPage.venue_check_box))
        venues = self.driver.find_elements(*StatsGuruPage.venue_label)
        for venue in venues:
            print(venue.text)
            if venue.text == "away (home of opposition)":
                return venue

    def submit_query(self):
        return self.driver.find_element(*StatsGuruPage.submit_btn)
