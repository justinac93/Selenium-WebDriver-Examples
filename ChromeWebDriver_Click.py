# simple automation test script using Seleium WebDriver for Chrome 




from selenium import webdriver
# importing classes and methods to control browser from the selenium library
from selenium.webdriver.chrome.service import Service
# service class responsible for starting and managing ChromeDriver executable
from selenium.webdriver.chrome.options import Options
# option class allows various settings specific to browser
from selenium.webdriver.common.by import By
# the "By" class allows you to use locators


chrome_options = webdriver.ChromeOptions()
# creates and instance of ChromeOptions class in Selenium
chrome_options.add_experimental_option("detach", True)
# stops the finished script from closing the browser window
driver = webdriver.Chrome(options=chrome_options)
# telling selenium to launch chrome with specific configurations
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# request browser information
driver.set_window_size(800, 800)
# sets the window size
driver.implicitly_wait(1)
# makes WebDriver wait up to 1 second if an element is not immediately available on page


submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# finds the first "button" element using CSS selector
submit_button.click()
# performs a button click
    







