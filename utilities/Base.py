from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pageObjects.home_page import HomePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:

    def hover_element(self, element):
        #action = ActionChains(self.driver)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def select_dropdown_element(self, driver, element, text):
        wait = WebDriverWait(self.driver, 15)
        host_dropdown = Select(wait.until(EC.presence_of_element_located(element)))
        for option in host_dropdown.options:
            if option.text == text:
                return option

    def select_checkbox(self, driver, element, text):
        #venues = self.wait.until(EC.presence_of_all_elements_located(*element))
        venues = self.driver.find_elements(*element)
        for venue in venues:
            print(venue.text)
            if venue.text == "text":
                return venue

    def select_radiobtn(self, driver, element, text):
        view_formats = self.driver.find_elements(*element)
        for format in view_formats:
            print(format.text)
            if format.text == text:
                return format
