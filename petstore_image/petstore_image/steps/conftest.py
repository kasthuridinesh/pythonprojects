import pytest
from selenium import webdriver


@pytest.fixture(scope="session", params=['chrome'], autouse=True)
def browser(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')

    if request.param == 'chrome':
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.maximize_window()

    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()

    if request.param == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()

    yield driver
    driver.close()
