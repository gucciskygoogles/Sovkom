import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from make_data import DataFromTable

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    return browser

@pytest.fixture()
def url():
    p = DataFromTable()
    url = p.get_value(1)
    return url
