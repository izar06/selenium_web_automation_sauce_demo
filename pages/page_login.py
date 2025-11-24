from locators.login import LocatorLogin
from selenium.webdriver.common.by import By
from tests.conftest import capture_screenshot
import allure
class Login:
    def __init__(self, setup):
        self.setup = setup

    def input_username(self, username):
        with allure.step("Masukkan Username"):
            self.setup.find_element(By.ID, LocatorLogin.user_name).send_keys(username)
            capture_screenshot(self.setup, "Username")

    def input_password(self, password):
        with allure.step("Masukkan Password"):
            self.setup.find_element(By.NAME, LocatorLogin.password).send_keys(password)
            capture_screenshot(self.setup, "Password")

    def click_login_button(self):
        with allure.step("Click Button Login"):
            self.setup.find_element(By.XPATH, LocatorLogin.btn_login).click()
            capture_screenshot(self.setup, "Login")
        
    def validation_error_required_username(self):
        validation = self.setup.find_element(By.XPATH, LocatorLogin.msg_error_required_username).text
        return validation
    
    def validation_error_required_password(self):
        validation = self.setup.find_element(By.XPATH, LocatorLogin.msg_error_required_password).text
        return validation
    
    def validation_error_wrong_username_and_password(self):
        validation = self.setup.find_element(By.XPATH, LocatorLogin.msg_error_wrong_password_username).text
        return validation
        