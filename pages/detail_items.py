from selenium.webdriver.common.by import By 
from locators.detail_item import DetailItem

class Detail:
    def __init__(self, setup):
        self.setup = setup
    
    def add_to_cart(self):
        self.setup.find_element(By.XPATH, DetailItem.add_to_cart).click()
    
    def remove_item_cart(self):
        self.setup.find_element(By.XPATH, DetailItem.remove_item).click()
    
    def validation(self):
        validation = self.setup.find_element(By.XPATH, DetailItem.validation_add_to_cart).text
        return validation