import pytest

from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)

