from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Function to check for presence of links in HTML content
def check_for_links_in_html(html_content):
    return '<a' in html_content.lower()

# Function to extend presence time if links are present
def extend_presence_time_for_links(driver, extend_time):
    html_content = driver.page_source
    if check_for_links_in_html(html_content):
        print(f"Links found. Extending presence time by {extend_time} seconds.")
        time.sleep(extend_time)
    else:
        print("No links found.")

# Define the website URLs
url_with_links = "https://en.wikipedia.org/wiki/Connor_McDavid"
current_directory = os.path.dirname(os.path.abspath(__file__))
url_without_links = f"file://{current_directory}/without_images.html"

# Define extend time per link
extend_time = 10

# Initialize WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Open the website with links
driver.get(url_with_links)
start_time = time.time()
extend_presence_time_for_links(driver, extend_time)
end_time = time.time()
presence_time_with_links = end_time - start_time
print(f"Presence time with links: {presence_time_with_links:.2f} seconds")

# Open the website without links
driver.get(url_without_links)
start_time = time.time()
extend_presence_time_for_links(driver, extend_time)
end_time = time.time()
presence_time_without_links = end_time - start_time
print(f"Presence time without links: {presence_time_without_links:.2f} seconds")

# Close the WebDriver
driver.quit()
