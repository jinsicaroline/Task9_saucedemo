from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the webpage
url = "https://www.saucedemo.com/"
driver.get(url)

# Log in with credentials
username = "standard_user"
password = "secret_sauce"

# Find the username field and enter the username
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
username_field.send_keys(username)

# Find the password field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load after login
WebDriverWait(driver, 10).until(EC.title_contains("Swag Labs"))

# Fetch and print the title of the webpage
title = driver.title
print("Title of the webpage:", title)

# Close the WebDriver
driver.quit()
