import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config.config import Data


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param =="chrome":
        options = Options()
        options.add_argument("user-data-dir=C:\\Users\\jreimers\\PycharmProjects\\TestAutomation_POM\\chrome_options")
        webDriver = webdriver.Chrome(executable_path=Data.CHROME_EXECUTABLE_PATH, chrome_options=options)
    request.cls.driver = webDriver
    yield
    webDriver.close()
    webDriver.quit()
#
# @pytest.fixture(scope='session')
# def whatever():
