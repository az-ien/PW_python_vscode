# same as xpath as id, tag, class, attributes. there can also be a comnbination, there is a special type of synatx
# css and xpath are universal 
# tag#id
# tag.class
# tag[attribute=value]
# tag.class[attribute=value]
# tag#id.class[attribute=value]
# absolute css is like absolute xpath starting from one node and going node to node   parent > child > child


from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page    

def test_verify_csslocators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    # by #id and tag
    page.locator("input#small-searchterms").fill("T-Shirts")
    page.wait_for_timeout(2000)

    # by .class and tag
    page.locator("input.search-box-text").fill("monkey")
    page.wait_for_timeout(2000)

    # by [attribute=value] and tag. this is any attribute, not just id and class. it can be name, type, value, etc
    page.locator("input[name='q']").fill("PUNCH")
    page.wait_for_timeout(2000)

    # by .class and [attribute=value] and tag. this is a combination of class and any attribute
    page.locator("input.search-box-text[name='q']").fill("labalab")
    page.wait_for_timeout(2000)

    # by #id and .class and [attribute=value] and tag. this is a combination of id, class and any attribute
    page.locator("input#small-searchterms.search-box-text[name='q']").fill("cacacacaca")
    page.wait_for_timeout(2000)

