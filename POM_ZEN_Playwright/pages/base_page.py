# POM Framework using playwright for ZEN Portal.Pages folder contains base_page and login_page
# Page classes represents the webpage.
# BasePage contains init, searching selector, fill values,click and explicit wait
class BasePage:


   # Constructor method and self refers to the current object.page is a parameter
   def __init__(self,page):
       # This stores the passed-in page object as an instance variable so other methods in the class can use it.
       self.page = page


   # fill() is used to locate the selector and fill the value
   def fill(self, selector, value):
       # page.locator() locates the element and fill(value) is used to enter the value
       # selector can be CSS selector,Xpath or Playwright selector
       self.page.locator(selector).fill(value)


   # click() is used to click the located element
   def click(self,selector):
       # page.locator() locates the element and clicks it
       self.page.locator(selector).click()


   # get_text() gets the text value of the element
   def get_text(self,selector):
       # inner_text() returns the visible text content of the located element
       return self.page.locator(selector).inner_text()


   # Explicit wait used in Playwright to wait for any specified locator
   def wait_for_selector(self, selector):
       self.page.wait_for_selector(selector)

