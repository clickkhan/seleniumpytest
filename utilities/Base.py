from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pageObjects.home_page import HomePage

@pytest.mark.usefixtures("setup")
class BaseClass:

    def hover_element(self, element):
        #homepage = HomePage(self.driver)
        action = ActionChains(self.driver)
        #action = ActionChains(driver)
        action.move_to_element(element).perform()