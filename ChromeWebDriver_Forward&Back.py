# press submit button then goes back then forward 




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')


forward_back = driver.find_element(by=By.CSS_SELECTOR, value='button')
forward_back.click()
time.sleep(1)
driver.back()
    # tells the browser to go back a page
time.sleep(1)
driver.forward()
    # tells the browser to go forward a page


input('press enter to quit')
driver.quit()
