from playwright.sync_api import sync_playwright, Page, expect

# when working with tables: first pick rows then pick columns and then pick the cell value.
# basically following the html in which the table is made
# why make your own logic to traverse the table when you can use the html structure to traverse the table and get the data you want.

def test_static_web_table(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 1) visibility of the table
    table = page.locator("table[name='BookTable']")
    expect(table).to_be_visible()


    # 2) count of rows in the table
    tableRow = page.locator("table[name='BookTable'] tbody tr")
    countTotalRows = tableRow.count()
    print("total rows in the table are:", countTotalRows)
    #expect() expects a Locator object, not an integer. So, we should use the countTotalRows variable to compare with the expected count.
    expect(tableRow).to_have_count(7)


    # 3) count of columns/headers in the table
    tableHeader = page.locator("table[name='BookTable'] tbody th")
    countTotalColumns = tableHeader.count()
    print("total columns in the table are:", countTotalColumns)
    #expect() expects a Locator object, not an integer. So, we should use the countTotalColumns variable to compare with the expected count.
    expect(tableHeader).to_have_count(4)

    # 4) get the text of the second row and thrid column
    #one way to get the text of the second row and third column is to use nth-child() selector in the locator
    secondRowThirdColumn = page.locator("table[name='BookTable'] tbody tr:nth-child(2) td:nth-child(3)")
    print("text of the second row and third column is:", secondRowThirdColumn.inner_text())

    #another way to get the text of the second row and third column is to use nth() method in the locator
    secondRow = page.locator("table[name='BookTable'] tbody tr").nth(1)

    # print second row text using for loop
    cells = secondRow.all()
    for i in cells: 
        print("text of the second row cell", i.inner_text())

    #the below line  uses the xpath chaining and instead of page use the above object and extend the locator using the column and the 3rd column 
    secondRowThirdColumn = secondRow.locator("td").nth(2)
    print("text of the second row and third column is:", secondRowThirdColumn.inner_text())

    #the below line  uses the xpath chaining and instead of page use the above object and extend the locator using the column and the 3rd column 
    secondRowThirdColumn = secondRow.locator("td").nth(2)
    print("text of the second row and third column is:", secondRowThirdColumn.inner_text())

    #now pick all row text first then print text only from the secodn row
    secondRow.all_inner_texts()
    print("text of the second row is:", secondRow.all_inner_texts())

    secondRow.inner_text()
    print("text of the second row is:", secondRow.inner_text()) 



    #5) get the text of all the rows and columns in the table
    allRows = page.locator("table[name='BookTable'] tbody tr").all()
    for i in allRows:
        print("text of the row is:", i.inner_text())


    #6) return books with subject as "Selenium"
    allRows = page.locator("table[name='BookTable'] tbody tr")
    for row in allRows.all()[1:]:  # Skip the header row (index 0)
        subject = row.locator("td").nth(2).inner_text()  # 0-based index, so nth(2) is the 3rd column
        if subject == "Selenium":
            print("Book with subject Selenium:", row.inner_text()) 

    #7) return the total of the price of all the books in the table
    totalPrice = 0
    allRows = page.locator("table[name='BookTable'] tbody tr")
    for row in allRows.all()[1:]:  # Skip the header row (index 0)
        priceText = row.locator("td").nth(3).inner_text()  # 0-based index, so nth(3) is the 4th column
        price = float(priceText)  # Convert the price text to a float
        totalPrice += price
    print("Total price of all books:", totalPrice)



    






    







