# finds a text web element and returns a boolean statement




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
    # waits for an element to load on page, if not found, throws aa timeout exception 
from selenium.webdriver.support import expected_conditions as EC
    # waits for specific conditions until a defined task is complete, returns boolean
from selenium.webdriver.support.ui import WebDriverWait
    # waits for web elements to appear before test script 


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")


try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "gNO89b")))
    print("text found")
        # waits 3 seconds, finds element by CLASS_NAME, if True, prints text 
except TimeoutException:
    print("text not found")
        # if element not found, False, prints text
finally:
    input("press -enter- to quit")
    driver.quit()
        # closes Chrome and WebDriver, saves resources
