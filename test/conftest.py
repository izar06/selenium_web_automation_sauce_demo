from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    # screenshoot = driver.get_screenshot_as_png()
    yield driver
    driver.quit()
