from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()


driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpcountry = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='input-country']"))
)

# Select option from the dropdown using visible text
drpcountry_select = Select(drpcountry)
drpcountry_select.select_by_visible_text("India")

# Select option from the dropdown using value
drpcountry_select.select_by_value("10")

# Select option from the dropdown using index
drpcountry_select.select_by_index(13)  # Index

# Print all options in the dropdown

for option in drpcountry_select.options:
    print(option.text)


driver.quit()
