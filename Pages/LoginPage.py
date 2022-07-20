from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from Locators.locators import LoginPageLocators as LPL
from Config.config import Data
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    user = LPL.element_username_by_name
    pw = LPL.element_password_by_name
    login = LPL.element_LoginButton_by_class

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Data.Base_URL)

    def login(self, user, pw):