from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

# Find all links on the page
all_links = driver.find_elements(By.TAG_NAME, 'a')

# Initialize a counter for broken links
count = 0

# Loop through all links and check if they are valid or broken
for link in all_links:
    url = link.get_attribute('href')
    try:
        # Send a HEAD request to check if the link is valid
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, "is a broken link")
        count += 1
    else:
        print(url, "is a valid link")

# Print the total number of broken links
print("Total number of broken links:", count)

driver.quit()
