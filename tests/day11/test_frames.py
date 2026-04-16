import pytest
from playwright.sync_api import Page, expect, Locator, Dialog


#this will count all the frames available on the page first by giving a list of frames
#in selenium we had to switch to the frame first and then perform the action
#but in playwright we can directly access the frame and perform the action
#this is because playwright has a concept of frame locators which are different from page locators
#frame locators are used to access the frames and perform the action
#page locators are used to access the elements on the page and perform the action

def test_frames(page: Page):
    page.goto("https://practice-automation.com/iframes/")
    page.wait_for_timeout(2000)
    frames = page.frames
    print("Number of frames on page:" ,len(frames))




def test_first_frame(page: Page):
    page.goto("https://practice-automation.com/iframes/")
    page.wait_for_timeout(2000)

    #interacting with the first frame
    # get the frame and inside it use the elements
    frame1 = page.frame_locator("#iframe-1") 

    # as the elements are inside the frame so first we need to find the frame and then the element inside the frame
    #as the frame has been found so now we find the element inside the frame
    frame_name = frame1.locator("b.navbar__title")
    print("Frame name is: ", frame_name.text_content())
    getting_started_button = frame1.locator("a.getStarted_Sjon")
    getting_started_button.click()
    page.wait_for_timeout(2000)
    first_page_heading = frame1.locator("h1")
    expect(first_page_heading).to_have_text("Installation")
    print("First page heading is: ", first_page_heading.text_content())


def test_second_frame(page: Page):

    # Force a large viewport so the navbar doesn't collapse
    page.set_viewport_size({"width": 1920, "height": 1080})
    
    page.goto("https://practice-automation.com/iframes/")
    # ... rest of your code

    page.goto("https://practice-automation.com/iframes/")
    page.wait_for_timeout(2000)

    #interacting with the second frame
    # get the frame and inside it use the elements
    frame2 = page.frame_locator("#iframe-2")

    # as the elements are inside the frame so first we need to find the frame and then the element inside the frame
    #as the frame has been found so now we find the element inside the frame
    frame_name = frame2.locator("h1.d-1")
    print("Frame header is: ", frame_name.text_content())
    documentation_link = frame2.locator("#main_navbar>ul>li:nth-child(3)>a>span")
    documentation_link.click()
    page.wait_for_timeout(2000)
    second_page_heading = frame2.locator("h1")
    expect(second_page_heading).to_have_text("The Selenium Browser Automation Project")
    print("Second page heading is: ", second_page_heading.text_content())



def test_nested_frames(page: Page):
    page.goto("http://uitestingplayground.com/frames")
    page.wait_for_timeout(2000)

    #parent frame is 
    parent_frame = page.frame_locator("#frame-outer")
    parent_frame_text = parent_frame.locator("body>div.frame-label")
    print("Parent frame text is: ", parent_frame_text.text_content())

    #child frame is inside the parent frame
    #in selenium we had to switch to the parent frame first and then to the child frame
    #but in playwright we can directly access the child frame from the parent frame
    #to interact with the child frame we need to go from the parent frame to the child frame otherwise we cannot access the elements inside the child frame
    #this is because the child frame is nested inside the parent frame
    #similarly if there are more frames nested inside the child frame then we need to go from the parent frame to the child frame and then to the grandchild frame and so on
    #this is because the frames are nested inside each other

    child_frame = parent_frame.frame_locator("#frame-inner")
    child_frame_text = child_frame.locator("body>div.frame-label")
    print("Child frame text is: ", child_frame_text.text_content())

    