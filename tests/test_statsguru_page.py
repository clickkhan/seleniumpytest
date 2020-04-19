from pageObjects.statsguru_page import StatsGuruPage
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pytest

@pytest.fixture(scope = "class")
#@pytest.fixture(scope = "function")
def setup(request):
    chrome_driver = "C:\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver)
    #self.wait = WebDriverWait(self.driver, 10)
    driver.get("https://stats.espncricinfo.com/ci/engine/stats/index.html")
    driver.maximize_window()
    #return driver
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.usefixtures("setup")
class TestStatsGuruPage:

    # def test_confirm_cookie(self):
    #     statsguru = StatsGuruPage(self.driver)
    #     cookie_banner = statsguru.cookie_visible()
    #     assert bool(cookie_banner) == True
        #statsguru.confirm_cookie().click()
        #assert bool(cookie_confirmed) == True

    def test_player_input(self):
        statsguru = StatsGuruPage(self.driver)
        text_input = statsguru.input_player_name()
        text_input.click()
        text_input.send_keys("Younis Khan")