from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

try:
    # Open Google.com
    driver.get("https://www.google.com")
    
    # Wait for the page to load and verify the title
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    
    print(f"Page title: {driver.title}")
    print("Successfully opened Google.com!")
    
    # Keep the browser open for 5 seconds to see the result
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")
