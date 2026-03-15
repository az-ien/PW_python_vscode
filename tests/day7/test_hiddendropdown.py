import  pytest
from playwright.sync_api import sync_playwright,Page,expect

#inner_text()   --  only the text is brought back
#text_content()  -- spaces and lines and hidden characters next to the text are also brought back , need to use strip
#all_inner_texts()   -- same as above with for loop
#all_text_contents()  -- same as above with for loop but strip the text
#.all()    --will get list of locators with index

def test_hiddendropdown(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    #login
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()

    #goto PIM in site
    page.get_by_text("PIM").click()

    #click on job title dropdown
    page.locator("div.oxd-select-text").nth(2).click() #open the options of the 3rd dropdown 

    #to enable the hidden drop down enable the selectors hub debugger, then click on the dropdown 
    #this will cause the drop down to open and freeze then in elements in the chrome tools hover over the 
    #dropdownoptions and then those will be open and stay open and click on the individual elements 
    
    page.wait_for_timeout(3000)
    dropdown_options = page.locator("div[role='listbox']>div>span")
    count = dropdown_options.count()
    print("the number of options in this dropdown are", count)

    expect(dropdown_options).to_have_count(count)

    page.wait_for_timeout(2000)

    # get all the text of the options from the dropdown 
    dropdown_options_text = dropdown_options.all_inner_texts()
    print("all options text are:",dropdown_options_text)

    #print all options using for loop, this is ranged not in the list of the elements that are returned above 
    for i in range (count):
        print("looped dropdown text is :", dropdown_options.nth(i).text_content())
        text = dropdown_options.nth(i).inner_text()
        if text == 'Automaton Tester':
            dropdown_options.nth(i).click()
            break

    page.wait_for_timeout(2000)


    

            
def test_method_comparison(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    products = page.locator(".product-title")

    #1) inner_text() vs text_content()
    print("inner text brings ----> :",products.nth(1).inner_text())
    print("text content brings ----> :",products.nth(1).text_content())

    count =products.count()
    for i in range(count):
        print("inner text brings ----> :",products.nth(i).inner_text())

    for i in range(count):
        print("text content brings ----> :",products.nth(i).text_content())

    #2) all_inner_texts() vs all_text_contents()
    print("inner text brings ----> :",products.all_inner_texts())
    print("text content brings ----> :",products.all_text_contents())
    text_content_product = products.all_text_contents()
    stripped_names =[text.strip() for text in text_content_product]
    print("text content strip brings ----> :",stripped_names)



    #3).all()

    product_locators = products.all()
    print("get first product:",product_locators[0])

    for product_loc in product_locators:
        print("each locator text --->", product_loc.inner_text())


















