from selenium import webdriver
import time

# Function to check for keyword and extend presence time if found
def extend_presence_time(driver, keyword, extend_time):
    start_time = time.time()
    page_source = driver.page_source
    if keyword.lower() in page_source.lower():
        print(f"Keyword '{keyword}' found. Extending presence time by {extend_time} seconds.")
        time.sleep(extend_time)
    else:
        print(f"Keyword '{keyword}' not found.")
    end_time = time.time()
    presence_time = end_time - start_time
    print(f"Presence time: {presence_time:.2f} seconds")

# Define the website URLs
url_with_keyword = "https://studentaid.gov/"
url_without_keyword = "https://www.espn.com/"

# Define keyword and extend time
keyword = "student"
extend_time = 10

# Initialize WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Open the website with the keyword
driver.get(url_with_keyword)
extend_presence_time(driver, keyword, extend_time)

# Open the website without the keyword
driver.get(url_without_keyword)
extend_presence_time(driver, keyword, extend_time)

# Close the WebDriver
driver.quit()
