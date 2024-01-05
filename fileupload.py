from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Set up the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# Find the Google Lens icon element by its class name
google_lens_icon = driver.find_element(By.XPATH, "nDcEnd")

# Click on the Google Lens icon
google_lens_icon.click()
# Specify the file path to be uploaded
file_path = r"C:\path\to\your\image.jpg"

# Use send_keys to attach the file to the file input
upload_input.send_keys(os.path.abspath(file_path))

# Wait for some time to see the uploaded file
time.sleep(5)

# Optionally, wait for some time to let the next page load
# time.sleep(5)

# Perform other actions or assertions as needed

# Close the browser window
driver.quit()
