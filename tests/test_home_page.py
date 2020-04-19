import pytest
from pageObjects.home_page import HomePage
from utilities.Base import BaseClass

class TestHomePage(BaseClass):
    #homepage = HomePage(self.driver)
    # def __init__(self, driver):
    #     #self.driver = driver
    #     self.homepage = HomePage(self.driver)

    def test_cookie(self):
        homepage = HomePage(self.driver)
        #homepage = HomePage(setup)
        element = bool(homepage.get_cookie_banner_displayed())
        assert element == True
        cookie_confirm_btn = homepage.get_accept_btn()
        cookie_confirm_btn.click()
        #print("Here is the print", homepage.get_cookie_banner_not_displayed())
        #assert homepage.get_cookie_banner_not_displayed() == False

    def test_select_stats(self):
        homepage = HomePage(self.driver)
        #homepage = HomePage(setup)
        element = homepage.get_stats_link()
        assert bool(element) == True
        #self.hover_element(homepage.get_stats_link())
        self.hover_element(homepage.get_stats_link())

    def test_select_stats_guru(self):
        homepage = HomePage(self.driver)
        #homepage = HomePage(setup)
        element = homepage.get_statsguru_link()
        assert bool(element) == True
        self.hover_element(element)
        homepage.get_statsguru_link().click()







#if __name__ == "__main__":
      #testone = TestOne()
      #testone.test_stats()
#     homepage = HomePage()
#     homepage.confirmCookieBanner()
#     homepage.selectStatsGuru()






