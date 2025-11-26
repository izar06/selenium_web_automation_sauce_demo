from locators.checkout_overview import LocatorCheckoutOverview
from selenium.webdriver.common.by import By
from tests.conftest import capture_screenshot
import allure


class CheckoutOverview:
    def __init__(self, setup):
        self.setup = setup
    
    def get_title_payment_information(self):
        with allure.step("Halaman Payment Information"):
            title = self.setup.find_element(By.XPATH, LocatorCheckoutOverview.title_payment_information).text
            capture_screenshot(self.setup, "Validasi Halaman Payment Information 1")
            return title
    
    def get_title_page_checkout_overview(self):
        with allure.step("Halaman Payment Information"):
            title = self.setup.find_element(By.XPATH, LocatorCheckoutOverview.title_checkout_overview).text
            capture_screenshot(self.setup, "Validasi Halaman Payment Information 2")
            return title
    
    def click_btn_finish(self):
        with allure.step("Click Button Finish"):
            self.setup.find_element(By.ID, LocatorCheckoutOverview.btn_finish).click()
            capture_screenshot(self.setup, "Checkout Berhasil")
        