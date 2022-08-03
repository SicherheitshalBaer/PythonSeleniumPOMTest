import pytest
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


@pytest.mark.usefixtures("init_driver")
class Test_Login(BaseTest):

    #@pytest.mark.usefixtures(["whatever", "whatever2"])
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()



