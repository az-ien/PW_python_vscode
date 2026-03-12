import pytest
import pytest_playwright

from playwright.sync_api import Page, expect


def test_singleselectdropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select an option from dropdown

    # 1. select by value - value is the value attribute of the option tag
    singleoptionselected = page.locator("#country").select_option("canada")
    print(singleoptionselected)

    # 2. select by label - label is the text shown in the dropdown
    singleoptionselected = page.locator("#country").select_option("Canada")
    print(singleoptionselected)

    # 3. select by index - index starts from 0
    singleoptionselected = page.locator("#country").select_option(index=2)
    print(singleoptionselected)


    # assertion to verify the selected option
    selectedoption = page.locator("#country").input_value()
    print(selectedoption)
    expect(page.locator("#country")).to_have_value("uk")

    # assertion to verify the number of options in the dropdown
    dropdownoptions = page.locator("#country>option")
    print("number of options are:", dropdownoptions.count())
    expect(dropdownoptions).to_have_count(10)

    #get text of all the options in the dropdown
    for option in dropdownoptions.all():
        raw_text = option.inner_text()    # gets the text of the option including leading and trailing whitespace characters
        text = raw_text.strip()           # .strip() is used to remove leading and trailing whitespace characters
        print(text)


    page.wait_for_timeout(4000)


def test_multiselectdropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options from the dropdown
    multiselectdropdown = page.locator("#colors")

    # 1. select by value - value is the value attribute of the option tag, mulitple values can be passed as a list
    multiselectdropdown.select_option(["red", "yellow"])

    # 2. select by label - label is the text shown in the dropdown, mulitple labels can be passed as a list
    multiselectdropdown.select_option(["Red", "Yellow"])

    # 3. select by index - index starts from 0, multiple indexes can be passed as a list
    multiselectdropdown.select_option(index=[0, 2])


    # get text of all the  options in the dropdown
    multioptions = page.locator("#colors>option")
    expect(multioptions).to_have_count(7)

    #get text of all the options in the dropdown
    for names in multioptions.all():
        raw_text = names.inner_text()    # gets the text of the option including leading and trailing whitespace characters
        text = raw_text.strip()           # .strip() is used to remove leading and trailing whitespace characters
        print(text)



    page.wait_for_timeout(4000)




def test_sortordercheck(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    unsorted_dropdown = page.locator("#colors>option")  # unsorted list
    sorted_dropdown = page.locator("#animals>option")   #sorted list

    unsorted_dropdown_text = [text.strip() for text in unsorted_dropdown.all_text_contents()]
    sorted_dropdown_text = [text.strip() for text in sorted_dropdown.all_text_contents()]

    original_list = unsorted_dropdown_text.copy()
    sorted_list = sorted(original_list)

    print(original_list)
    print(sorted_list)


    if (original_list == sorted_list ):
        print ("drop down are in sorted order....")

    else:
        print(" drop down not in sorted....")



    original_sorted_list = sorted_dropdown_text.copy()
    sorted_sorted_list = sorted(original_sorted_list)

    print(original_sorted_list)
    print(sorted_sorted_list)
    
    if (original_sorted_list == sorted_sorted_list ):
        print ("drop down are in sorted order....")

    else:
        print(" drop down not in sorted....")




    page.wait_for_timeout(5000)



















