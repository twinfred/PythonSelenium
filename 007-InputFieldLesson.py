from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://python.org")

searchBox = driver.find_element_by_name('q')
searchBox.clear()
searchBox.send_keys("selenium")
searchBox.send_keys(Keys.RETURN)
time.sleep(6)

driver.close()
