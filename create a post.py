import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")


email = 'nandakoshore123@gmail.com'
password = 'Manu707@'

# Wait for the email input to be present
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'email'))
)

# Find the email and password input fields and submit button
password_input = driver.find_element(By.ID, 'pass')
login_button = driver.find_element(By.NAME, 'login')


email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

# Wait for the "Create" button to be clickable
create_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="x14yjl9h xudhj91 x18nykt9 xww2gxu x6s0dn4 x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x3nfvp2 xl56j7k x1n2onr6 x1hr4nm9 x1vqgdyp x100vrsf"]'))
)

# Click the "Create" button
create_button.click()

# Wait for a while to see the create post page (you may adjust this time)
time.sleep(5)


driver.quit()
=======
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")


email = 'nandakoshore123@gmail.com'
password = 'Manu707@'

# Wait for the email input to be present
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'email'))
)

# Find the email and password input fields and submit button
password_input = driver.find_element(By.ID, 'pass')
login_button = driver.find_element(By.NAME, 'login')


email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

# Wait for the "Create" button to be clickable
create_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="x14yjl9h xudhj91 x18nykt9 xww2gxu x6s0dn4 x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x3nfvp2 xl56j7k x1n2onr6 x1hr4nm9 x1vqgdyp x100vrsf"]'))
)

# Click the "Create" button
create_button.click()

# Wait for a while to see the create post page (you may adjust this time)
time.sleep(5)


driver.quit()

