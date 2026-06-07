from playwright.sync_api import Page, expect  # Page is the type hint for the Playwright browser tab object; expect is used for assertions


# POM class — groups all interactions for the Google homepage in one place
class GooglePage:

    URL = "https://www.google.com/"  # class-level constant — defined once here, reused in all methods

    def __init__(self, page: Page) -> None:  # constructor — called automatically when GooglePage(page) is created in conftest.py
        self.page = page  # stores the Playwright page object so all methods below can use it

    def navigate(self) -> None:  # opens the Google URL in the browser
        self.page.goto(self.URL)  # self.URL refers to the class constant above — avoids hardcoding the URL in multiple places

    def get_title(self) -> str:  # returns the current page title as a string — used in the test for printing
        return self.page.title()  # calls Playwright's built-in title() method on the browser tab

    def assert_title(self) -> None:  # assertion lives here in the POM — the test file never needs to import expect directly
        expect(self.page).to_have_title("Google")  # verifies the page title matches — fails the test if it doesn't
