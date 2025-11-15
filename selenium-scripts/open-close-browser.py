from selenium import webdriver  #imports required modules - to control browser
from selenium.webdriver.chrome.service import Service   #to manage chromedriver process
service=Service("C:/Users/surya/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  #creates service object
driver = webdriver.Chrome(service=service)  #initialize chrome using service object

driver.get("https://www.google.com")    #nabigates to google
title=driver.title #gets the title name
print(f"Page title is {title}") #prints the title
driver.quit()   #closes the browser
