from selenium import webdriver

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) Count number of rows & columns
noofRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
no0fColumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
print(noofRows)  # 7
print(no0fColumns)  # 4


data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)

# 3) Read all the rows & Columns data
print("Printing all the rows and columns data. .")

for r in range(2, noofRows + 1):
    for c in range(1, no0fColumns + 1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='                 ')
        print()

# Close the browser
driver.close()
