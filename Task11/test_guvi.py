#To import pytest modules and filename should be test_filename.py or \filename_test.py
import pytest
#Importing WebDriver and By classes from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Fixtures are functions in pytest used to prepare environment for test execution.Scope by default it is "function".
#Scope="class" defines set up and tear down once for each test class
@pytest.fixture(scope="class")
# driver() is used to open Sign In page of GUVI in chrome,it runs all testcases and quits session
def driver():
#Headless browsing where the Chrome runs in background which will not be visible
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver=webdriver.Chrome(options=options)

#get() navigates to the Sign-in page of GUVI
    driver.get("https://www.guvi.in/sign-in/")
#Maximizes the Chrome Browser Window
    driver.maximize_window()

    print("[class]To check validation of login page started")
#yield moves to test cases and runs all the testcases
    yield driver
    print("[class]To check validation of login page ended")

#Terminates the browser session
    driver.quit()


#Grouped all the test cases inside a class
class TestingGUVI:

#Pytest testcases are written as test_method()
#Positive test case on asserting URL of Login button by providing correct url
#assert is used to compare values and return TRUE or FALSE
    def test_positive_url(self,driver):
        assert driver.current_url=="https://www.guvi.in/sign-in/"


#Negative test case on asserting URL of Login button by providing incorrect url
    def test_negative_url(self,driver):
        assert driver.current_url=="https://www.guvi.in/sign-up/"


#Positive test case on asserting username input box is visible and enabled
#is_enabled checks whether the input box is interactable or not, like typing an email address
#is_displayed checks whether the input box is visible or not, like typed email address is visible or not
    def test_positive_username(self,driver):
        username=driver.find_element(By.ID,"email")
        assert username.is_enabled()
        assert username.is_displayed()


#Negative test case on asserting username input box is visible and enabled
#assert not returns FALSE if username is enabled and visible
    def test_negative_username(self,driver):
        username = driver.find_element(By.ID,"email")
        assert not username.is_enabled()
        assert not username.is_displayed()


#Positive test case on asserting Password input box is visible and enabled
    def test_positive_password(self,driver):
        password=driver.find_element(By.ID, "password")
        assert password.is_enabled()
        assert password.is_displayed()


#Negative test case on asserting Password input box is visible and enabled
    def test_negative_password(self,driver):
        password=driver.find_element(By.ID, "password")
        assert not password.is_enabled()
        assert not password.is_displayed()


#Positive test case on asserting Login button is working properly after providing correct credentials
#If click() signup a user then assert returns TRUE
    def test_positive_login_button(self,driver):
        driver.find_element(By.ID, "email").send_keys("dhiviyainbox01@gmail.com")
        driver.find_element(By.ID, "password").send_keys("$Flowering92")
        submit_button = driver.find_element(By.ID, "login-btn")
        submit_button.click()
        assert submit_button.is_enabled()


#Negative test case on asserting Login button is working properly after providing incorrect credentials
#If click() doesn't signup a user then assert returns FALSE.Invalid user cannot Sign up
    def test_negative_login_button(self,driver):
        driver.find_element(By.ID, "email").send_keys("diya@gmail.com")
        driver.find_element(By.ID, "password").send_keys("lowering92")
        submit_button=driver.find_element(By.ID, "login-btn")
        submit_button.click()
        assert not submit_button.is_enabled()

#To generate HTML Report of Pytest cases:pytest -v -s test_guvi.py --html=report.html
#report.html(to be opened in Browser)