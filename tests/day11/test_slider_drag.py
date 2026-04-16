from playwright.sync_api import sync_playwright , expect,Page,Locator
import time

def test_drag_slider(page: Page):
    # Navigate to the page
    page.goto('https://practice.expandtesting.com/horizontal-slider')

    # 1. Locate the slider element
    slider = page.locator('input[type="range"]')
    
    slider.scroll_into_view_if_needed()
    # 2. Get the dimensions and position of the slider on the screen
    box = slider.bounding_box()
    
    if box:
        # Note: The horizontal slider goes from 0.0 to 5.0.
        # To get to 3.0, we want to drag to 60% of the slider wide (3.0 / 5.0 = 0.6)
        
        # Start position: Left edge of the slider
        start_x = box["x"]
        start_y = box["y"] + (box["height"] / 2)
        
        # Target position: 60% across the slider's total width
        target_x = box["x"] + (box["width"] * 0.6)
        target_y = box["y"] + (box["height"] / 2)

        # Move mouse to the very beginning of the slider and press down
        page.mouse.move(start_x, start_y)
        page.mouse.down()
        
        # Drag the mouse to our calculated target X coordinate to reach 3.0
        page.mouse.move(target_x, target_y)
        page.mouse.up()
        
    # Verify the value text next to it updated correctly
    value = page.locator('#range')
    expect(value).to_have_text("3")
    print("Current Slider Value is: ", value)

    # Adding sleep just so you can actually see it before browser closes
    time.sleep(3)
