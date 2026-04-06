from playwright.sync_api import sync_playwright, Page, expect

#css selector can be used to use partial text and it will get the complete elemenent with that partial text.
#no need for any text check conditions in the code use the css selector


def test_static_dynamic_table(page: Page):

    page.goto("https://practice.expandtesting.com/dynamic-table")
    table = page.locator("table.table-striped>tbody")
    rows = table.locator("tr") 
    listOfRows = rows.all()


    for row in listOfRows:
        firstColumn = row.locator("td").nth(0)
        browserName = firstColumn.inner_text()
        if browserName == "Chrome":
            CPUusage = row.locator("td:has-text('%')").inner_text()
            print("CPU usage of Chrome is:", CPUusage)
            break

    yellowBarText = page.locator("#chrome-cpu")
    expect(yellowBarText).to_contain_text(CPUusage)


    






        







