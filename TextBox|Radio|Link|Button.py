from selenium.webdriver import Chrome

path = "/home/pycharm-community-2018.3.2/Selenium/chromedriver"    # path for chromedrive.exe
driver = Chrome(executable_path=path)
driver.get("https://www.facebook.com/")

driver.maximize_window()

# Enter data to TextBox

driver.find_element_by_name("fld_username").send_keys("helloworld")
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("abc@gmail.com")

driver.find_element_by_name("fld_username").clear()
driver.find_element_by_name("fld_username").send_keys("xyz")

# Click on Radio button | Checkbox | Button | Link

driver.find_element_by_xpath("//input[@value='office']").click()

driver.close()



