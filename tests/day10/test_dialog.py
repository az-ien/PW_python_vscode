from playwright.sync_api import Page, expect, Locator, Dialog



#in selenium the driver has to be switched to the alert and then we can accept or dismiss
#but in playwright (type script or python) event listeners are used to handle dialogs, so before clicking the button to launch the dialog 
# an event listener will wait for the dialog to appear and when it appears after the click will automatically accept or dismiss it 
# but the method for the event listener can modified to play with the dialog and get the text of the dialog or even send text to the dialog if it's a prompt dialog (that takes text)

def test_simple_alert_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    

    #before clicking we need to register the event listener for dialog using page.on() method
    page.on('dialog', lambda dialog: dialog.accept())

    # then when the event is registered we can click the button to trigger the dialog and it will be automatically accepted by the event listener
    # this happens because the event listener is set up to listen for 'dialog' events and when the dialog appears, it calls the lambda function which accepts the dialog
    # and wait just to see what happens after accepting the dialog
    page.wait_for_timeout(2000)
    page.locator("#alertBtn").click()


def test_confirmation_alert_dialog2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)

    # this is custom handler for the dialog, instead of calling the custom lambda accept method, this custom handler will not only accept the dialog but also print the 
    # type of the dialog before accepting it 
    def handle_dialog(dialog: Dialog):
        print("Dialog type is :", dialog.type)
        dialog.accept()

    # here that custom handler is registered to listen for the dialog event and when the dialog appears after clicking the button, the custom handler will be executed which will print the type of the dialog
    page.on("dialog",handle_dialog)
    page.wait_for_timeout(2000)
    page.locator("#confirmBtn").click()


def test_prompt_alert_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)

    def handle_dialog(dialog: Dialog):
        print("Dialog type is :", dialog.type)
        dialog.accept("jajajajajajajajaja")

    page.on("dialog",handle_dialog)
    page.wait_for_timeout(2000)
    page.locator("#promptBtn").click()

    prompt_text_displayed = page.locator("#demo")
    expect(prompt_text_displayed).to_contain_text("Hello jajajajajajajajaja! How are you today?") 
