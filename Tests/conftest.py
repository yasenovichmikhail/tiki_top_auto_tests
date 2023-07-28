from selenium import webdriver
import pytest
import

from Config.config import TestData

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    elif request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()