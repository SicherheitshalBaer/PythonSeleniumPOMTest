import pytest
from selenium import webdriver
from Config.config import Data

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param =="chrome":
        webDriver = webdriver.Chrome(executable_path=Data.CHROME_EXECUTABLE_PATH)
    request.cls.driver = webDriver
    yield
    webDriver.close()
    webDriver.quit()
