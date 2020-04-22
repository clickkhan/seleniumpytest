from pageObjects.statsguru_page import StatsGuruPage
from selenium import webdriver
import pytest
from utilities.Base import BaseClass
import time

@pytest.fixture(scope = "class")
#@pytest.fixture(scope = "function")
def setup(request):
    chrome_driver = "C:\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver)
    driver.get("https://stats.espncricinfo.com/ci/engine/stats/index.html")
    driver.maximize_window()
    #return driver
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.usefixtures("setup")
class TestStatsGuruPage(BaseClass):

    def test_player_input(self):
        log = self.getlogger()
        statsguru = StatsGuruPage(self.driver)
        #self.driver.implicitly_wait(15)
        text_input = statsguru.get_text_box()
        text_input.click()
        text_input.clear()
        assert text_input.get_attribute("value") == "", "Text Box was not empty."
        text_input.send_keys("Younis Khan")
        statsguru.get_search_btn().click()
        time.sleep(5)
        statsguru.confirm_cookie()
        #statsguru.confirm_alert()
        statsguru.get_player_btn().click()
        statsguru.get_stats_links().click()

    def test_stats_query(self):
        lst = []
        log = self.getlogger()
        statsguru = StatsGuruPage(self.driver)
        self.select_dropdown_element(self.driver, statsguru.opposition_team_dropdown, "India").click()
        #log.info("Here is the label: ", self.select_checkbox(self.driver, statsguru.venue_label, "away (home of opposition)"))
        statsguru.select_venue().click()
        self.select_dropdown_element(self.driver, statsguru.ground_dropdown, "all grounds").click()
        self.select_dropdown_element(self.driver, statsguru.host_country_dropdown, "India").click()
        self.select_dropdown_element(self.driver, statsguru.seasons_dropdown, "all seasons").click()
        self.select_radiobtn(self.driver, statsguru.view_format_label, "Batting formats").click()
        statsguru.submit_query().click()
        log.info(statsguru.career_avg_table(statsguru.career_avg_head, statsguru.career_avg_title_rows))
        log.info(statsguru.career_avg_table(statsguru.career_avg_unfiltered_data, statsguru.career_avg_data_rows))
        lst.append(tuple(statsguru.career_avg_table(statsguru.career_avg_head, statsguru.career_avg_title_rows)))
        lst.append(tuple(statsguru.career_avg_table(statsguru.career_avg_unfiltered_data, statsguru.career_avg_data_rows)))
        lst.append(tuple(statsguru.career_avg_table(statsguru.career_avg_filtered_data, statsguru.career_avg_data_rows)))
        self.write_excel_sheet(lst)
