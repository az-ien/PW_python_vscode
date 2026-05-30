import pytest
from playwright.sync_api import sync_playwright, Page, Locator, expect



'''
test scenarios to run:

valid data --  successfull login  --  test passed
valid data  -- unsuccessfull login  -- test failed

invalid data -- unsuccessfull login  -- test passed
invalid data  -- successfull login  -- test failed


'''


login_test_data = [
    ("laura.taylor1234@example.com", "test123", "valid"),
    ("laura.taylor1234@example.com", "passs", "invalid"),
    ("lauraasd@example.com", "bnbnb", "invalid"),
    ("", "", "invalid")
]






@pytest.mark.parametrize("email,password,expected_result", login_test_data)
def test_login_dd(page:Page,email,password,expected_result):
    page.goto("https://demowebshop.tricentis.com/")

    login_link = page.locator("a:has-text('Log in')")
    login_link.click()
    page.wait_for_timeout(2000)
    
    page.locator("#Email").fill(email)
    page.locator("#Password").fill(password)

    login_button = page.locator(".button-1.login-button").click()
    page.wait_for_timeout(2000) 

    if expected_result == "valid":
        logout_link = page.locator("a:has-text('Log out')")
        expect(logout_link).to_be_visible()
        print("Login successfull")
    elif expected_result == "invalid":
        error_msg = page.locator("div.validation-summary-errors")
        expect(error_msg).to_be_visible()   
        print("Login failed")



