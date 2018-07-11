from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://wiki.python.org/moin/FrontPag'e)
time.sleep(3)

searchBox = driver.find_element_by_id('searchinput')
searchBox.clear()
searchBox.send_keys('Beginner')
searchBox.send_keys(Keys.RETURN)
time.sleep(3)

actionSelect = Select(driver.find_element_by_xpath('//*[@class="actionsmenu"]//select[1]'))
actionSelect.select_by_value('raw')
time.sleep(3)

driver.close()
