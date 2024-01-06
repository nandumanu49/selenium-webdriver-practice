from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/download_secure")

# Get all the links on the page that lead to file downloads
download_links = driver.find_elements(By.XPATH, "//div[@class='example']//a")

# Iterate through each download link and download the file
for link in download_links:
    file_name = link.text
    link.click()

    # Wait for the file to be downloaded (you may need to adjust the wait time)
    # This is a simple wait, and you may want to use a more robust mechanism
    driver.implicitly_wait(5)

driver.quit()
