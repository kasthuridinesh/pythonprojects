import pytest


@pytest.fixture
def input_value():
    from selenium import webdriver
    import time
    from webdriver_manager.core import driver
    import logindata
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    return