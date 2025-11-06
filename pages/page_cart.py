from locators.cart import LocatorCart
from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, setup):
        self.setup = setup
    
    
    def get_name_title(self):
        titles = self.setup.find_elements(By.XPATH, LocatorCart.title_item)
        result = []
        for i in titles:
            text = i.text
            print(f"Found item: {text}")
            result.append(text)
        
        return result