# simple automation test script using Seleium WebDriver for Chrome 


from selenium import webdriver
    # importing classes and methods to control browser from the selenium library
from selenium.webdriver.chrome.options import Options
    # option class allows various settings specific to browser
from selenium.webdriver.common.by import By
    # the "By" class allows you to use locators




chrome_options = Options()
    # creates and instance of ChromeOptions class in Selenium
driver = webdriver.Chrome(options=chrome_options)
    # telling selenium to launch chrome with specific configurations
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    # request browser information
driver.set_window_size(800, 800)
    # sets the window size
driver.implicitly_wait(3)
    # makes WebDriver wait up to 3 seconds if an element is not immediately available on page


submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    # finds the first "button" element using CSS selector
submit_button.click()
    # performs a button click on selected element


input("press enter to quit")
    # asking user to press "enter" to close program
driver.quit()
    # this properly closes the webdriver and browser, saving resources

    







