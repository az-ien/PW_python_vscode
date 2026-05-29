from datetime import datetime
from datetime import date
from playwright.sync_api import Page, expect, Locator


def test_take_screenshot(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # take full page screenshot 
    page.screenshot(path=f'screenshots/homepage_{timestamp}.png' , full_page=True) 

    #take screenshot of specific element
    product = page.locator(".product-grid.home-page-product-grid")
    product.screenshot(path=f'screenshots/product_{timestamp}.png')


def test_trace_creation(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    #start tracing
    page.context.tracing.start(screenshots=True, snapshots=True)

    #actions
    product =page.locator("img[title='Show details for 14.1-inch Laptop']")
    product.click()

    #stop tracing and save trace file
    page.context.tracing.stop(path="trace/trace.zip")

    #open the zip file using the command in terminal
    # run this command in terminal: playwright show-trace 
    # open that file in browser 
    # this is very useful for debugging 