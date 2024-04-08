from selenium import webdriver
import time
import os

# Function to check for images in HTML content
def check_for_images_in_html(html_content):
    return '<img' in html_content.lower()

# Function to extend presence time if images are present
def extend_presence_time_for_images(driver, extend_time):
    html_content = driver.page_source
    if check_for_images_in_html(html_content):
        print(f"Images found. Extending presence time by {extend_time} seconds.")
        time.sleep(extend_time)
    else:
        print("No images found.")

# Define the website URLs
url_with_images = "https://www.britannica.com/technology/photography"

# Get the absolute path to the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
url_without_images = f"file://{current_directory}/without_images.html"

# Define extend time per image
extend_time = 10

# Initialize WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Open the website with images
driver.get(url_with_images)
start_time = time.time()
extend_presence_time_for_images(driver, extend_time)
end_time = time.time()
presence_time_with_images = end_time - start_time
print(f"Presence time with images: {presence_time_with_images:.2f} seconds")

# Open the website without images
driver.get(url_without_images)
start_time = time.time()
extend_presence_time_for_images(driver, extend_time)
end_time = time.time()
presence_time_without_images = end_time - start_time
print(f"Presence time without images: {presence_time_without_images:.2f} seconds")

# Close the WebDriver
driver.quit()
