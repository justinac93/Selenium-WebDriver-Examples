# test script thats adds text to an input field and then removes it




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
action = webdriver.ActionChains(driver)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


add_remove = driver.find_element(by=By.NAME, value='my-text')
add_remove.send_keys("abc123")
ActionChains(driver).move_to_element(add_remove).pause(5).perform()
    # mmoves mouse to web element and puase for 5 seconds before next action
add_remove.clear()
    # this removes text from the input field


input("press enter to quit")
driver.quit()
