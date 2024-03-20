import time
from selenium import webdriver

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")

# Track presence time 
start_time = time.time()
presence_time = start_time
while True:
    current_time = time.time()
    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    
    # Track scrolling
    scroll_height = driver.execute_script("return document.body.scrollHeight")  
    current_scroll = driver.execute_script("return window.pageYOffset")
    print(f"Scrolled {current_scroll}/{scroll_height} pixels")
    
    # Access numClicks from the global scope
    num_clicks = driver.execute_script("return window.numClicks;")
    print(f"Number of clicks: {num_clicks}")
    
    time.sleep(2) 

driver.quit()
