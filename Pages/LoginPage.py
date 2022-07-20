from Pages.BasePage import BasePage
from Locators.locators import LoginPageLocators as LPL
from Config.config import Data,Properties


class LoginPage(BasePage):

    USER = LPL.element_username_by_name
    PW = LPL.element_password_by_name
    LOGIN_BUTTON = LPL.element_LoginButton_by_class

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.driver.get(Properties.Base_URL)
        self.send_keys(self.USER, Properties.username)
        self.send_keys(self.PW, Properties.password)
        self.login(self.LOGIN_BUTTON)
