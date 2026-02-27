import pytest
from playwright.sync_api import Page, expect


def test_xpath_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    # relative xpath
    logo = page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()

    #xpath with contains function in xpath not code :P
    computerproducts = page.locator("//h2[@class='product-title']//a[contains(@href,'computer')]")
    productcount = computerproducts.count() # counts from 1 not from 0 so not like an index
    print("Number of computer products: ", productcount)
    expect(computerproducts).to_have_count(4)

    #capture the first product in from the 4 computer products
    firstcomputerproduct = computerproducts.first
    print("First computer product: ", firstcomputerproduct.text_content())

    #capture the 2nd product
    secondcomputerproduct = computerproducts.nth(2)
    print("Second computer product: ", secondcomputerproduct.text_content())

    #capture the last product
    lastcomputerproduct = computerproducts.last
    print("Last computer product: ", lastcomputerproduct.text_content())

    # captures the text of all the computer products and stores it in a list
    product_titles= computerproducts.all_text_contents()
    print("All computer product titles: ")
    for i in product_titles:
        print(i)

    # grab only the products which have the word "build" in them
    buildcomputerproducts = page.locator("//h2[@class='product-title']//a[contains(@href,'/build')]")
    expect(buildcomputerproducts).to_have_count(3)

    # xpath with text() -- this the text without the text attribute but has text in the html element
    registerlink = page.locator("//a[text()='Register']")
    expect(registerlink).to_be_visible()

    #xpath with last function to capture the last product in a list of elements
    lastelement= page.locator("//div[@class='column follow-us']//li[5]")
    print("Last element in the follow us section: ", lastelement.text_content())

    #handle dynamic elements
    page.goto("https://testautomationpractice.blogspot.com/")

    # xpaths
    #//button[text()='START' or text()='STOP']
    #//button[@name='start' or @name='stop']
    #//button[contains(@name,'st')]

    #css selector
    #button[name='start'], button[name='stop']
    #button[name^='st'] -- starts with st
    #button[name$='op'] -- ends with op

    
    for i in range(5):
        page.locator("//button[text()='START' or text()='STOP']").click()
        page.wait_for_timeout(2000)



      

