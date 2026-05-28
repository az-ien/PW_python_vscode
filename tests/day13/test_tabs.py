from types import LambdaType
from playwright.sync_api import Page,expect,Playwright, Locator,Browser,Dialog


def test_opentabs(playwright:Playwright):
    custom_browser =playwright.chromium.launch(headless=True)
    custom_context = custom_browser.new_context()
    parent_page = custom_context.new_page()
    parent_page.goto("https://testautomationpractice.blogspot.com/")


    # REGISTER EVENT to open new tab
    custom_context.on("popup", lambda page:page.wait_for_load_state() )

    # click on open tab
    parent_page.locator("button:has-text('New Tab')").click()
    parent_page.wait_for_timeout(2000)

    #print number of pages
    print(len(custom_context.pages))

    #switch to child page
    child_page = custom_context.pages[1]
    child_page.wait_for_timeout(2000)

    #check the title of the child page
    expect(child_page).to_have_title("SDET-QA Blog")
    print(child_page.title())

    #close the child page
    child_page.close()

    #check the number of pages
    print(len(custom_context.pages))

    #switch back to parent page and check the title
    parent_page = custom_context.pages[0]
    parent_page.wait_for_timeout(2000)
    expect(parent_page).to_have_title("Automation Testing Practice")
    print(parent_page.title())
    
    #close the browser
    custom_browser.close()


    







    





    
