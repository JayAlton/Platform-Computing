import time
from selenium import webdriver

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")

metrics = []
# Track presence time 
start_time = time.time()
presence_time = start_time
while True:#presence_time < 50: # seconds
    current_time = time.time()
    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    
    # Track scrolling
    scroll_height = driver.execute_script("return document.body.scrollHeight")  
    current_scroll = driver.execute_script("return window.pageYOffset")
    print(f"Scrolled {current_scroll}/{scroll_height} pixels")
    
    time.sleep(2) 

    # Track clicks   
   # buttons = driver.find_elements_by_tag_name("button")
   # num_clicks = 0

   # for button in buttons:
    #    button.click()
     #   num_clicks += 1
        
   # print(f"Number of clicks: {num_clicks}")
        
driver.quit()