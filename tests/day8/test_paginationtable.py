from playwright.sync_api import sync_playwright, Page, expect
import pytest

# while loop becuase we dont know when to stop so stop on false condition
# for loop is when we know where we can stop


@pytest.mark.skip(reason="just wanted to skip this for fun")
def test_dynamic_paginationtable(page: Page):

    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    has_more_pages = True  # we are assuming that there are more pages to start with, we will check this condition in the loop and update it accordingly
    while has_more_pages:  #while loop becuase we dont know when to stop so stop on false condition
        
        #get all the rows in the table 
        tableRows = page.locator("table#example tbody tr").all()
        
        for row in tableRows:  #for loop is when we know where we can stop
            print("text of the row is:", row.inner_text())

        nextpagebutton = page.locator("button[aria-label='Next']")  #locator for the next page button
        # nextpagebuttonState = nextpagebutton.get_attribute("disabled")  #get the disabled attribute of the next page button, if it is disabled then there are no more pages to navigate
       
        nextpagebuttondisabled = page.locator("button[aria-label='Next'][aria-disabled='true']")  #locator for the next page button when it is disabled, if this locator is visible then there are no more pages to navigate
       
        if nextpagebuttondisabled.is_visible():  #if the next page button is disabled then there are no more pages to navigate, so we can stop the loop
            has_more_pages = False
        else:  #if the next page button is not disabled then there are more pages to navigate, so we can click on the next page button to navigate to the next page
            nextpagebutton.click()
            page.wait_for_timeout(2000)  #wait for 2 seconds to load the next page, you can use wait_for_selector() instead of wait_for_timeout() to wait for a specific element to be visible on the next page before proceeding with the loop
        
          

def test_filter_rows_in_paginationtable(page: Page):

    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    dropdown = page.locator("#dt-length-0") #locator for the dropdown to select the number of rows to display
    dropdown.select_option('25') #select the option to display 25 rows per page

    Rows = page.locator("table#example tbody tr")
    expect(Rows).to_have_count(25) #expect the number of rows to be 25 after selecting the option to display 25 rows per page   



def test_search_in_paginationtable(page: Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    searchbox = page.locator("input[type='search']") #locator for the search box
    searchbox.fill("software engineer") #fill the search box with the keyword to search
    page.wait_for_timeout(2000) #wait for 2 seconds to get the search results, you can use wait_for_selector() instead of wait_for_timeout() to wait for a specific element to be visible on the search results page before proceeding with the loop

    Rows = page.locator("table#example tbody tr") #locator for the rows in the table
    for row in Rows.all(): #iterate through all the rows in the table
        print("the found records are :", row.inner_text()) #print the text of each row, you can also add an assertion here to check if the text of the row contains the keyword to search
        expect(row).to_contain_text("Software Engineer") #expect the text of the row to contain the keyword to search, this will ensure that the search functionality is working as expected and only relevant records are being displayed in the table after performing the search operation
        
    
