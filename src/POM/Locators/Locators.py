class Locators:
    # Date Parse Objects
    date_textBox_xpath = "//input[@class='form-control']"
    date_submitButton_xpath = "//*[@class='btn btn-default']"
    parsed_dateResult_xpath = "//div[@class='col-md-6']/div[1]"

    # Test_Config
    Test_URL = "https://vast-dawn-73245.herokuapp.com/"
    valid_date_regex = r"([A-Z])([a-z])([a-z]) ([A-Z])([a-z])([a-z]) ([0-2]\d|[3][0-1]) (\d{4}) (\d{2}):(\d{2}):(\d{2}) GMT\+(\d{4})"
