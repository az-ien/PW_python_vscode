from playwright.sync_api import Page, expect, Locator

def select_checkin_date(page: Page, year:str, month:str, day:str) -> None:
    while True:
        checkin_month_and_year =page.locator("h3.e7addce19e.af236b7586:visible").nth(0).inner_text()
        if month in checkin_month_and_year and year in checkin_month_and_year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()
    
    dates_checkin_table = page.locator("table[aria-labelledby='bui-calendar-month-2026-9'] tbody tr td").all()
    for date in dates_checkin_table:
        if date.inner_text() ==day:
            date.click()
            break
    
    page.wait_for_timeout(3000)
    


def select_checkout_date(page: Page, year:str, month:str, day:str):
    while True:
        checkout_month_and_year =page.locator("h3.e7addce19e.af236b7586:visible").nth(1).inner_text()
        if month in checkout_month_and_year and year in checkout_month_and_year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()
    
    dates_checkout_table = page.locator("table[aria-labelledby='bui-calendar-month-2026-10'] tbody tr td").all()
    for date in dates_checkout_table:
        if date.inner_text() ==day:
            date.click()
            break
    
    page.wait_for_timeout(3000)





def test_booking_date_picker(page: Page):
    page.goto("https://www.booking.com/")
    # Set up the listener first
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.locator("button[aria-label='Dismiss sign-in info.']").click()
    page.get_by_test_id("searchbox-dates-container").click()
    
    select_checkin_date(page,"2026","October","10")
    checkindate = page.locator("span[data-date='2026-10-10']")
    expect(checkindate).to_contain_text("10")

    select_checkout_date(page,"2026","November","5")
    checkoutdate = page.locator("span[data-date='2026-11-05']")
    expect(checkoutdate).to_contain_text("5")




