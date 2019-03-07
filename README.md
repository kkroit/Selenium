# Selenium


pip install selenium


Free Tool, mainly for functional/regression automation testing of web-based application

Advantages of Selenium:-
--------------------------------------
  Free
  Support multiple Programming languages
  Support Multiple Browsers
  Can execute test cases in parallel

Dis-Advantages of Selenium:-
--------------------------------------
  Support only web-based application
  programming skills are mandatory
  not user-friendly
  no official support is available

Components of Selenium
-------------------------------------
  Selenium IDE
  Selenium RC --> Can execute test cases on different browsers
  Selenium Webdriver
  Selenium Grid --> Execute test case in parallel
  
History of Selenium
--------------------------------------
  Selenium 1 ----> IDE, RC, Grid
  Selenium 2 ----> IDE, RC, Webdriver, Grid
  Selenium 3 ----> IDE, Webdriver, Grid

Selenium IDE
--------------------------------------
  Selenium IDE is used for Record and Play
  Support Chrome as well as Firefox
  can record a script, can execute a script
  can be used to perform basic tasks without programming
  save the script and use it whenever required.
  
Element Locators
----------------------------------------
  With the help of it, we can locate (search) elements uniquely on the page.
  Different type of locators are: Id, Name, Class name, Link, CSS, XPath 
  "Selenium IDE" for Firefox and "CSS and XPath checker" for chrome to locate the element.
  
Selenium IDE use for Locators
----------------------------------------
  We can write Locators on Selenium IDE
  We can highlight elements search by locators
  
CSS Locator
----------------------------------------

  Option 1 --> CSS = tag with id (css=input/div#id or css=input#id)
  Option 2 --> CSS = tag with class (css=input/div.class or css=input.class) (Note: Inplace of space use '.')
  Option 3 --> CSS = tag with any attribute (css=input/div[type='email'])
  Option 4 --> CSS = tag with class with any attribute (css=input.class[type='email'])
  Option 5 --> CSS = tag with id with any attribute (css=input#id[type='email'])
  
XPATH
------------------------------------------

  Group 1 --> 
  
      --> Xpath with single attribute (//tagname[@attribute='value'])
      --> Xpath with multiple attributes (//tagname[@attribute1='value' or @attribute2='value']) 
                                                              use 'and' as well in place of 'or'
      --> Use * on a place of the attribute (//tagname[@*='value'])
      --> Use * on a place of the tag name (//*[@attribute='value'])
      --> Partial value of attributes :- (//tagname[contains(@type,'value')])
      
  Group 2 -->
  
      --> Xpath with inner text  (//tagname[text()='value'])
      --> Xpath with inner text(contains) (//tagname[contains(text(),'value')])
      --> Xpath with inner text(not contains) (//tagname[not(contains(text(),'value'))])
      --> Xpath with inner text(starts-with) (//tagname[starts-with(text(),'value')])
      
  Group 3 -->
  
      --> Multiple XPath for the same element  --> different xpath for different browsers 
                            //tagname[@attribute='value']|//tagname[@attribute='value_c']
      --> Dynamic Xpath using contains (//tagname[contains(@attribute,'value')])
      
  Group 4 -->
  
      --> Locating element through its parent (//tagname[@attribute='value']/tbody/tr[2]/input)
                                                          (//tagname[@attribute='value']//input)
      --> Locating element through its child (//tagname[@attribute='value']/parent::td/parent::tr)
      
  Group 5 -->
      --> Locating elements through siblings 
              (//tagname[@attribute='value']/preceding-sibling::select)
              (//tagname[@attribute='value']/following-sibling::select)
