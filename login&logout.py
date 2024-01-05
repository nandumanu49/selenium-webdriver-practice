<<<<<<< HEAD
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

email = 'nandakoshore123@gmail.com'
password = 'Manu707@'

# Wait for the email input to be present
email_input = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.ID, 'email'))
)

# Find the email and password input fields and submit button
password_input = driver.find_element(By.ID, 'pass')
login_button = driver.find_element(By.NAME, 'login')

# Enter the credentials and click the login button
email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

# Wait for the profile button to be clickable
profile_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and @tabindex="0"]'))
)

# Use ActionChains to move to the element and then click
action = ActionChains(driver)
action.move_to_element(profile_button).click().perform()

# Print a message to indicate whether the element is clicked
if "active" in profile_button.get_attribute("class"):
    print("Profile button clicked successfully!")
else:
    print("Profile button click unsuccessful. Element may not have been clicked.")

# Add a delay for visual inspection (you can adjust the time as needed)
time.sleep(10)

driver.quit()

=======
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

email = 'nandakoshore123@gmail.com'
password = 'Manu707@'

# Wait for the email input to be present
email_input = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.ID, 'email'))
)

# Find the email and password input fields and submit button
password_input = driver.find_element(By.ID, 'pass')
login_button = driver.find_element(By.NAME, 'login')

# Enter the credentials and click the login button
email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

# Wait for the profile button to be clickable
profile_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and @tabindex="0"]'))
)

# Use ActionChains to move to the element and then click
action = ActionChains(driver)
action.move_to_element(profile_button).click().perform()

# Print a message to indicate whether the element is clicked
if "active" in profile_button.get_attribute("class"):
    print("Profile button clicked successfully!")
else:
    print("Profile button click unsuccessful. Element may not have been clicked.")

# Add a delay for visual inspection (you can adjust the time as needed)
time.sleep(10)

driver.quit()

>>>>>>> origin/main
