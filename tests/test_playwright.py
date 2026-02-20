from playwright.sync_api import Page, expect


# Setup: python -m pip install -r requirements.txt
# Note: Ensure that Playwright browsers are installed by running: playwright install
# Run tests: pytest tests/test_playwright.py
# to run in headed mode: pytest tests/test_playwright.py --headed
# to run only second test : pytest tests/test_playwright.py -k test_verifytitle 
# this file is a module 
# synchronous vs asynchronous, is sequential or concurrent execution of code statements.
# Synchronous code executes in a single thread, where each statement waits for the previous one to complete before executing. 
# Asynchronous code, on the other hand, allows multiple tasks to run concurrently 
# Async calls are handled by awaiting  promises to be fulfilled, which can be resolved or rejected based on the outcome of the asynchronous operation.
# async await for waiting till promise is fulfilled and used inside test function before that we need to declare async def and also need to use async version of playwright which is playwright.async_api
# IMP FOR TypeScript OR JavaScript
# playwright python supports both synchronous and asynchronous programming styles..recommedned synchronous style for simplicity and ease of use, especially for beginners.
# in API testing then asynchronous style can be beneficial for handling multiple requests concurrently, improving performance and efficiency.
# pytest tests/test_playwright.py -s -v --headed --browser firefox --browser chromium --browser webkit



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

