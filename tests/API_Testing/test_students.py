'''
install the json server in local machine using command: npm install -g json-server
A json file is placed in the local machine in any folder 
goto that folder and open command prompt and start the server by running the command: json-server --watch students.json
by default the server will be launched on: http://localhost:3000

So you can now call real REST endpoints like:
✔️ GET http://localhost:3000/students
✔️ GET http://localhost:3000/students/1


Fixtures (from conftest.py):
- `student`   → loads students.json data (like base.extend in TypeScript)

- For specific status codes or JSON data we use assert, as expect does not support those
'''

import os
import pytest
from playwright.sync_api import expect

# Automatically skip all tests in this file if we are running in CI (GitHub Actions)
# since the local json-server is not running there.
pytestmark = pytest.mark.skipif(
    os.environ.get("CI") == "true",
    reason="Skipping API tests in CI environment as the local json-server is not available"
)



# ---- Tests ----

# new parameter to chain the endpoint requests in the tests
chainParameter = "active"


# GET /students — should return all 4 students
# student fixture is loaded from conftest.py which reads students.json
def test_get_all_students(api_request_context, student):

    # GET all students from the API
    response = api_request_context.get("http://localhost:3000/students")

    # Expect successful response
    expect(response).to_be_ok()
    # in TS we can do expect(response.status()).toBe(200) but in Python:
    # - response.status is a property (int), NOT a method — so no ()
    # - expect() only accepts Playwright objects (Page, Locator, APIResponse), NOT int
    # - so we use assert for exact status code checks
    assert response.status == 200
    print("The response code is:", response.status)

    # parse the response body as JSON
    data = response.json()
    print("The data from the JSON is:", data)

    # verify the API returns the same number of students as the JSON file
    assert len(data) == len(student)
    print("Total students from API:", len(data))
    print("Total students from JSON:", len(student))



# POST /students — should add a new student
# test_add_student is dependent on test_get_all_students
# so it should be run after test_get_all_students
# and the chainParameter should be updated with the new student id

def test_add_student(api_request_context, student):
    new_student_data = {
      "id": "874",
      "name": "Macky",
      "location": "Poland",
      "phone": "99443321",
      "courses": [
        "ML",
        "AWS"
      ]
    }

    response = api_request_context.post("http://localhost:3000/students", data=new_student_data)
    expect(response).to_be_ok()
    assert response.status == 201

    # get the data from the response
    new_data = response.json()

    if new_data["id"] == "874":
        print("The newly created student details:", new_data)
        
    global chainParameter
    chainParameter = new_data["id"]
    print("The new parameter is:", chainParameter)

    
    
# PATCH /students/:id — should update an existing student
# test_update_student is dependent on test_add_student
# so it should be run after test_add_student
def test_update_student_location_only(api_request_context, student):
    update_data ={
        "location": "Jamamamambabababalalalalayayaya"
    }

    response = api_request_context.patch(f"http://localhost:3000/students/{chainParameter}", data=update_data)
    expect(response).to_be_ok()
    assert response.status == 200

    updated_data = response.json()
    print("The updated student details:", updated_data)



# update an existing student with a speific id and dont use the chainParameter
# also this test should not be dependent on any other test

def test_update_specific_student(api_request_context, student):
    specific_id = 4
    update_data = {
        "location": "lagi lagi lagi la land"
    }
    response = api_request_context.patch(f"http://localhost:3000/students/{specific_id}", data=update_data)
    expect(response).to_be_ok()
    assert response.status == 200
    updated_data = response.json()
    print("The updated student details:", updated_data)

# DELETE /students/{chainParameter} — should delete the student added in test_add_student
# test_delete_student is dependent on test_add_student
# so it should be run after test_add_student


def test_delete_student(api_request_context, student):
    response = api_request_context.delete(f"http://localhost:3000/students/{chainParameter}")
    expect(response).to_be_ok()
    assert response.status == 200
    deleted_data = response.json()
    print("The deleted student details:", deleted_data)
    