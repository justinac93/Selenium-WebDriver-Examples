# this test script prints and saves a PDF as a binary and writes to a file




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.print_page_options import PrintOptions
import base64
    # provides functions to encode/decode binary to printable ASCII characters


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')


print_options = PrintOptions() 
    # this allows to set parameters like height, width, scale
print_options.page_ranges = ['1']
    # prints only 1 page
pdf = driver.print_page(print_options)
    # generates PDF and stores it


with open("output.pdf", "wb") as f:
    # opens PDF file called 'output' in 'write binary(wb)' mode
    f.write(base64.b64decode(pdf))
        # decodes into raw binary data then writes to a file


input('press enter to quit')
driver.quit()
