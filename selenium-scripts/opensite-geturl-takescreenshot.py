import os

from selenium import webdriver  #imports required modules - to control browser
from selenium.webdriver.chrome.service import Service   #to manage chromedriver process

service=Service("C:/Users/surya/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  #creates service object
driver = webdriver.Chrome(service=service)  #initialize chrome using service object

driver.get("https://example.com")   #navigates to example.com

url=driver.current_url  #captures the current url
print(f"Current url is {url}")  #print url

driver.save_screenshot("example_screenshot.png")    #captures the current page of the specified browser page
print("Scrrenshot saved as example_screenshot.png")
driver.quit()   #closes the browser
print(os.getcwd())  #Prints the path to screenshot
