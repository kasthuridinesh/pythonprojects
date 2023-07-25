import pytest
from selenium.webdriver.edge import webdriver
from selenium import webdriver


@pytest.fixture(scope="session", params=['edge'], autouse=True)
def browser_setup(request):
    ''' Setting browser globally'''
    global driver
    # if request.param == 'chrome':
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()

    if request.param == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()

    yield driver
    driver.close()
