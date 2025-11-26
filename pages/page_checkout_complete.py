from locators.checkout_complete import LocatorCheckoutComplete
from selenium.webdriver.common.by import By
from tests.conftest import capture_screenshot
import allure

class CheckoutComplete:
    def __init__(self, setup):
        self.setup = setup
        
    def get_title_checkout_complete(self):
        with allure.step("Halaman Checkout Complete"):
            title = self.setup.find_element(By.XPATH, LocatorCheckoutComplete.title_checkout_complete).text
            capture_screenshot(self.setup, "Validasi Halaman Checkout Complete 1")
            return title
    
    def get_title_order_success(self):
        with allure.step("Title Order Success"):
            order_success =  self.setup.find_element(By.XPATH, LocatorCheckoutComplete.order_success).text
            capture_screenshot(self.setup, "Validasi Halaman Checkout Complete 1")
            return order_success