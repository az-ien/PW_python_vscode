
# Selenium: usually extract element data first, then assert using test framework assertions.
#in playwright python  assertions need locators cannot be done on values/data of the elements so to have attribute is there
#in playwright ts assertions can be done on both locators and values/data of the elements 


import pytest
import pytest_playwright

from playwright.sync_api import Page, expect


def test_inputbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    nametextbox = page.locator("#name")
    expect(nametextbox).to_be_visible()
    expect(nametextbox).to_be_enabled()  

    #check  the attribute of the text box
    expect(nametextbox).to_have_attribute("maxlength", "15")

    # this is specific to python and selenium to get any attribute value of the text box 
    maxlengthvalue = nametextbox.get_attribute("maxlength")
    print("Max length value of the name text box: ", maxlengthvalue)

    #fill value in the text box and check the value
    nametextbox.fill("John Doe")
    nametextbox_value = nametextbox.input_value()
    print("Value entered in the name text box: ", nametextbox_value)


def test_radiobutton(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    male_radiobutton = page.locator("#male")
    expect(male_radiobutton).to_be_visible()
    expect(male_radiobutton).not_to_be_checked()  # Assert that the radio button is not selected by default

    male_radiobutton.check()  # Select the radio button
    expect(male_radiobutton).to_be_checked()  # Assert that the radio button is now selected


def test_checkbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #select single checkbox
    sunday_checkbox =page.get_by_label("Sunday")
    sunday_checkbox.check()  # Select the checkbox
    expect(sunday_checkbox).to_be_checked()  # Assert that the checkbox is now selected

    #count total number of checkboxes
    all_checkboxes =page.locator("input.form-check-input[type='checkbox']")
    all_checkboxes_count = all_checkboxes.count()
    expect(all_checkboxes).to_have_count(7)  # Assert that there are 7 checkboxes on the page
    print("Total number of checkboxes on the page: ", all_checkboxes_count)

    # get all checkboxes as list of locators
    checkbox_list = all_checkboxes.all()

    # iterate only through the last 3 checkboxes
    #for checkbox in checkboxes[-3:]:
    for checkbox in checkbox_list:
        checkbox_id = checkbox.get_attribute("id")      # Get the ID of the checkbox
        #checkbox_label = page.locator(f"label[for='{checkbox_id}']").inner_text()  # Get the label text associated with the checkbox using its ID
        checkbox_label = checkbox.locator("xpath=following-sibling::label").inner_text()  # Get the label text associated with the checkbox 

        checkbox.check() # Select the checkbox

        print("Checkbox ID:", checkbox_id, "Checkbox Label:", checkbox_label)

        #check only the checkbox with label "Wednesday"
        if checkbox_label =="wednesday":
            checkbox.uncheck()  # Select the checkbox
            expect(checkbox).not_to_be_checked()  # Assert that the checkbox is now selected

    # get all checkboxes as list of locators
    #checkbox_list = all_checkboxes.all()

    # Iterate through all checkboxes and toggle their state
    for checkbox in checkbox_list:

        if(checkbox.is_checked()):
            checkbox.uncheck()  # Unselect the checkbox
            expect(checkbox).not_to_be_checked()  # Assert that the checkbox is now unselected

        else:
            checkbox.check() # Select the checkbox
            expect(checkbox).to_be_checked()  # Assert that the checkbox is now selected    

    
    #check only the 1,3,6 checkboxes
    for index in [0,2,5]:  # Indexes of the checkboxes to be checked (1st, 3rd, and 6th)
        checkbox = checkbox_list[index]
        checkbox.check()  # Select the checkbox
        expect(checkbox).to_be_checked()  # Assert that the checkbox is now selected





         