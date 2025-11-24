from locators.checkout_overview import LocatorCheckoutOverview
from selenium.webdriver.common.by import By



class CheckoutOverview:
    def __init__(self, setup):
        self.setup = setup
    
    def get_title_payment_information(self):
        title = self.setup.find_element(By.XPATH, LocatorCheckoutOverview.title_payment_information).text
        return title
    
    def get_title_page_checkout_overview(self):
        title = self.setup.find_element(By.XPATH, LocatorCheckoutOverview.title_checkout_overview).text
        return title
    
    def click_btn_finish(self):
        self.setup.find_element(By.ID, LocatorCheckoutOverview.btn_finish).click()