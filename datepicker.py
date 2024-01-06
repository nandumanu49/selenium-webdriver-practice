from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# Switch to the iframe containing the datepicker
driver.switch_to.frame(0)

# Set the desired date (e.g., May 30, 2022)
year = "2024"
month = "December"
date = "30"

# Open the datepicker
datepicker = driver.find_element(By.XPATH, "//*[@id='datepicker']")
datepicker.click()

# Keep selecting next month until the desired month and year are reached
while True:
    current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if current_month == month and current_year == year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # Next arrow
        time.sleep(1)  # Add a short delay to allow the page to update

# Select the desired date
dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for ele in dates:
    if ele.text == date:
        ele.click()
        break

# Close the browser
driver.quit()
