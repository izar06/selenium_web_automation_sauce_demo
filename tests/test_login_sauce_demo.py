# from pages.page_login import Login
# from pages.page_dashboard import Dashboard
# from data.data import Data
# import pytest


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