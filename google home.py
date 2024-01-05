<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

# Open Google's homepage
driver.get("https://www.google.com")

# Find the search input element by name
search_box = driver.find_element("name", "q")

# Type a search query
search_box.send_keys("Selenium WebDriver")

# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for a moment (you can use WebDriverWait for more complex scenarios)
driver.implicitly_wait(5)

# Print the title of the current page
print("Current Page Title:", driver.title)

# Find multiple search results using the class name
search_results = driver.find_elements("class name", "tF2Cxc")

# Print the text of each search result
for result in search_results:
    print(result.text)

driver.quit()
=======
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

# Open Google's homepage
driver.get("https://www.google.com")

# Find the search input element by name
search_box = driver.find_element("name", "q")

# Type a search query
search_box.send_keys("Selenium WebDriver")

# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for a moment (you can use WebDriverWait for more complex scenarios)
driver.implicitly_wait(5)

# Print the title of the current page
print("Current Page Title:", driver.title)

# Find multiple search results using the class name
search_results = driver.find_elements("class name", "tF2Cxc")

# Print the text of each search result
for result in search_results:
    print(result.text)

driver.quit()
>>>>>>> origin/main
