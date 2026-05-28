from playwright.sync_api import Page, expect, Locator, Dialog, Browser,Playwright

"""
In Playwright, a Context is the container that holds cookies and local storage. Therefore, when a page opens a popup, Playwright automatically puts that popup into the same Context as the parent page so it inherits the exact same session data.
When you call browser.new_context(), you are explicitly asking Playwright to create a completely brand-new, isolated incognito profile with zero cookies. That's why two contexts act like completely different users.
However, when a popup opens, it is just a new Page (tab/window) being spawned by an existing Page. Even if it pops up as a physically separate window on your computer screen, logically, it is just another tab living inside the same "incognito profile" (Context).

popups although open in new window but they still are treated like child of the parent page in terms of cookies and local storage.


Selenium = reactive & manual
Playwright = event-driven & automatic

Playwright
Alert = Dialog
Popup = Page
Everything is a real object.


Browser
 └─ Context
     ├─ Page (main)
     ├─ Page (popup)
     └─ Page (new tab)
          └─ Dialog (alert)



Selenium
Alert = Alert
Popup / Tab / Page = same thing
You just switch, nothing is a separate object.

Driver
 └─ Current Window
     ├─ switchTo(window)
     └─ switchTo(alert)





"""

def test_handle_poopups(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)


    page.on("popup",lambda popup:popup.wait_for_load_state()) # this is the event handler before the event of click and popup launch happens
    page.locator("#PopUp").click()
    page.wait_for_timeout(5000)

    # now we need to switch to the popup for this we can use the page.context.pages() this will return a list of all the pages
    # this can be done using a for loop in the list and check if the page title is not the same as the main page title
    # the first page will be the main page the second page will be the popup

    all_popup = page.context.pages
    print("Total pages opened:",len(all_popup))

    # FIX: Do NOT rely on index positions (pages[1], pages[2]) to identify popups.
    # The order of pages in page.context.pages depends on which popup finishes loading first,
    # which is non-deterministic and varies between local runs and CI (GitHub Actions).
    # Instead, find each popup by its URL so the test is deterministic in any environment.

    playwright_page = next(p for p in all_popup if "playwright.dev" in p.url)
    selenium_page = next(p for p in all_popup if "selenium.dev" in p.url)

    print("Playwright page title:", playwright_page.title())
    expect(playwright_page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
    playwright_page.close()

    print("Selenium page title:", selenium_page.title())
    expect(selenium_page).to_have_title("Selenium")
    selenium_page.close()
 


# for authentication popups as this is a popup that is launched immediately after the page is loaded
# it has to be handeled like an event. the best way to handle the event is to pass the credentials in the context that is then used by the page 
# this is so that as soon as the page is loaded the authentication is done and the popup is not shown
# and the next assert on success message is done

def test_authpopup(playwright:Playwright):
    browser =playwright.chromium.launch(headless=True)
    context = browser.new_context(http_credentials={"username":"admin","password":"admin"})
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator(":text('Congratulations! You must have the proper credentials.')")).to_be_visible()
    page.wait_for_timeout(3000)


    




    
