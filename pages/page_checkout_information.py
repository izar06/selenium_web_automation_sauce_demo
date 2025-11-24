from locators.checkout_information import LocatorCheckoutInformation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import capture_screenshot
import allure

class CheckoutInformation:
    def __init__(self, setup):
        self.setup = setup
        
    
    def validation_title(self):
        with allure.step("Validation Halaman Checkout Information"):
            title = self.setup.find_element(By.XPATH, LocatorCheckoutInformation.title_page_checkout_information).text
            capture_screenshot(self.setup, "Halaman Checkout Information")
            return title
    
    def input_first_name(self, first_name):
        with allure.step("Masukkan First Name"):
            try:
                element = WebDriverWait(self.setup,10).until(EC.visibility_of_element_located((By.XPATH, LocatorCheckoutInformation.title_page_checkout_information))).text
                print(element)
                print("Element Muncul")
            except:
                print("Element Tidak Muncul")
            self.setup.find_element(By.ID, LocatorCheckoutInformation.first_name).send_keys(first_name)
            capture_screenshot(self.setup, "Berhasil Input First Name")
        
    def input_last_name(self, last_name):
        with allure.step("Masukkan Last Name"):
            self.setup.find_element(By.ID, LocatorCheckoutInformation.last_name).send_keys(last_name)
            capture_screenshot(self.setup, "Berhasil Input Last Name")
            
    def input_postal_code(self, postal_code):
        with allure.step("Masukkan Postal Code"):
            self.setup.find_element(By.ID, LocatorCheckoutInformation.postal_code).send_keys(postal_code)
            capture_screenshot(self.setup, "Berhasil Input Postal Code")
            
    def click_btn_continue(self):
        with allure.step("Click Button Continue"):
            self.setup.find_element(By.ID, LocatorCheckoutInformation.btn_continue).click()
            capture_screenshot(self.setup, "Berhasil Click Button")