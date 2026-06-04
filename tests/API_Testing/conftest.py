import pytest
import json
import os


# This fixture loads the students.json file and provides the data to the tests
# In TypeScript Playwright this is done by extending the test with base.extend<MyFixtures>
# In Python Playwright we use pytest fixtures in conftest.py to achieve the same thing
# conftest.py is automatically discovered by pytest — no need to import it in the test files

'''
| Concept                    | TypeScript (Playwright)    | Python (Playwright + pytest)       |
| -------------------------- | -------------------------- | ---------------------------------- |
| Fixture definition         | `test.extend({ ... })`     | `@pytest.fixture` in `conftest.py` |
| How tests receive fixtures | Arguments to test function | Arguments to test function         |
| Cleanup logic              | After `use()`              | After `yield`– return teardown     |
| Test runner                | Playwright Test            | Pytest                             |
| API Request                | `request.get()`            | `api_request_context.get()`        |
| API Status                 | `response.status`          | `response.status`                  |
| API JSON                   | `response.json()`          | `response.json()`                  |



'''



@pytest.fixture
def student():
    """Load student data from the JSON file — like a TypeScript fixture"""
    # get the path to the json file relative to this conftest.py
    json_path = os.path.join(os.path.dirname(__file__), "students.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["students"]

'''
api_request_context is NOT a built-in fixture in pytest-playwright
we need to create it ourselves using the `playwright` fixture
the `playwright` fixture IS provided by pytest-playwright and gives us access to the Playwright API
we use playwright.request.new_context() to create a lightweight HTTP client
this is similar to how TypeScript Playwright provides `request` in test fixtures

 it comes down to who runs the tests.

TypeScript: Playwright Test is both the test runner AND the framework. It bundles everything — page, request, browser, context — all built-in automatically.
Python: Two separate tools are involved:

pytest = the test runner
pytest-playwright = a plugin that connects Playwright to pytest
The plugin only provides browser-related fixtures (page, browser, context). It does not provide an API request context. So we have to create it ourselves.

'''

@pytest.fixture(scope="session")
def api_request_context(playwright):
    """Create an API request context — like the `request` fixture in TypeScript Playwright"""
    request_context = playwright.request.new_context()
    yield request_context
    # cleanup: dispose the context after all tests are done
    request_context.dispose()
