import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()

@pytest.mark.first

def test_google_web(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert driver.title == "Google"
    assert driver.current_url == url

@pytest.mark.second

def test_github_web(driver):
    url = "https://github.com/"
    driver.get(url)
    assert "GitHub" in driver.title  # "GitHub" содержится в заголовке
    assert driver.current_url == url
