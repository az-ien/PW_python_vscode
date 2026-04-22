import pytest
from playwright.sync_api import Page, expect, Locator, Dialog

@pytest.mark.skip("Skipping the file upload test case as when uploaded it will not be able to find the files")
def test_multiple_file_upload(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    multiplefileupload = page.locator("#multipleFilesInput")

    files=["C:/Users/azlan.malik/Downloads/AC_SL1500_.jpg", "C:/Users/azlan.malik/Downloads/s-l1600.jpg"]
    multiplefileupload.set_input_files(files)
    page.wait_for_timeout(3000)
    page.locator("button:has-text('Upload Multiple Files')").click()
    page.wait_for_timeout(3000)

    message_contains_all_file_name = page.locator("#multipleFilesStatus")
    expect(message_contains_all_file_name).to_contain_text("AC_SL1500_.jpg")
    expect(message_contains_all_file_name).to_contain_text("s-l1600.jpg")

    page.wait_for_timeout(3000)




    

    



