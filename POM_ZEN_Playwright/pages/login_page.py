# LoginPage contains init,selectors,login,get error message and logout method
# To use the methods from base_page importing Class BasePage.
# from folder_name.file_name import Class_name
from pages.base_page import BasePage


# LoginPage inherits BasePage. LoginPage contains selectors and methods to interact with selectors.
class LoginPage(BasePage):


   # Constructor method contains different selectors for login and logout functionality
   def __init__(self, page):
       # super() is used to call the basepage constructor method to initialize self.page
       super().__init__(page)

       # SELECTORS - Uses fill() from BasePage to locate these elements while doing interactions.
       # Email and password box selector using XPATH
       self.username_input = '//input[@type="text"]'
       self.password_input = '//input[@type="password"]'

       # Signin button and error message selector using XPATH
       self.login_button = '//button[@type="submit"]'
       self.error_message='//p[text()="*Incorrect password!"]'

       # Pop_up,Profile icon and logout selector using XPATH
       self.pop_up='//button[@aria-label="Close popup"]'
       self.profile_icon='//img[@class="profile-click-icon"]'
       self.logout_button='//div[@class="user-profile-notify-container"]/div[3]'


   # METHODS TO INTERACT WITH THE ELEMENTS
   # login() is used to find username and password and enter the valid data and to click signin button
   def login(self, username, password):

       #self.username_input,self.password_input are selectors. username,password are the text to be entered.
       # uses fill() and click() methods from BasePage
       self.fill(self.username_input, username)
       self.fill(self.password_input, password)
       self.click(self.login_button)


   # get_error_message() is used to return the error message text while entering invalid credentials
   def get_error_message(self):
       return self.get_text(self.error_message)


   # logout() is used to close the popup which appears and search the profile icon and clicks logout
   def logout(self):

       # wait_for_selector waits for the pop_up selector and closes the pop_up
       self.wait_for_selector(self.pop_up)
       self.click(self.pop_up)

       # Locates the logout icon which appears under profile icon and clicks it.
       self.click(self.profile_icon)
       self.click(self.logout_button)
