from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from src.POM.Files.Inputs import csvReader
import unittest
from src.POM.Pages.DateParsePage import DateParsePage
from src.POM.Locators.Locators import Locators
import HtmlTestRunner
import time
import re
import pandas


class DateParserTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_parseDate(self):
        driver = self.driver
        driver.get(Locators.Test_URL)
        print("Test URL: " + Locators.Test_URL)
        delay = 15  # seconds

        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, Locators.date_textBox_xpath)))
            print()
            "Page is ready!"
        except TimeoutException:
            print()
            "Loading took too much time!"

        assert "Propine Date Parser" in driver.title

        parseDate = DateParsePage(driver)

        input_parameters = csvReader()
        csv_len = len(input_parameters)
        for date in range(csv_len):
            parseDate.enter_date(input_parameters[date])
            time.sleep(3)
            parseDate.click_submit()
            parser_response = parseDate.check_result()
            print("INPUT:\t" + str(input_parameters[date]) + " || " + "OUTPUT:\t" + str(parser_response))
            print("\n")

            if re.search(Locators.valid_date_regex, parser_response):
                assert True
            elif parser_response.__eq__("Invalid input date/Parsing failed"):
                print("\n")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
