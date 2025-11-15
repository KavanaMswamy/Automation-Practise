# Automate a login form (use https://practicetestautomation.com/practice-test-login/)
# •	Enter username/password
# •	Click login
# •	Print success message

from selenium import webdriver  #imports required modules - to control browser
from selenium.webdriver.chrome.service import Service   #to manage chromedriver process
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service("C:/Users/surya/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  #creates service object
driver = webdriver.Chrome(service=service)  #initialize chrome using service object

driver.get("https://practicetestautomation.com/practice-test-login/")   #navigates to the website

username_field=driver.find_element(By.ID,"username")    #Finds username weblement
username_field.send_keys("student") #enter username

password_field=driver.find_element(By.ID,"password")    #Finds password webelement
password_field.send_keys("Password123") #enter password

login_button=driver.find_element(By.ID,"submit")    #Finds submit button
login_button.click()    #Clicks submit

wait = WebDriverWait(driver, 10)    #using external wait to get the response
success_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "post-title")))
print(f"Success message : {success_msg.text}")  #Displaying the message

driver.quit()   #Close the browser
