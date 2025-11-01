from selenium.webdriver.common.by import By 
from locators.dashboard import LocatorDashboard
class Dashboard:
    def __init__(self, setup):
        self.setup = setup
        
    def validation_dashboard(self):
        validation = self.setup.find_element(By.XPATH, LocatorDashboard.text_swag_labs).text
        return validation
    
    def show_detail_sauce_labs_backpack(self):
        self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_backpack).click()
    
    def show_detail_sauce_labs_bike_light(self):
        self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_bike_light).click()
    
    def show_detail_sauce_labs_bolt_tshirt(self):
        self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_bolt_tshirt).click()
    
    def show_detail_sauce_labs_fleece_jacket(self):
        self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_fleece_jacket).click()
        
    def show_detail_sauce_labs_onesia(self):
        self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_onesia).click()
    
    def show_detail_tshirt_red(self):
        self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_tshirt_red).click()
    
    def validation_detail_items(self):
        validation = self.setup.find_element(By.XPATH, LocatorDashboard.back_to_products).text
        return validation