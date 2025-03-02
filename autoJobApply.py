import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Brave Browser path on OS
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

# Set Brave as the browser
chrome_options = Options()
chrome_options.binary_location = brave_path  # Set the Brave binary


# Get Brave profile path from environment variable
brave_profile_path = os.getenv('BRAVE_PROFILE_PATH', '/default/path/to/BraveProfile')
chrome_options.add_argument(f"user-data-dir={brave_profile_path}")  # Path to your Brave profile

# Path to Chromedriver (Ensure this matches Brave's Chromium version)
chromedriver_path = "/usr/local/bin/chromedriver"  # Update this path if necessary

# Initialize WebDriver with the specified Chromedriver and options
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


# Define multiple job roles to search for
job_roles = ["Systems Administrator", "IT Support Specialist"]



### LINKEDIN FUNCTIONS ###
def search_linkedin_jobs(job_title):
    print(f"Searching for {job_title} jobs on LinkedIn...")
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(2)
    
    # Find the search box and enter the job title
    search_box = driver.find_element(By.XPATH, "//input[contains(@class, 'jobs-search-box__text-input')]")
    search_box.clear()
    search_box.send_keys(job_title)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

def apply_linkedin_jobs():
    print("Applying for jobs on LinkedIn...")
    
   # Wait for button to be clickable using class name
    apply_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "jobs-apply-button"))
    )
    apply_button.click()
    time.sleep(2)



for role in job_roles:
    search_linkedin_jobs(role)
    apply_linkedin_jobs()
    


