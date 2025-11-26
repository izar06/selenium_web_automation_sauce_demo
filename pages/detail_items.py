from selenium.webdriver.common.by import By 
from locators.detail_item import DetailItem
from tests.conftest import capture_screenshot
import allure

class Detail:
    def __init__(self, setup):
        self.setup = setup
    
    def add_to_cart(self):
        with allure.step("Menambahkan Barang Ke Keranjang"):
            self.setup.find_element(By.XPATH, DetailItem.add_to_cart).click()
            capture_screenshot(self.setup, "Add to Cart")
            
    def remove_item_cart(self):
        with allure.step("Menghapus Barang Dari Keranjang"):
            self.setup.find_element(By.XPATH, DetailItem.remove_item).click()
            capture_screenshot(self.setup, "Remove Item Cart")
    
    def validation(self):
        validation = self.setup.find_element(By.XPATH, DetailItem.validation_add_to_cart).text
        return validation