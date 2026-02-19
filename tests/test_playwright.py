from playwright.sync_api import Page, expect

# Setup: python -m pip install -r requirements.txt
# Run tests: pytest tests/test_playwright.py


def test_verifypageURL(page: Page):
    page.goto("https://www.google.com")
    expect(page).to_have_url("https://www.google.com/")
