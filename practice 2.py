from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Edge()  # You can use other browsers as well

# Navigate to the provided URL
driver.get("https://www.saucedemo.com/inventory.html")

# Fill in the username and password fields
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

# Click the login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Test Case 1: Click the "Add to cart" button
add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
add_to_cart_button.click()

# Test Case 2: Select a filter option from the dropdown
filter_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
filter_dropdown.select_by_value("za")  # Change the value as needed

# Test Case 3: Open the shopping cart link
shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
shopping_cart_link.click()

# Test Case 4: Click the "Checkout" button
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

# Test Case 5: Fill the "First Name", "Last Name", and "Zip/Postal Code" fields and continue
first_name_field = driver.find_element(By.ID, "first-name")
first_name_field.send_keys("nanda")

last_name_field = driver.find_element(By.ID, "last-name")
last_name_field.send_keys("Manoj")

postal_code_field = driver.find_element(By.ID, "postal-code")
postal_code_field.send_keys("515541")
time.sleep(2)

continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
continue_button.click()
time.sleep(2)

# Test Case 6: Perform logout
menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()

# Wait for the menu to be visible (you may need to adjust the timeout)
menu_visible = EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/div'))
WebDriverWait(driver, 10).until(menu_visible)

# Click the logout button
logout_button_xpath = '/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]'
logout_button = driver.find_element(By.XPATH, logout_button_xpath)
logout_button.click()


# Close the browser window
driver.quit()

