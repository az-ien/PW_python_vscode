import pytest  # required to use the @pytest.fixture decorator
from pages.google_page import GooglePage  # relative to this conftest.py location — no need for full `tests.day16.pages` path


@pytest.fixture  # tells pytest this function is a fixture — it can be injected into test functions as a parameter
def google_page(page):  # `page` is automatically provided by pytest-playwright — it opens a browser tab for us
    gp = GooglePage(page)  # create an instance of the POM, passing the playwright `page` object into it
    gp.navigate()  # call the navigate() method to open the URL before the test runs
    yield gp  # hand the POM instance to the test — code AFTER yield runs as teardown (none here)
    # pytest-playwright automatically closes the page and browser after the test — no manual cleanup needed
