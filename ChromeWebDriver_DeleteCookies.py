# this script deleats all browser cookies and login info, good for avoiding inconsistent tests




from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')


driver.delete_all_cookies()
    # deletes stored information


input('press enter to quit')
driver.quit()
