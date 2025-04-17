# enters text into a webpage input field




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


pass_box = driver.find_element(by=By.NAME, value="my-password")
pass_box.send_keys("1234567")
    # enters text into password box


input("press -enter- to quit")
driver.quit()
