from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

try:
    driver.get("https://www.facebook.com/")
    driver.maximize_window()

    username_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "pass")
    login_button = driver.find_element(By.NAME, "login")

    # Enter the corrected username and password
    username_field.send_keys("nandakoshore123@gmail.com")
    password_field.send_keys("Manu707@")
    login_button.click()

    # Wait for the "Create" button to be present
    create_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Create"][role="button"]'))
    )

    # Click on the "Create" button
    create_button.click()

    # Wait for the "Self" button to be present (you need to identify the correct selector)
    self_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Self"]'))
    )

    # Click on the "Self" button
    self_button.click()

finally:
    driver.quit()

