from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (assuming ChromeDriver is used)
driver = webdriver.Chrome()

# URL of the webpage with the file uploader
url = "https://the-internet.herokuapp.com/upload"

# File path to the image you want to upload
file_path = r"C:\Users\nadu4\OneDrive\Pictures\Screenshots\Screenshot (663).png"

# Open the webpage
driver.get(url)

# Find the file input element using its ID ("file-upload")
file_input = driver.find_element(By.ID, "file-upload")

# Provide the file path for upload
file_input.send_keys(file_path)

# Find the submit button and click it
submit_button = driver.find_element(By.ID, "file-submit")
submit_button.click()

# Optional: Wait for some time to see the result or perform additional actions

# Close the WebDriver
driver.quit()
