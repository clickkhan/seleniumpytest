from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pageObjects.home_page import HomePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
import inspect
import openpyxl

@pytest.mark.usefixtures("setup")
class BaseClass:

    def hover_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def select_dropdown_element(self, driver, element, text):
        wait = WebDriverWait(self.driver, 25)
        host_dropdown = Select(wait.until(EC.presence_of_element_located(element)))
        for option in host_dropdown.options:
            if option.text == text:
                return option

    def select_checkbox(self, driver, element, text):
        #venues = self.wait.until(EC.presence_of_all_elements_located(*element))
        venues = self.driver.find_elements(*element)
        for venue in venues:
            if venue.text == "text":
                return venue

    def select_radiobtn(self, driver, element, text):
        view_formats = self.driver.find_elements(*element)
        for format in view_formats:
            if format.text == text:
                return format

    def getlogger(self):
        test_name = inspect.stack()[1][3]
        logger = logging.Logger(test_name)
        logger.setLevel(logging.DEBUG)
        filehandler = logging.FileHandler("file.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        return logger

    def write_excel_sheet(self, lst):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        row, col = 1, 1
        for item in lst:
            worksheet.append(item)
            col += 1
        workbook.save('Player Stats.xlsx')
        workbook.close()

