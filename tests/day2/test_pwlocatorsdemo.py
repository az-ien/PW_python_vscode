import re
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page


def test_verify_pwlocators(page:Page):
    page.goto("https://ultimateqa.com/simple-html-elements-for-automation/")
    #page.getbyalttext() which is same as alt text in html   
    logopage = page.get_by_alt_text("ultimate qa")
    expect(logopage).to_be_visible(timeout=5000)

    page.goto("https://testautomationpractice.blogspot.com/")
    #page.getbytext() which is same as text in html
    #textpage = page.get_by_text("Automation Testing Practice")
    textpage = page.get_by_text(re.compile(".*Testing.*"))
    expect(textpage).to_be_visible(timeout=5000)

    #page.getbyrole() which is same as role in html, every element has a role in html
    #role is the element type like button, link, checkbox, etc and its name is the text on the element
    buttonpage = page.get_by_role("button", name="START")
    expect(buttonpage).to_be_visible(timeout=5000)

    #page.getbylabel() which is same as label in html, label is the text associated with an input element
    labelpage = page.get_by_label("Address:")
    labelpage.fill("abra cadabra street")
    expect(labelpage).to_be_visible(timeout=5000)

    #page.title() which is same as title in html
    titlepage = page.title()  # this returns the title of the page as a string automatically 
    #so we can directly use it in expect statement. and so no need to use expect(titlepage)  because titlepage is already a string and we can directly compare it with the expected title.
    expect(page).to_have_title("Automation Testing Practice")



    page.close()