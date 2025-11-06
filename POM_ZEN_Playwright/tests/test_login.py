# Test Classes contains test scripts and calling actions
# To import pytest modules
import pytest
# To use the methods from login_page importing Class LoginPage.
from pages.login_page import LoginPage
# To assert in Playwright import expect
from playwright.sync_api import expect


# To use setup fixture from conftest.py
# @pytest.mark.usefixtures("page")
class TestLogin:


   # test_successful_login() enters valid data and moves into dashboard page
   def test_successful_login(self,page):

      #This line creates an instance of the LoginPage class and passes 'page' object to interact
      login_page = LoginPage(page)
      #login_page object calls login() from login_page.py and enters username and password
      login_page.login("dhiviyainbox01@gmail.com", "$Flowering92")

      # Explicit wait, wait_for_url() waits until the URL appears after entering valid credentials
      page.wait_for_url("https://v2.zenclass.in/dashboard")
      # Assert checks current page URL matches the expected URL
      assert page.url == "https://v2.zenclass.in/dashboard"


   #test_unsuccessful_login() enters invalid credentials and asserts the url of the page
   def test_unsuccessful_login(self,page):
      login_page = LoginPage(page)
      login_page.login("dhiviyainbox@gmail.com", "flowering")

      # Assert checks current page URL matches the expected URL else displays the given message
      #This test fails since it cannot enter dashboard page
      assert page.url == "https://v2.zenclass.in/dashboard","Invalid login credentials"


   # test_validate_input_box is used to validate the email and password box is visible/editable or not
   def test_validate_input(self,page):
      login_page = LoginPage(page)

      # expect is used to assert the username and password input box is visible or not
      #page.locator locates the given selector.[login_page.username_input(object.selector_name)]
      expect(page.locator(login_page.username_input)).to_be_visible(timeout=2000)
      expect(page.locator(login_page.password_input)).to_be_visible(timeout=2000)

      # expect is used to assert the username and password input box is editable or not
      expect(page.locator(login_page.username_input)).to_be_editable(timeout=2000)
      expect(page.locator(login_page.password_input)).to_be_editable(timeout=2000)


   # test_validate_submit() is used to validate the signin button is enabled or not
   # expect is used to assert the signin button with timeout of 2 seconds
   def test_validate_submit(self,page):
      login_page = LoginPage(page)
      expect(page.locator(login_page.login_button)).to_be_enabled(timeout=2000)


   # test_negative_submit_message() used to assert error message after entering invalid credentials
   def test_negative_submit_message(self,page):
      login_page = LoginPage(page)
      login_page.login("dhiviyainbox@gmail.com", "flowering")

      # to_have_text() is used to check whether the selector has the given text
      # If text is indifferent test fails and assertion error occurs
      expect(page.locator(login_page.error_message)).to_have_text("Incorrect password")


   # test_logout_button() is used to enter valid data and moves to dashboard page and clicks logout
   def test_logout_button(self,page):
      logout_page = LoginPage(page)
      logout_page.login("dhiviyainbox01@gmail.com", "$Flowering92")

      # Explicit wait for URL to appear
      page.wait_for_url("https://v2.zenclass.in/dashboard")

      # Calls logout() from LoginPage to click logout which appears under profile icon
      logout_page.logout()

      # Checks after logout whether it moves back to login page again
      page.wait_for_url("https://v2.zenclass.in/login")
      assert page.url=="https://v2.zenclass.in/login"


#To generate HTML Report of Pytest cases:pytest -v -s tests/test_login.py --html=report.html
#report.html(to be opened in Browser)

