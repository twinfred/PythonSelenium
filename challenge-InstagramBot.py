from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.instagram.com')
sleep(2)

login_link = driver.find_element_by_xpath('//*/a[text()="Log in"]')
login_link.click()
sleep(2)

username_input = driver.find_element_by_name('username')
username_input.clear()
username_input.send_keys('enterUsernameHere')
sleep(2)

password_input = driver.find_element_by_name('password')
password_input.clear()
password_input.send_keys('enterPasswordHere')
sleep(2)

login_btn = driver.find_element_by_xpath('//*/button[text()="Log in"]')
login_btn.click()
sleep(2)

driver.get('https://www.instagram.com/explore/tags/monkey/')
sleep(1)

body_element = driver.find_element_by_tag_name('body')
for x in range(5):
    body_element.send_keys(Keys.END)
    sleep(2)
    body_element.send_keys(Keys.HOME)
    sleep(2)

first_img = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a')
first_img.click()
sleep(2)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'coreSpriteHeartOpen'))
        )
finally:
    like_btn = driver.find_element_by_class_name('coreSpriteHeartOpen')
    sleep(2)
    like_btn.click()
    sleep(1)
    for y in range(45):
        next_btn = driver.find_element_by_xpath('//*/a[text()="Next"]')
        next_btn.click()
        sleep(2)
        like_btn.click()
        sleep(1)

driver.quit()
