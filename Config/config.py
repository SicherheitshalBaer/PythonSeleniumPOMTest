from dataclasses import dataclass


@dataclass
class Data:
    CHROME_EXECUTABLE_PATH = "C:/Users/jreimers/PycharmProjects/TestAutomation_POM/drivers/chromedriver.exe"


@dataclass
class Properties:
    username = "WhoAmI"
    password = "Whattever"
    Base_URL = "https://google.com"
