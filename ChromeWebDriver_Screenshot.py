# snaps a screenshot of the webpage and saves it as a PNG




from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')


driver.get_screenshot_as_file('C:/Users/(your_username)/Desktop/example.png')
    # tells the webdriver to take a screenshot and save it as a PNG to a designated path


input('press enter to quit')
driver.quit()
