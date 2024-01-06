from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# Or using partial link text
driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

# Finding number of links in a page
# links = driver.find_elements(By.XPATH, '//a')
links = driver.find_elements(By.TAG_NAME, "a")
print("Total number of links:", len(links))

# Print all the link names
for link in links:
    print(link.text)


driver.quit()
