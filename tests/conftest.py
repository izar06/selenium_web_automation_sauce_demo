from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from utils.notifier import send_report_to_telegram
import pytest
import allure
import subprocess



def capture_screenshot(driver, name="Screenshoot"):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
    
@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--disable-features=LocalNetworkAccessPolicies")
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    capture_screenshot(driver, "Berhasil Buka Browser")
    yield driver
    capture_screenshot(driver)
    driver.quit()




# def pytest_sessionfinish(session, exitstatus):
#     print("📤 Kirim report ke Telegram...")
#     send_report_to_telegram()