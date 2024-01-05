<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()


search_results = driver.find_elements(By.CSS_SELECTOR, "h3")

if search_results:
    print("Search Results:")
    for index, result in enumerate(search_results, 1):
        print(f"{index}. {result.text}")
else:
    print("No search results found.")


driver.quit()
=======
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()


search_results = driver.find_elements(By.CSS_SELECTOR, "h3")

if search_results:
    print("Search Results:")
    for index, result in enumerate(search_results, 1):
        print(f"{index}. {result.text}")
else:
    print("No search results found.")


driver.quit()
>>>>>>> origin/main
