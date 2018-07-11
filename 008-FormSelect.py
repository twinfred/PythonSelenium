from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('file:///C:/Users/twin5/Desktop/DojoAssignments/Python/Selenium/Exercise%20Files/CH03/03_02/html_code_03_02.html')
time.sleep(2)

select = Select(driver.find_element_by_name('numReturnSelect'))
options = select.options

print("your options are:")
print(options)
time.sleep(4)

select.select_by_index(4)
time.sleep(2)

select.select_by_visible_text("200")
time.sleep(2)

select.select_by_value("250")
time.sleep(2)

submit_button = driver.find_element_by_name("continue")
submit_button.submit()
time.sleep(2)

driver.close()
