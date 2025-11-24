from selenium.webdriver.common.by import By 
from locators.dashboard import LocatorDashboard
from tests.conftest import capture_screenshot
import allure
class Dashboard:
    def __init__(self, setup):
        self.setup = setup
        
    def validation_dashboard(self):
        with allure.step("Halaman Dashboard"):
            validation = self.setup.find_element(By.XPATH, LocatorDashboard.text_swag_labs).text
            capture_screenshot(self.setup, "Dashboard")
            return validation
    
    def show_detail_sauce_labs_backpack(self):
        with allure.step("Detail Sauce Labs Backpack"):
            self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_backpack).click()
            capture_screenshot(self.setup, "Sauce Labs Backpack")
    
    def show_detail_sauce_labs_bike_light(self):
        with allure.step("Detail Sauce Labs Bike Light"):
            self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_bike_light).click()
            capture_screenshot(self.setup, "Sauce Labs Bike Light")
            
    def show_detail_sauce_labs_bolt_tshirt(self):
        with allure.step("Detail Sauce Labs Bolt Tshirt"):
            self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_bolt_tshirt).click()
            capture_screenshot(self.setup, "Sauce Labs Bolt Tshirt")
            
    def show_detail_sauce_labs_fleece_jacket(self):
        with allure.step("Detail Sauce Labs Fleece Jacket"):
            self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_fleece_jacket).click()
            capture_screenshot(self.setup, "Sauce Labs Fleece Jacket")
            
    def show_detail_sauce_labs_onesia(self):
        with allure.step("Detail Sauce Labs Onesia"):
            self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_sauce_labs_onesia).click()
            capture_screenshot(self.setup, "Sauce Labs Onesia")
            
    def show_detail_tshirt_red(self):
        with allure.step("Detail Tshirt Red"):
            self.setup.find_element(By.XPATH, LocatorDashboard.show_detail_tshirt_red).click()
            capture_screenshot(self.setup, "Tshirt Red")
    
    def validation_detail_items(self):
        validation = self.setup.find_element(By.XPATH, LocatorDashboard.back_to_products).text
        return validation
    
    def click_cart(self):
        with allure.step("Halaman Cart"):
            self.setup.find_element(By.XPATH, LocatorDashboard.cart).click()
            capture_screenshot(self.setup, "Cart")
            
    def add_to_cart_Sauce_Labs_Backpack(self):
        with allure.step("Add to Cart Item Sauce Labs Backpack"):
            self.setup.find_element(By.XPATH, LocatorDashboard.add_to_cart_Sauce_Labs_Backpack).click()
            capture_screenshot(self.setup, "Berhasil Add to Cart")
    
    def add_to_cart_Sauce_Labs_Bike_Light(self):
        with allure.step("Add to Cart Item Sauce Labs Bike Light"):
            self.setup.find_element(By.XPATH, LocatorDashboard.add_to_cart_Sauce_Labs_Bike_Light).click()
            capture_screenshot(self.setup, "Berhasil Add to Cart")
    
    def add_to_cart_Sauce_Labs_Bolt_TShirt(self):
        with allure.step("Add to Cart Item Sauce Labs Bolt Tshirt"):
            self.setup.find_element(By.XPATH, LocatorDashboard.add_to_cart_Sauce_Labs_Bolt_TShirt).click()
            capture_screenshot(self.setup, "Berhasil Add to Cart")
            
    def add_to_cart_Sauce_Labs_Fleece_Jacket(self):
        with allure.step("Add to Cart Item Sauce Labs Fleece Jacket"):
            self.setup.find_element(By.XPATH, LocatorDashboard.add_to_cart_Sauce_Labs_Fleece_Jacket).click()
            capture_screenshot(self.setup, "Berhasil Add to Cart")
    
    def add_to_cart_Sauce_Labs_Onesie(self):
        with allure.step("Add to Cart Item Sauce Labs Onesie"):
            self.setup.find_element(By.XPATH, LocatorDashboard.add_to_cart_Sauce_Labs_Onesie).click()
            capture_screenshot(self.setup, "Berhasil Add to Cart")
    
    def add_to_cart_Test_allTheThings_TShirt(self):
        with allure.step("Add to Cart Item Test All The Things Tshirt"):
            self.setup.find_element(By.XPATH, LocatorDashboard.add_to_cart_Test_allTheThings_TShirt).click()
            capture_screenshot(self.setup, "Berhasil Add to Cart")

    def add_all_product(self):
        with allure.step("Add All Product"):
            products = self.setup.find_elements(By.XPATH, LocatorDashboard.add_to_cart)
            for product in products:
                product.click()
            capture_screenshot(self.setup, "Berhasil Add to Cart")
        
    def get_all_name_item_by_filter_Z_to_A(self):
        item_name = self.setup.find_elements(By.XPATH, LocatorDashboard.text_detail_items)
        results = []
        for names in item_name:
            text = names.text
            results.append(text)
        return results
    
    def get_all_price_item_by_filter_low_to_high(self):
        price_item = self.setup.find_elements(By.XPATH, LocatorDashboard.price_item)
        results = []
        for price in price_item:
            get_price = price.text
            results.append(get_price)
            
        return results
    
    def click_filter(self):
        with allure.step("Click Fitur Filter"):
            self.setup.find_element(By.XPATH, LocatorDashboard.filter).click()
            capture_screenshot(self.setup, "Fitur Filter Berhasil Muncul")
    
    def filter_A_to_Z(self):
        with allure.step("Filter A to Z"):
            self.setup.find_element(By.XPATH, LocatorDashboard.option_filter_A_to_Z).click()
            capture_screenshot(self.setup, "Filter Berhasil")
    
    def filter_Z_to_A(self):
        with allure.step("Filter Z to A"):
            self.setup.find_element(By.XPATH, LocatorDashboard.option_filter_Z_to_A).click()
            capture_screenshot(self.setup, "Filter Berhasil")
            
    def filter_low_to_high(self):
        with allure.step("Filter Low to High"):
            self.setup.find_element(By.XPATH, LocatorDashboard.option_filter_low_to_high).click()
            capture_screenshot(self.setup, "Filter Berhasil")
            
    def filter_high_to_low(self):
        with allure.step("Filter High to Low"):
            self.setup.find_element(By.XPATH, LocatorDashboard.option_filter_high_to_low).click()
            capture_screenshot(self.setup, "Filter Berhasil")
            
    def validation_cart(self):
        validation_cart = self.setup.find_element(By.XPATH, LocatorDashboard.validation_cart).text
        return validation_cart