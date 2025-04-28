# this can be used to test that the expected landing page loads




from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


check_title = driver.title
check_url= driver.current_url
print(f"{check_url}\n {check_title}")
  # checks the url and title and prints the results

input('press enter to cancel')
driver.quit()
