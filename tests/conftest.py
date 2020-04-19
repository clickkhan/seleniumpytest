import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope = "class")
#@pytest.fixture(scope = "function")
def setup(request):
    chrome_driver = "C:\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver)
    #self.wait = WebDriverWait(self.driver, 10)
    driver.get("https://www.espncricinfo.com")
    driver.maximize_window()
    #return driver
    request.cls.driver = driver
    yield
    driver.close()
