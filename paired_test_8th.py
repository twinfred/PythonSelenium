from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
chrome.get('https://www.twitter.com/login')
sleep(2)

username_input = chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
username_input.send_keys('enterUsernameHere')
sleep(2)

password_input = chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
password_input.send_keys('enterPasswordHere')
sleep(2)

login_button = chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
login_button.click()
sleep(2)

chrome.get('https://www.twitter.com/corywysz')
x = chrome.find_element_by_class_name('HeartAnimation')
x.click()
sleep(2)

chrome.close()
