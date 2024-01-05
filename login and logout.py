from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

# Replace these with your Facebook credentials
username = "9110529009"
password = "Manu7075@"

# Path to your EdgeDriver executable


# Start the Edge browser
driver = webdriver.Edge()

# Open Facebook login page
driver.get("https://www.facebook.com")

# Find the username and password input fields and login button
username_field = driver.find_element("id", "email")
password_field = driver.find_element("id", "pass")
login_button = driver.find_element("name", "login")

# Enter credentials and click login
username_field.send_keys(username)
password_field.send_keys(password)
login_button.click()


# Wait for the home page to load after login
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="your-unique-element-id"]')))
except TimeoutException:
    print("Timed out waiting for the home page to load")
search_input = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_GK"]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/label/input'))
)

# Type "hii" into the search input field
search_input.send_keys("hii")

# Perform any additional actions if needed, e.g., pressing Enter to submit the search
# search_input.send_keys(Keys.RETURN)

# Continue with the rest of your script

# Close the browser
driver.quit()


