from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///C:/Users/twin5/Desktop/DojoAssignments/Python/Selenium/Exercise%20Files/CH02/html_code_02.html")

login_form = driver.find_element_by_id('loginForm')
print("My login form variable is:")
print(login_form)

driver.close()
