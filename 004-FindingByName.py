from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///C:/Users/twin5/Desktop/DojoAssignments/Python/Selenium/Exercise%20Files/CH02/html_code_02.html")

username = driver.find_element_by_name('username')
print("My input element is:")
print(username)

driver.close()
