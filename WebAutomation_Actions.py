#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:45:49 2021

@author: giri
"""

############################################

#Alert popu window handling

############################################


from selenium import webdriver

url = "http://demo.guru99.com/test/delete_customer.php"

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

element = driver.find_element_by_xpath('//input[@name="cusid"]')

element.clear()

element.send_keys('1234')

submit = driver.find_element_by_xpath('//input[@name="submit"]')

submit.click()

alert = driver.switch_to.alert

print(alert.text)

alert.accept()

driver.close()

############################################

#Handling multiple windows which were opened in browser

############################################

from selenium import webdriver
from time import sleep

url = "http://demo.guru99.com/popup.php"

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

#driver.maximize_window()

#print(driver.current_window_handle)

driver.find_element_by_xpath("//a[contains(@href,'popup.php')]").click()

mainwindow = driver.window_handles

ch_wnd = mainwindow[1]

pa_wnd = mainwindow[0]
#print(driver.current_window_handle)

print(len(mainwindow))

for _ in range(5):
    driver.switch_to_window(pa_wnd)
    #driver.switch_to.window(pa_wnd)
    sleep(2)
    driver.switch_to_window(ch_wnd)
    #driver.switch_to.window(ch_wnd)
    sleep(2)

driver.quit()

############################################

#Handling & getting the content/text from the table on webpage

############################################

from selenium import webdriver

url = 'http://demo.guru99.com/test/write-xpath-table.html' 

driver = webdriver.Chrome('./chromedriver')

print("Browser used :",driver.desired_capabilities['browserName'])

print("Browser version :",driver.desired_capabilities['browserVersion'])

print("On platofrm :",driver.desired_capabilities['platformName'])

driver.get(url)

elements = driver.find_elements_by_xpath('//tbody/tr/td')

print("Table contents are : \n")

for _ in range(len(elements)):
    print(elements[_].text)
    
driver.close()
