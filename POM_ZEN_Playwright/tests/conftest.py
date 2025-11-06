# conftest.py is used to define fixtures that can be reused across multiple test files.
# To import pytest modules
import pytest
#To import the synchronous version of the Playwright API in Python
from playwright.sync_api import sync_playwright


# Fixtures are functions in pytest used to prepare environment for test execution.Scope by default it is "function".
#Scope="function" defines set up and tear down for each test
@pytest.fixture(scope="function")
def page():

   # with defines proper setup and teardown of browser
   # sync_playwright() initiates playwright, alias name for playwright used is 'p'
   with sync_playwright() as p:

       # By default,playwright runs on headless mode.Launches Chromium browser
       # For headed mode, headless=False is used
       browser = p.chromium.launch()
       # new_context() opens a new browser window
       context = browser.new_context()

       # new_page() opens a new tab in context
       page = context.new_page()
       #  page.goto() navigates to the given URL
       page.goto("https://v2.zenclass.in/login")

       # yield is used for setup and teardown logic
       yield page
       # Close the browser after test completes
       browser.close()
