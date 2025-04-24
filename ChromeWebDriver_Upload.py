# test script that uploads a text document 




import os
    # provides a way to interact with the operating system
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


file_name = os.path.abspath('C:/Users/(your_username)/Desktop/Document.txt')
    # using the os module to make an absolute path to the text document


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/upload")


file_upload = driver.find_element(by=By.CSS_SELECTOR, value= "input[type='file']")
file_upload.send_keys(file_name)
    # selenium cant interact with the upload dialog, use send_key with full path of document
driver.find_element(By.ID, "file-submit").click()


input('press enter to quit')
driver.quit()
