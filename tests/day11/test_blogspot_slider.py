from playwright.sync_api import Page, expect
import re
import time


def drag_handle(page: Page, handle_locator, target_x: float):
    # get the position and size of the handle
    box = handle_locator.bounding_box()

    # calculate the center of the handle so we click exactly on it
    handle_center_x = box["x"] + box["width"] / 2
    handle_center_y = box["y"] + box["height"] / 2

    # move mouse to the handle center, hold down, drag to target, then release
    page.mouse.move(handle_center_x, handle_center_y)   # move the mouse to the location of the handle 
    page.mouse.down()     # press the mouse button
    page.mouse.move(target_x, handle_center_y, steps=20)  # drag the mouse to the target location steps=20 makes the drag smooth
    page.mouse.up()     # release the mouse button  


def test_slider_drag_range(page: Page):

    # navigate to the practice site
    page.goto("https://testautomationpractice.blogspot.com/")

    # find the slider bar and scroll it into view so it's interactable
    slider_bar = page.locator("#slider-range")
    slider_bar.scroll_into_view_if_needed()

    page.wait_for_timeout(2000)

    # confirm the slider is actually visible on the page
    expect(slider_bar).to_be_visible()

    # get the pixel position and dimensions of the slider bar
    slider_box = slider_bar.bounding_box()

    # the slider has two handles - first span is left, second span is right
    left_handle  = page.locator("#slider-range span:nth-of-type(1)")
    right_handle = page.locator("#slider-range span:nth-of-type(2)")

    # calculate x position for 20% across the slider → should land around $100
    # slider range is $0-$500, so 20% = $100
    target_left = slider_box["x"] + (slider_box["width"] * 0.20)
    drag_handle(page, left_handle, target_left)
    time.sleep(0.5)  # wait a moment so the UI updates before next drag

    # calculate x position for 80% across the slider → should land around $400
    target_right = slider_box["x"] + (slider_box["width"] * 0.80)
    drag_handle(page, right_handle, target_right)
    time.sleep(0.5)

    # check what value is shown in the amount field after dragging
    amount_display = page.locator("#amount")
    print("Slider value after drag:", amount_display.input_value())

    # mouse drag isn't pixel perfect so the value can be $1-2 off
    # using regex to accept $98/$99/$100 on left and $398/$399/$400 on right
    expect(amount_display).to_have_value(re.compile(r"\$9[89]|\$100 - \$39[89]|\$400"))

    time.sleep(2)  # keep browser open so we can see the final result







