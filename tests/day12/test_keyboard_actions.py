import pytest
from playwright.sync_api import Page, expect, Locator, Dialog

#all of the below steps are common for all keyboard actions
# first we need to focus on the element
# write some text in the input field 1 then select it and delete it and then insert text using insert_text() method
# then we need to select all of the text that was inputed into the first field using press ctrl+a
# then we need to copy the text using press ctrl+c
# then we need to move to the next element by focusing on the next element 
# then we need to paste the text using press ctrl+v
# then we need to move to the next element by focusing on the next element
# then we need to paste the text using press ctrl+v



def test_kwyboard_actions(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    input1 = page.locator("#input1")
    input2 = page.locator("#input2")
    input3 = page.locator("#input3")

    input1.focus()
    input1.fill("heeeeeellllloooooooooo")
    input1.press("Control+a")
    input1.press("Delete")
    expect(input1).to_have_value("")
    page.keyboard.insert_text("lalalalala")
    page.keyboard.press("Control+a")
    page.keyboard.press("Control+c")

    input2.focus()
    page.keyboard.press("Control+v")

    input3.focus()
    page.keyboard.press("Control+v")

    page.wait_for_timeout(3000)


 

    
