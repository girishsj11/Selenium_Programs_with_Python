# Selenium_with_Python_Programs
Using Selenium code with Python to automate the WebBrowser stuffs


## ***Video_database_collection_from_Youtube_using-Selenium-Python***

* Prerequisite package installation :
  - pip install db-sqlite3
  - pip install configparser
  - pip install logging
  - pip install selenium
    
       
 * Prerequisite program code :  mouse_operations.py
   - file contains all type of operations which human will do on web pages, so whenever its required we can specific operation/action based on requirement in our main program.
   - actions/operations/user_functions are listed below -->
     1. MoveToElement :- which moves the control to specific xpath 
     2. GetAttribute  :- which returns the attribute(either href,text,html link,name) based on input string value to the function
     3. LoadPage :- which waits the webpage to load a specific content/xpath to be present on the loaded webpage content.
     4. MouseClick :- which performs click operation on the specific element/xpath.
     5. Clear :- which performs clear operation on the specifc element.
     6. MouseClickAndSendKeys :- which performs click,clear operations then it will sends the given value on function to the element.
     7. MouseClickandSendKeysEnter :- which does the operation of MouseClickAndSendKeys, then hits the enter key.
     8. Dropdown_Options :- which will returns the all listed options on the particular xpath/element.
     9. scroll_down :- which scrolls down the webpage content by a mentioned offset value .
   
   
* Prerequisite property file : youtube.properties
  - file contains useful & input commands to the main program code , which contains the xpath address on it and also user can change the requirement based on his/her interest.
  
  
* Main program code : Youtube.py
  - This is the our main program file , which divides the whole actions into subparts as listed below :
      1. creating one log file to store the operations/errors occured on main program code validation 
      2. adding the few option settings to Chrome browser .
      3. opening web browser with 'requirement' data from 'youtube.properties' file on youtube 
      4. creating sql_databse class to store all video titels & its duration on to the file .
      5. once execution is done user can check the 'Youtube.db' file which generates & stored on the same directory .



## ***OnlineDataEntryJob Form Filling Work-Selenium-Python***

* Prerequisite package installation :
  - pip install configparser
  - pip install selenium
  
* Prerequisite program code :  mouse_operations.py
   - file contains all type of operations which human will do on web pages, so whenever its required we can specific operation/action based on requirement in our main program.
   - actions/operations/user_functions are listed below -->
     1. MoveToElement :- which moves the control to specific xpath 
     2. GetAttribute  :- which returns the attribute(either href,text,html link,name) based on input string value to the function
     3. LoadPage :- which waits the webpage to load a specific content/xpath to be present on the loaded webpage content.
     4. MouseClick :- which performs click operation on the specific element/xpath.
     5. Clear :- which performs clear operation on the specifc element.
     6. MouseClickAndSendKeys :- which performs click,clear operations then it will sends the given value on function to the element.
     7. MouseClickandSendKeysEnter :- which does the operation of MouseClickAndSendKeys, then hits the enter key.
     8. Dropdown_Options :- which will returns the all listed options on the particular xpath/element.
     9. scroll_down :- which scrolls down the webpage content by a mentioned offset value .
     
* Prerequisite property file : OnlineDataEntry.properties
  - file contains useful & input commands to the main program code , which contains the xpath address on it and also user can change the requirement based on his/her interest.
  
* Main program code : OnlineDataEntry.py
  - This is the our main program file , which divides the whole actions into subparts as listed below :
      1. Opening website & with provided login info from properties file 
      2. Adding the few option settings to Chrome browser .
      3. Opening web browser with 'form filling work' data from 'OnlineDataEntry.properties' file on onlinedataentry job portal. 
      4. First program will read the contents of table & also keep on adding the data/contens on to the field.


## Forward and Backward actions on Web page by using selenium+python

1. load the packages

   - selenium.webdriver
   - selenium.webdriver.common.keys 
  
2. create instance suitable driver & also provide its executable path as one of parameter to it, which you have it in your system

   - Chrome : webdriver.Chrome(executable_path="/chromedriver")
   - Internet explorer : webdriver.Ie()
   - Firefox : webdriver.Firefox() 
   
3. Load the url page link to the driver.

4. once webpage is loaded , search/enter some string onto the search bar , let it load

5. click the back button & again click forward button 

   - Just to checking the history of activity which is stored in the session or not.


## Close_And_Quit_Actions onto Web page by using selenium+python

1. load the packages

   - selenium.webdriver
   - from selenium.webdriver.chrome.options
   - from time import sleep module
  
2. create instance suitable driver & also provide its executable path as one of parameter to it, which you have it in your system

   - Chrome : webdriver.Chrome(executable_path="./chromedriver")
   - Internet explorer : webdriver.Ie()
   - Firefox : webdriver.Firefox() 
  
3. Create the options which is suitable for user to watch .
 
4. Load the url page link to the driver with predefined options which are predefined above.

5. once webpage is loaded & it will search for the "click button" , & once its clicked it will opens new tab.

6. finally based on user interest/option the program will close older web window or closes whole web browser & destroys the session.

   - driver.close :
   	     
         only the window that has focus is closed
   	
   - driver.quit : 
   	
         used to exit the browser, end the session, tabs, pop-ups etc.
