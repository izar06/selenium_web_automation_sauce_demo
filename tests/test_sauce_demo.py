from pages.page_login import Login
from pages.page_dashboard import Dashboard
from pages.page_cart import Cart
from data.data import Data
from pages.detail_items import Detail
from pages.page_checkout_information import CheckoutInformation
from pages.page_checkout_overview import CheckoutOverview
from pages.page_checkout_complete import CheckoutComplete
import pytest
import allure
from time import sleep

@allure.title("Test Login Positif Case")
def test_login_positive(setup):
    login = Login(setup)
    dashboard = Dashboard(setup)
    login.input_username("standard_user")
    login.input_password("secret_sauce")
    login.click_login_button()
    validation_text = dashboard.validation_dashboard()
    print(validation_text)
    assert validation_text == "Swag Labs"

# def test_login_field_username_kosong(setup):
#     login = Login(setup)
#     login.input_username("")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     validation_text = login.validation_error_required_username()
#     print(validation_text)
#     assert validation_text == "Epic sadface: Username is required"

# def test_login_field_password_kosong(setup):
#     login = Login(setup)
#     login.input_username("standard_user")
#     login.input_password("")
#     login.click_login_button()
#     validation_text = login.validation_error_required_password()
#     print(validation_text)
#     assert validation_text == "Epic sadface: Password is required"

# test_data_negative = Data.test_data_negative

# @pytest.mark.parametrize("username, password, expected_error", test_data_negative)
# def test_login_negative(setup, username, password, expected_error):
#     login = Login(setup)
#     login.input_username(username)
#     login.input_password(password)
#     login.click_login_button()
#     validation_text = login.validation_error_wrong_username_and_password()
#     print(validation_text)
#     assert validation_text == expected_error

# def test_show_detail_sauce_labs_backpack(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.show_detail_sauce_labs_backpack()
#     validation_text = (dashboard.validation_detail_items())
#     print(validation_text)
#     assert validation_text in ("Back to products", "Sauce Labs Backpack")

# def test_show_detail_sauce_labs_bike_light(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.show_detail_sauce_labs_bike_light()
#     validation_text = dashboard.validation_detail_items()
#     print(validation_text)
#     assert validation_text == "Back to products"

# def test_show_detail_sauce_labs_bolt_tshirt(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.show_detail_sauce_labs_bolt_tshirt()
#     validation_text = dashboard.validation_detail_items()
#     print(validation_text)
#     assert validation_text == "Back to products"

# def test_show_detail_sauce_labs_fleece_jacket(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.show_detail_sauce_labs_fleece_jacket()
#     validation_text = dashboard.validation_detail_items()
#     print(validation_text)
#     assert validation_text == "Back to products"

# def test_show_detail_sauce_labs_onesia(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.show_detail_sauce_labs_onesia()
#     validation_text = dashboard.validation_detail_items()
#     print(validation_text)
#     assert validation_text == "Back to products"

# def test_show_detail_tshirt_red(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.show_detail_tshirt_red()
#     validation_text = dashboard.validation_detail_items()
#     print(validation_text)
#     assert validation_text == "Back to products"

# def test_show_detail_tshirt_red(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.show_detail_tshirt_red()
#     validation_text = dashboard.validation_detail_items()
#     print(validation_text)
#     assert validation_text in ("Back to products")

# def test_add_to_cart(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     detail = Detail(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.show_detail_tshirt_red()
#     detail.add_to_cart()
#     validation = detail.validation()
#     print(validation)
#     assert "1" in validation

# def test_remove_cart(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     detail = Detail(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.show_detail_tshirt_red()
#     detail.add_to_cart()
#     detail.remove_item_cart()
#     validation = detail.validation()
#     print(validation)
#     assert "1" not in validation
    
# def test_add_to_cart_all_item(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     cart = Cart(setup)
#     detail = Detail(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.add_all_product()
#     dashboard.click_cart()
    
#     validation = detail.validation()
#     print(validation)
#     assert "6" in validation
    
#     title = cart.get_name_title()
#     print(title)
#     assert ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)'] == title
    

# def test_add_to_cart_item_Sauce_Labs_Backpack(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.add_to_cart_Sauce_Labs_Backpack()
    
#     validation = dashboard.validation_cart()
#     assert "1" in validation

# def test_add_to_cart_item_Sauce_Labs_Bike_Light(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.add_to_cart_Sauce_Labs_Bike_Light()
    
#     validation = dashboard.validation_cart()
#     assert "1" in validation
    
# def test_add_to_cart_item_Sauce_Labs_Bolt_TShirt(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.add_to_cart_Sauce_Labs_Bolt_TShirt()
    
#     validation = dashboard.validation_cart()
#     assert "1" in validation

# def test_add_to_cart_item_Sauce_Labs_Fleece_Jacket(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.add_to_cart_Sauce_Labs_Fleece_Jacket()
    
#     validation = dashboard.validation_cart()
#     assert "1" in validation

# def test_add_to_cart_item_Sauce_Labs_Onesie(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.add_to_cart_Sauce_Labs_Onesie()
    
#     validation = dashboard.validation_cart()
#     assert "1" in validation

# def test_add_to_cart_item_Test_allTheThings(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.add_to_cart_Test_allTheThings_TShirt()
    
#     validation = dashboard.validation_cart()
#     assert "1" in validation
    
# def test_filter_Z_to_A(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.click_filter()
#     dashboard.filter_Z_to_A()
#     validation = dashboard.get_all_name_item_by_filter_Z_to_A()
#     sorted_desc = sorted(validation, reverse=True)
#     print(validation)
    
#     assert sorted_desc == validation

# def test_filter_low_to_high(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.click_filter()
#     dashboard.filter_low_to_high()
#     validation = dashboard.get_all_price_item_by_filter_low_to_high()
#     sorted_desc = sorted(validation)
#     print(validation)
    
#     assert ['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99'] == validation

# def test_filter_high_to_low(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     dashboard.click_filter()
#     dashboard.filter_high_to_low()
#     validation = dashboard.get_all_price_item_by_filter_low_to_high()
#     print(validation)
    
#     assert ['$49.99', '$29.99', '$15.99', '$15.99', '$9.99', '$7.99'] == validation

def test_checkout(setup):
    login = Login(setup)
    dashboard = Dashboard(setup)
    cart = Cart(setup)
    checkout_information = CheckoutInformation(setup)
    checkout_overview = CheckoutOverview(setup)
    checkout_complete = CheckoutComplete(setup)
    login.input_username("standard_user")
    login.input_password("secret_sauce")
    login.click_login_button()
    dashboard.add_to_cart_Sauce_Labs_Backpack()
    dashboard.click_cart()
    cart.click_checkout()
    checkout_information.input_first_name("Izar")
    checkout_information.input_last_name("Anam")
    checkout_information.input_postal_code("160002")
    checkout_information.click_btn_continue()
    checkout_overview.click_btn_finish()
    # validation_title1 = checkout_overview.get_title_page_checkout_overview()
    # print(validation_title1)
    # assert "Checkout: Overview" == validation_title1
    
    # validation_title2 = checkout_overview.get_title_payment_information()
    # print(validation_title2)
    # assert "Payment Information:" == validation_title2
    
    validation_title = checkout_complete.get_title_checkout_complete()
    print(validation_title)
    assert "Checkout: Complete!" == validation_title
    
    validation_order_success = checkout_complete.get_title_order_success()
    print(validation_order_success)
    assert "Thank you for your order!" == validation_order_success



      
    
