from playwright.sync_api import Page, expect, Locator, Dialog, Browser,Playwright

"""
In Playwright, a Context is the container that holds cookies and local storage. Therefore, when a page opens a popup, Playwright automatically puts that popup into the same Context as the parent page so it inherits the exact same session data.
When you call browser.new_context(), you are explicitly asking Playwright to create a completely brand-new, isolated incognito profile with zero cookies. That's why two contexts act like completely different users.
However, when a popup opens, it is just a new Page (tab/window) being spawned by an existing Page. Even if it pops up as a physically separate window on your computer screen, logically, it is just another tab living inside the same "incognito profile" (Context).

popups although open in new window but they still are treated like child of the parent page in terms of cookies and local storage.

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

    print("Main page url:",page.context.pages[0].url)
    print("URL of 1st popup:",page.context.pages[1].url)
    print("URL of 2nd popup:",page.context.pages[2].url)

    page1 = page.context.pages[1]
    page2 = page.context.pages[2]

    print("Page1 title:",page1.title())
    expect(page1).to_have_title("Selenium")
    page1.close()

    print("Page2 title:",page2.title())
    expect(page2).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
    page2.close()
 







    
