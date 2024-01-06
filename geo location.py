from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/geolocation")

# Click the "Where am I?" button to trigger geolocation
location_button = driver.find_element(By.XPATH, "//button[text()='Where am I?']")
location_button.click()

# Wait for the alert to appear
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
alert = wait.until(EC.alert_is_present())

# Allow the geolocation permission
alert.accept()

# Wait for the geolocation data to be retrieved (you may need to adjust the wait time)
time.sleep(5)

# Retrieve latitude and longitude values
latitude_element = driver.find_element(By.XPATH, "//div[@id='lat-value']")
longitude_element = driver.find_element(By.XPATH, "//div[@id='long-value']")

latitude = latitude_element.text
longitude = longitude_element.text

# Print or use the latitude and longitude values as needed
print("Latitude:", latitude)
print("Longitude:", longitude)

driver.quit()

