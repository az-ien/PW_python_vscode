'''
install the json server in local machine using command: npm install -g json-server
A json file is placed in the local machine in any folder 
goto that folder and open command prompt and start the server by running the command: json-server --watch students.json
by default the server will be launched on: http://localhost:3000

So you can now call real REST endpoints like:
✔️ GET http://localhost:3000/students
✔️ GET http://localhost:3000/students/1

API Testing in Playwright:
- For UI tests we use `page` fixture to interact with the browser
- For API tests we use `api_request_context` fixture — no browser opens
- api_request_context is like Postman but in code
- It supports: .get(), .post(), .put(), .delete() methods
- Response gives us: .status (status code) and .json() (response body)

Fixtures (from conftest.py):
- `student`   → loads students.json data (like base.extend in TypeScript)
- `base_url`  → provides the base URL http://localhost:3000

Playwright Python expect() for API responses:
- expect(response).to_be_ok()       → checks status is 200-299
- expect(response).not_to_be_ok()   → checks status is NOT 200-299
- For specific status codes or JSON data we use assert, as expect does not support those
'''

from playwright.sync_api import expect


# ---- GET Tests ----


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

