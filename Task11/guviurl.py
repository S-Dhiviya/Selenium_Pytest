#SELENIUM AUTOMATION CODE TO LOGIN INTO GUVI PAGE
#Importing WebDriver,Service,ChromeDriverManager and By classes from selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#To import time library for use of time.sleep()
import time

#Creating WebDriver instance to open Chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#get() navigates to the GUVI page
driver.get("https://www.guvi.in/")
#Maximizes the Chrome Browser Window
driver.maximize_window()
time.sleep(3)


#<a href="/sign-in/" id="login-btn" class="⭐️rawbli-0 text-decoration-none me-3 text-success text-base font-medium">Login</a>
#find_element is used to find "login button" and value of it using Inspect and click() is used to click login
#This migrates to login page
#Syntax:driver.find_element(By.ID,"value")
driver.find_element(By.ID,"login-btn").click()
#driver.current_url prints the current URL of the page
print("Login URL:",driver.current_url)


#find_element is used to find "email address" input box and send_keys is used to enter the given value
# <input type="email" class="form-control" id="email" placeholder="">
driver.find_element(By.ID,"email").send_keys("dhiviyainbox01@gmail.com")
time.sleep(3)

#find_element is used to find "password" input box and send_keys is used to enter the given value
# <input type="password" class="form-control" id="password" placeholder="">
driver.find_element(By.ID,"password").send_keys("$Flowering92")
time.sleep(3)


#After entering valid username and password and by clicking login,user signup into GUVI page
# <a id="login-btn" class="btn login-btn">Login</a>
#LINK_TEXT is used to find the text of "login button" element and click() is used to click login
#Syntax:driver.find_element(By.LINK_TEXT,"value")
driver.find_element(By.LINK_TEXT,"Login").click()
time.sleep(5)


#Closes the Chrome Window and ends the WebDriver session
driver.quit()