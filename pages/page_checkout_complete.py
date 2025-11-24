from locators.checkout_complete import LocatorCheckoutComplete
from selenium.webdriver.common.by import By


class CheckoutComplete:
    def __init__(self, setup):
        self.setup = setup
        
    def get_title_checkout_complete(self):
        title = self.setup.find_element(By.XPATH, LocatorCheckoutComplete.title_checkout_complete).text
        return title
    
    def get_title_order_success(self):
        order_success =  self.setup.find_element(By.XPATH, LocatorCheckoutComplete.order_success).text
        return order_success