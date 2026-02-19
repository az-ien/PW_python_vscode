from playwright.sync_api import Page, expect

# Setup: python -m pip install -r requirements.txt
# Note: Ensure that Playwright browsers are installed by running: playwright install
# Run tests: pytest tests/test_playwright.py
# to run in headed mode: pytest tests/test_playwright.py --headed
# to run only second test : pytest tests/test_playwright.py -k test_verifytitle 
# this file is a module 


def test_verifypageURL(page: Page):
    page.goto("https://www.google.com")
    myurl=page.url
    print("URL of the page is: " + myurl)
    expect(page).to_have_url("https://www.google.com/")

def test_verifytitle(page: Page):
    page.goto("https://www.google.com")
    mytitle=page.title()
    print("Title of the page is: " + mytitle)
    expect(page).to_have_title("Google")       

