import pytest
from playwright.sync_api import sync_playwright, Page, Locator, expect


search_items =['Laptop','Phone','Camera',]


# pytest provides this parametrization as in playwright there is no direct method for this.
# in selenium there is @DataProvider and @Test in java
# in pytest @pytest.mark.parametrize is used for this
# and then the test also needs to parametrized with the data provider parameteres
# in this case item 

@pytest.mark.parametrize("item",search_items)
def test_searchitem(page : Page , item):

    print("Testing for item: ", item)
    page.goto("https://demowebshop.tricentis.com/")
    
    search_box =page.locator("#small-searchterms")
    search_box.fill(item)

    search_button =page.locator("input[type='submit']")
    search_button.click()

    page.wait_for_timeout(1000)

    first_result = page.locator("h2>a").nth(0)
    print("First result is: ", first_result.inner_text())
    expect(first_result).to_contain_text(item)







