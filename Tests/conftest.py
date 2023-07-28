from selenium import webdriver
import pytest
from Config.config import TestData


@pytest.fixture(params=["chrome"], scope="function")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "edge":
        web_driver = webdriver.Edge()
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()