# same as xpath as id, tag, class, attributes. there can also be a comnbination, there is a special type of synatx
# css and xpath are universal 
# tag#id
# tag.class
# tag[attribute=value]
# tag.class[attribute=value]
# tag#id.class[attribute=value]
# absolute css is like absolute xpath starting from one node and going node to node   parent > child > child
# body>div>*:nth-child(1)
# p[class^='ma'] this is a starts with syntax, it will match any element whose class attribute starts with 'main'
# p[class$='in'] this is an ends with syntax, it will match any element whose class attribute ends with 'main'
# p[class*='ai'] this is a contains syntax, it will match any element whose class attribute contains 'main'
# p:not(.main) this is a not syntax, it will match any element that does not have the class 'main'
# p:has(.main) this is a has syntax, it will match any element that has a child element with the class 'main'
# p:has-text("text") this is a has-text syntax, it will match any element that has the text "text" anywhere inside it
# title+link this is an adjacent sibling syntax, it will match any element that is immediately preceded by a sibling element with the tag name 'title'
# body>head>title+link this is an adjacent sibling syntax, it will match any element that is immediately preceded by a sibling element with the tag name 'title' which is a child of 'head' which is a child of 'body'


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

