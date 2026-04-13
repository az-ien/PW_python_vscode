from playwright.sync_api import Page, expect

# same logic was done in play wright tests, this handles both future and past date selections,
# the while loop is to ensure that the clicks contineu to happen until the month and year are correct, then we loop through the date cells to find the correct date and click it



def select_date(target_year: str, target_month: str, target_date: str, page: Page, is_future: bool) -> None:
    while True:
        current_month = page.locator(".ui-datepicker-month").text_content()
        current_year = page.locator(".ui-datepicker-year").text_content()

        if current_month == target_month and current_year == target_year:
            break

        if is_future:
            page.locator("a[title='Next']").click()
        else:
            page.locator("a[title='Prev']").click()

    date_cells = page.locator(".ui-datepicker-calendar td")
    date_count = date_cells.count()

    for index in range(date_count):
        date_cell = date_cells.nth(index)
        date_text = date_cell.inner_text()

        if date_text == target_date:
            date_cell.click()
            break

    page.wait_for_timeout(3000)


def test_jquery_datepicker(page: Page) -> None:
    page.goto("https://testautomationpractice.blogspot.com/")
    date_input = page.locator("#datepicker")
    expect(date_input).to_be_visible()

    date_input.click()

    year = "2027"
    month = "December"
    date = "12"

    select_date(year, month, date, page, True)

    expected_date = "12/12/2027"
    expect(date_input).to_have_value(expected_date)

    page.wait_for_timeout(5000)
