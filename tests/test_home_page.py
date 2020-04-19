from pageObjects.home_page import HomePage
from utilities.Base import BaseClass

class TestHomePage(BaseClass):

    def test_cookie(self):
        homepage = HomePage(self.driver) #self.driver is the class variable inherited from BaseClass, which gets it
                                            #from fixture
        element = bool(homepage.get_cookie_banner_displayed())
        assert element == True
        cookie_confirm_btn = homepage.get_accept_btn()
        cookie_confirm_btn.click()

    def test_select_stats(self):
        homepage = HomePage(self.driver)
        element = homepage.get_stats_link()
        assert bool(element) == True
        self.hover_element(homepage.get_stats_link())

    def test_select_stats_guru(self):
        homepage = HomePage(self.driver)
        element = homepage.get_statsguru_link()
        assert bool(element) == True
        self.hover_element(element)
        homepage.get_statsguru_link().click()
