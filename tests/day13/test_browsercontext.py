"""
browser ->  context -> page

context will always be like the browser session behavior so it is irrespective of what browser windows do

in previous test cases we only used page skipping browser and context so by default browser and context were created
but now we are going to work with multiple pages 

multiple pages need multiple contexts because they should not share the cookies, local storage, cache etc..


Browser Context is an isolated session within a browser instance
If a page opens another page, e.g. with a window.open call, the popup will belong to the parent page's browser context.
All Pages within the same browser context share storage (cookies, local storage, cache).

Context API
BrowserContext objects expose powerful APIs to control and configure the isolated session.

browser can have multiple contexts

Basic Example: 
browser = sync_playwright().start()
context1 = browser.new_context()
context2 = browser.new_context()

page1 = context1.new_page()
page2 = context1.new_page()
page3 = context2.new_page()

browser.close()

in selenium swtiching is used between the pages or windows by using handles
but in playwright we use browser contexts

"""

from playwright.sync_api import Page, expect, Locator, Dialog, Browser,Playwright

def test_browsercontext_single_context_single_browser(playwright: Playwright):  
   chromium_browser =  playwright.chromium.launch(headless=False)  # custom browser instance, have to add headless manually as the instance of the browser is custom so it doesn't run with in a standard headed mode 
   context_1 = chromium_browser.new_context()   #custom context
   page1 = context_1.new_page()    #custom page
   page2 = context_1.new_page() 

   page1.goto("https://google.com")
   page1.wait_for_timeout(3000)
   expect(page1).to_have_title("Google")


   page2.goto("https://facebook.com")
   page2.wait_for_timeout(3000)
   expect(page2).to_have_title("Facebook")

   page1.close()   # closes the page 1 tab
   page2.close()   # closes the page 2 tab
   context_1.close() # closes the context 
   chromium_browser.close()   # closes the browser

# note that the above approach creates 1 browser 1 context and 2 pages in it so these are like 2 tabs 

def test_browsercontext_multiple_context_multiple_browser(playwright: Playwright):  
   chromium_browser =  playwright.chromium.launch(headless=False)  # custom browser instance, have to add headless manually as the instance of the browser is custom so it doesn't run with in a standard headed mode 
   context_1 = chromium_browser.new_context()   #custom context
   context_2 = chromium_browser.new_context()   #custom context
   page1 = context_1.new_page()    #custom page
   page2 = context_2.new_page() 

   page1.goto("https://google.com")
   page1.wait_for_timeout(3000)
   expect(page1).to_have_title("Google")


   page2.goto("https://facebook.com")
   page2.wait_for_timeout(3000)
   expect(page2).to_have_title("Facebook")

   page1.close()   
   page2.close()   
   context_1.close() 
   context_2.close() 
   chromium_browser.close()   

# this above approach will create 1 browser 2 contexts and 2 pages that are seperate pages of the same browser 




   

   


