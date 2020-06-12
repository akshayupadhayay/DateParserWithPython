from src.POM.Locators.Locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DateParsePage:

    def __init__(self, driver):
        self.driver = driver

        self.date_textBox_xpath = Locators.date_textBox_xpath
        self.date_submitButton_xpath = Locators.date_submitButton_xpath
        self.parsed_dateResult_xpath = Locators.parsed_dateResult_xpath

    def enter_date(self, date):
        delay = 5  # seconds
        WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, Locators.date_textBox_xpath)))
        self.driver.find_element_by_xpath(self.date_textBox_xpath).click()
        self.driver.find_element_by_xpath(self.date_textBox_xpath).clear()
        self.driver.execute_script("document.querySelector(\"input[placeholder='date']\").value = '{0}'".format(date))

    def click_submit(self):
        self.driver.find_element_by_xpath(self.date_submitButton_xpath).send_keys(Keys.ENTER)

    def check_result(self) -> str:
        var = self.driver.find_element_by_xpath(self.parsed_dateResult_xpath).text
        print(var)
        return var
