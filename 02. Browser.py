
'''
1. chrome.exe version should be in between the pre-installed chrome, in other words, it should be matched with chrome.
2. To install Chrome.exe file "https://sites.google.com/a/chromium.org/chromedriver/downloads"
3. For firefox --> Gecko driver "https://github.com/mozilla/geckodriver/"
'''


# Chrome
# ----------------------------

from selenium.webdriver import Chrome

path = "/home/pycharm-community-2018.3.2/Selenium/chromedriver"    # path for chromedrive.exe
driver = Chrome(executable_path=path)
driver.get("https://www.facebook.com/")
driver.maximize_window()
#driver.close()
driver.quit()

# Firefox
# ----------------------------

from selenium.webdriver import Firefox

path = "/home/pycharm-community-2018.3.2/Selenium/geckodriver"     # path for Firefox Gecko Driver
driver = Firefox(executable_path=path)
driver.get("https://www.facebook.com/")
driver.maximize_window()
#driver.close()
driver.quit()
