from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Edge WebDriver
driver = webdriver.Edge()

# Test Case 1: Grab page title and place title text in answer slot #1
driver.get("http://timvroom.com/selenium/playground/")
title_text = driver.title
driver.find_element(By.ID, "answer1").send_keys(title_text)

# Test Case 2: Fill out name section of the form to be Kilgore Trout
driver.find_element(By.ID, "name").send_keys("Kilgore Trout")

# Test Case 3: Set occupation on form to Sci-Fi Author
driver.find_element(By.ID, "occupation").send_keys("scifiauthor")

# Test Case 4: Count number of blue_boxes on the page after the form and enter into answer box #4
blue_box_count = len(driver.find_elements(By.CLASS_NAME, "bluebox"))
driver.find_element(By.ID, "answer4").send_keys(blue_box_count)

# Test Case 5: Click link that says 'click me'
driver.find_element(By.LINK_TEXT, "click me").click()

# Test Case 6: Find red box on its page, find class applied to it, and enter into answer box #6
red_box_class = driver.find_element(By.CSS_SELECTOR, "#redbox").get_attribute("class")
driver.find_element(By.ID, "answer6").send_keys(red_box_class)

# Test Case 7: Run JavaScript function as: ran_this_js_function() from your Selenium script
driver.execute_script("ran_this_js_function();")

# Test Case 8: Run JavaScript function as: got_return_from_js_function() from your Selenium script,
# take returned value and place it in answer slot #8
returned_value = driver.execute_script("return got_return_from_js_function();")
driver.find_element(By.ID, "answer8").send_keys(returned_value)

# Test Case 9: Mark radio button on form for written book? to Yes
driver.find_element(By.CSS_SELECTOR, "input[name='wrotebook'][value='wrotebook']").click()

# Test Case 10: Get the text from the Red Box and place it in answer slot #10
red_box_text = driver.find_element(By.ID, "redbox").text
driver.find_element(By.ID, "answer10").send_keys(red_box_text)

# Test Case 11: Which box is on top? orange or green -- place correct color in answer slot #11
orange_box_location = driver.find_element(By.ID, "orangebox").location
green_box_location = driver.find_element(By.ID, "greenbox").location
if orange_box_location["y"] < green_box_location["y"]:
    driver.find_element(By.ID, "answer11").send_keys("orange")
else:
    driver.find_element(By.ID, "answer11").send_keys("green")

# Test Case 12: Set browser width to 850 and height to 650
driver.set_window_size(850, 650)

# Test Case 13: Type into answer slot 13 yes or no depending on whether item by id of ishere is on the page
is_here_present = driver.find_elements(By.ID, "ishere")
if is_here_present:
    driver.find_element(By.ID, "answer13").send_keys("yes")
else:
    driver.find_element(By.ID, "answer13").send_keys("no")

# Test Case 14: Type into answer slot 14 yes or no depending on whether item with id of purplebox is visible
is_purplebox_visible = driver.find_element(By.ID, "purplebox").is_displayed()
if is_purplebox_visible:
    driver.find_element(By.ID, "answer14").send_keys("yes")
else:
    driver.find_element(By.ID, "answer14").send_keys("no")

# Test Case 15: Waiting game - click the link with link text of 'click then wait'
driver.find_element(By.LINK_TEXT, "click then wait").click()

# Use WebDriverWait to wait for the "click after wait" link to be present
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "click after wait")))

# Click the new link within 500 ms of it appearing to pass this test
driver.find_element(By.LINK_TEXT, "click after wait").click()

# ... (continue with the rest of your script)
time.sleep(20)
# Close the browser
driver.quit()
