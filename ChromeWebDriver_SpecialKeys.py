# this script uses SPECIAL_KEYS in a loop to highlight each element on the page by pressing "TAB"




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
    # simulates keyboard keys
from selenium.webdriver.common.action_chains import ActionChains
    # simulate user interactions like hovering and mouse movement
import time
    # standard python library, usesd for timing, delays, timestamps


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


button_press = 15
for key in range(button_press):
    action.key_down(Keys.TAB).perform()
    time.sleep(1)
        # using 'range' in a loop to press TAB until it reaches the value in 'button_press'


input("press enter to quit")
driver.quit()
