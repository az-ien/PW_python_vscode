from playwright.sync_api import Page, expect

# to run test the terminal command that is used is "pytest tests/test_playwright.py"


def test_verifypageURL(page: Page):
    page.goto("https://www.google.com")
    expect(page).to_have_url("https://www.google.com/")
