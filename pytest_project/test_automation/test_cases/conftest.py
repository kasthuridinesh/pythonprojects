from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture(scope="session", params=['chrome','edge'])
def browser_setup(request):
    global driver
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()

    if request.param == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()

    yield driver
    driver.close()