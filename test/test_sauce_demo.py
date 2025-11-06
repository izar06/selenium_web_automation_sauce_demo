from pages.page_login import Login
from pages.page_dashboard import Dashboard
from pages.page_cart import Cart
from data.data import Data
from pages.detail_items import Detail
import pytest

# def test_login_positive(setup):
#     login = Login(setup)
#     dashboard = Dashboard(setup)
#     login.input_username("standard_user")
#     login.input_password("secret_sauce")
#     login.click_login_button()
#     validation_text = dashboard.validation_dashboard()
#     print(validation_text)
#     assert validation_text == "Swag Labs"

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
    
def test_add_to_cart(setup):
    login = Login(setup)
    dashboard = Dashboard(setup)
    cart = Cart(setup)
    # detail = Detail(setup)
    login.input_username("standard_user")
    login.input_password("secret_sauce")
    login.click_login_button()
    dashboard.add_all_product()
    dashboard.click_cart()
    title = cart.get_name_title()
    print(title)
    # validation = dashboard.validation_cart()
    
    assert ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)'] == title
    # detail.add_to_cart()
    # validation = detail.validation()
    # print(validation)
    # assert "1" in validation
    
