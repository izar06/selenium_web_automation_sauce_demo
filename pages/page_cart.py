from locators.cart import LocatorCart
from locators.checkout_information import LocatorCheckoutInformation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import capture_screenshot
import allure

class Cart:
    def __init__(self, setup):
        self.setup = setup
    
    
    def get_name_title(self):
        with allure.step("Validation Halaman Cart"):
            titles = self.setup.find_elements(By.XPATH, LocatorCart.title_item)
            result = []
            for i in titles:
                text = i.text
                print(f"Found item: {text}")
                result.append(text)
            capture_screenshot(self.setup, "Halaman Cart")
            return result
    
    def click_checkout(self):
        with allure.step("Click Checkout"):
            self.setup.find_element(By.ID, LocatorCart.btn_checkout).click()
            try:
                element = WebDriverWait(self.setup,10).until(EC.visibility_of_element_located((By.XPATH, LocatorCheckoutInformation.title_page_checkout_information))).text
                print(element)
                print("Element Muncul")
                capture_screenshot(self.setup, "Click Checkout Berhasil")
            except:
                print("Element Tidak Muncul")
                
                