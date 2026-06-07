# `google_page` is injected by pytest from conftest.py — it is a GooglePage POM instance with the browser already open on Google



def test_googlemainpage(google_page):
    print("Title of the page is:", google_page.get_title())  # calls get_title() on the POM — no direct Playwright code needed here
    google_page.assert_title()  # assertion is handled inside the POM — this test has zero Playwright imports or knowledge
