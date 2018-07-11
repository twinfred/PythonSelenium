from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

searchBox = driver.find_element_by_class_name("gsfi")
searchBox.clear()
searchBox.send_keys("tim winfred")
searchBox.send_keys(Keys.RETURN)
time.sleep(8)

searchBox = driver.find_element_by_class_name("gsfi")
searchBox.clear()
searchBox.send_keys("selenium")
searchBox.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()
