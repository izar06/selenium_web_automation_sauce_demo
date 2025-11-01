from locators.login import LocatorLogin
from selenium.webdriver.common.by import By 
class Login:
    def __init__(self, setup):
        self.setup = setup

    def input_username(self, username):
        self.setup.find_element(By.ID, LocatorLogin.user_name).send_keys(username)

    def input_password(self, password):
        self.setup.find_element(By.NAME, LocatorLogin.password).send_keys(password)

    def click_login_button(self):
        self.setup.find_element(By.XPATH, LocatorLogin.btn_login).click()
        
    def validation_error_required_username(self):
        validation = self.setup.find_element(By.XPATH, LocatorLogin.msg_error_required_username).text
        return validation
    
    def validation_error_required_password(self):
        validation = self.setup.find_element(By.XPATH, LocatorLogin.msg_error_required_password).text
        return validation
    
    def validation_error_wrong_username_and_password(self):
        validation = self.setup.find_element(By.XPATH, LocatorLogin.msg_error_wrong_password_username).text
        return validation
        