# test scipt that grabs the attributes of a web element using a loop




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


get_attribute = driver.find_element(By.NAME, value='my-text')
for atri in ['type', 'id', 'class']:
    print(f"{atri}: {get_attribute.get_attribute(atri)}")
        # for loop that prints each attribute as a dictionary


input('press enter to quit')
driver.quit()
