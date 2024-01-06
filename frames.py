from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navigate to the target URL
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# Maximize the browser window
driver.maximize_window()

# Wait for the frame with ID "packageListFrame" to be present
try:
    WebDriverWait(driver, 60).until(EC.frame_to_be_available_and_switch_to_it("packageListFrame"))
except:
    print("TimeoutException: Unable to find the frame within the specified time.")

# Click on the link with text "org.openqa.selenium"
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

# Rest of your code...

# Close the browser
driver.quit()
