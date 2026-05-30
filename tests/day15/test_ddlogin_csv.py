import pytest
from playwright.sync_api import sync_playwright, Page, Locator, expect
import csv


login_test_data = []


# first open file then read the json file 
csvfile = open("testdata\data.csv", newline = '', encoding = 'utf-8') 
reader = csv.DictReader(csvfile)
for row in reader:
    login_test_data.append(row)





@pytest.mark.parametrize("email,password,expected_result", [ ("" + d["email"] + "", "" + d["password"] + "", "" + d["expected_result"] + "") for d in login_test_data])
def test_login_dd_csv(page:Page,email,password,expected_result):
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

