# Automate a login form (use https://practicetestautomation.com/practice-test-login/)
# •	Enter username/password
# •	Click login
# •	Print success message
# •	Print error message

from selenium import webdriver  #imports required modules - to control browser
from selenium.webdriver.chrome.service import Service   #to manage chromedriver process
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service("C:/Users/surya/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  #creates service object
driver = webdriver.Chrome(service=service)  #initialize chrome using service object

driver.get("https://practicetestautomation.com/practice-test-login/")   #navigates to the website

username_field=driver.find_element(By.ID,"username")
username_field.send_keys("student")

password_field=driver.find_element(By.ID,"password")
password_field.send_keys("Password123")                   #Give different username and password to explore except condition

submit_button=driver.find_element(By.ID,"submit")
submit_button.click()

wait = WebDriverWait(driver, 10)

try:
    success_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"post-title")))
    print(f"Success message : {success_msg.text}")  #Displaying the message

except:
    error_msg = driver.find_element(By.ID, "error")
    print("ERROR:", error_msg.text)