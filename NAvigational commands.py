<<<<<<< HEAD
from selenium import webdriver


driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Perform a search on Google
search_box = driver.find_element("name", "q")
search_box.send_keys("cricbuzz")
search_box.submit()

# Open a new tab and switch to it
driver.execute_script("window.open('about:blank', '_blank');")
driver.switch_to.window(driver.window_handles[1])

# Navigate to Cricbuzz in the new tab
driver.get("https://www.cricbuzz.com")

# Close the new tab
driver.close()

# Switch back to the original tab
driver.switch_to.window(driver.window_handles[0])

# Navigate back
driver.back()

# Navigate forward
driver.forward()

driver.quit()
=======
from selenium import webdriver


driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Perform a search on Google
search_box = driver.find_element("name", "q")
search_box.send_keys("cricbuzz")
search_box.submit()

# Open a new tab and switch to it
driver.execute_script("window.open('about:blank', '_blank');")
driver.switch_to.window(driver.window_handles[1])

# Navigate to Cricbuzz in the new tab
driver.get("https://www.cricbuzz.com")

# Close the new tab
driver.close()

# Switch back to the original tab
driver.switch_to.window(driver.window_handles[0])

# Navigate back
driver.back()

# Navigate forward
driver.forward()

driver.quit()
>>>>>>> origin/main
