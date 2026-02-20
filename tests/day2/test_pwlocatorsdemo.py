from playwright.sync_api import Page, expect


def test_verify_pwlocators(page:Page):
    page.goto("https://ultimateqa.com/simple-html-elements-for-automation/")
    #page.getbyalttext() which is same as alt text in html   
    logopage = page.get_by_alt_text("ultimate qa")
    expect(logopage).to_be_visible(timeout=5000)