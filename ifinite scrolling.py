from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/infinite_scroll")

try:
    # Scroll down to the bottom of the page to trigger loading more content
    while True:
        # Perform scroll by sending the SPACE key to the body element
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)

        # Wait for a brief moment to allow content to load
        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'jscroll-added')))
except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C) to stop scrolling
    pass
finally:

    driver.quit()


