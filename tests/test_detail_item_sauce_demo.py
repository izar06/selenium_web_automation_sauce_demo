# from pages.page_login import Login
# from pages.page_dashboard import Dashboard
# from pages.page_cart import Cart
# from data.data import Data
# from pages.detail_items import Detail
# import pytest





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