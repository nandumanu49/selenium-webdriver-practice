from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()

# Wait for some time (if needed)
time.sleep(5)

# Switch to the alert window
alert_window = driver.switch_to.alert

# Print the text of the alert
print(alert_window.text)

# Send keys to the prompt (type "welcome")
alert_window.send_keys("welcome")

# Accept the alert (click OK)
alert_window.accept()
# alert_window.dismiss()# to clik cancel

driver.quit()
