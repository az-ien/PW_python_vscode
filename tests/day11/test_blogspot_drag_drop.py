from playwright.sync_api import Page, expect
import time


# mouse interactions with elements are different than the playweright interaction with elements, mouse needs to be moved to the precise location of the element to interact with it
# otherwise it will not work
# all these steps are common for all mouse actions
# to perform mouse actions first we need to get the bounding box of the element. bounding box is the area of the element on the screen. 
# then we need to calculate the center of the element
# then we need to move the mouse to the center of the element
# then we need to press the mouse button
# then we need to move the mouse to the target location
# then we need to release the mouse button

# same steps can be combined in a multiple time used method only the source and target locators will change
# source and target will be the parameters to the method and they will be different for different elements
# this method can be used for any drag and drop operation


def test_drag_and_drop(page: Page):

    # navigate to the practice site
    page.goto("https://testautomationpractice.blogspot.com/")

    # locate the draggable box and the droppable target area
    draggable = page.locator("#draggable")
    droppable = page.locator("#droppable")

    # scroll the drag-and-drop section into view so it's interactable
    draggable.scroll_into_view_if_needed()

    # confirm both elements are visible before attempting the drag
    expect(draggable).to_be_visible()
    expect(droppable).to_be_visible()

    # verify the initial text of the drop target is "Drop here"
    expect(droppable).to_have_text("Drop here")

    # get bounding boxes for both elements so we can calculate center coordinates
    drag_box  = draggable.bounding_box()
    drop_box  = droppable.bounding_box()


    page.wait_for_timeout(2000)

    # calculate center of the draggable element (where we'll press the mouse)
    drag_center_x = drag_box["x"] + drag_box["width"] / 2
    drag_center_y = drag_box["y"] + drag_box["height"] / 2

    # calculate center of the droppable target (where we'll release the mouse)
    drop_center_x = drop_box["x"] + drop_box["width"] / 2
    drop_center_y = drop_box["y"] + drop_box["height"] / 2

    # perform the drag: move to the draggable, hold, move to target, release
    page.mouse.move(drag_center_x, drag_center_y)   # hover over the draggable box
    page.mouse.down()                                # press and hold the mouse button
    page.mouse.move(drop_center_x, drop_center_y, steps=20)  # drag smoothly to the target
    page.mouse.up()                                  # release to complete the drop

    time.sleep(0.5)  # brief pause to allow the UI to register the drop event

    # after a successful drop the text inside the droppable area changes to "Dropped!"
    expect(droppable).to_have_text("Dropped!")

    time.sleep(2)  # keep the browser open to visually verify the result
