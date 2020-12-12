# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("./chromedriver")

driver.maximize_window()

driver.get("https://www.google.com/")

print(driver.title)

driver.find_element_by_name("q").send_keys("Automation testing")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

for _ in range(4):
  print(driver.title) #gets the web title 
  driver.back() #moves back to the older history & opens the page
  print(driver.title) #gets the web title 
  driver.forward() #moves forward to the new page which is stored in history & opens the page
  
driver.close() #ends the browser actions here 



