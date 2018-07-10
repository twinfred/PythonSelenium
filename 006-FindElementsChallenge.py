from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.seleniumhq.org/')

q_id = driver.find_element_by_id('q')
q_name = driver.find_element_by_name('q')
title_xpath = driver.find_element_by_xpath('/html/body/div[@id="container"]/div[@id="mBody"]/div[@id="mainContent"]/h2[1]')
title_xpath_2 = driver.find_element_by_xpath('//*[@id="mainContent"]/h2[1]')
sponsors_class = driver.find_element_by_class_name('selenium-sponsors')

print("by id:")
print(q_id)
print("by name:")
print(q_name)
print("by xpath:")
print(title_xpath)
print(title_xpath_2)
print("by class:")
print(sponsors_class)

driver.close()
