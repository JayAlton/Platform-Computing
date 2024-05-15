import time
from selenium import webdriver
import collections
import csv

def writeToCSV(filename : str, metrics : dict):
    with open(file=filename, mode="w", newline="") as fp:
        # Create a writer object
        writer = csv.DictWriter(fp, fieldnames=metrics.keys())

        # Write the header row
        writer.writeheader()

        # Write the data row
        writer.writerow(metrics)


def main():
    # Initialize browser
    driver = webdriver.Chrome()
    
    print("web driver init")
    
    # Navigate to your website 
    driver.get("http://localhost:3000/")

    # Track presence time 
    metrics = collections.defaultdict(list)
    SAMPLE_SIZE = 10
    count = 0
    start_time = time.time()
    presence_time = start_time
    while count < SAMPLE_SIZE:
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

        count += 1
        time.sleep(2) 

    driver.quit()
    metrics["Timestamp"].append(current_time)
    metrics["Presence time (Seconds)"].append(presence_time)
    metrics["Scrolling (Pixels)"].append(current_scroll/scroll_height)
    metrics["Clicks"].append(num_clicks)

    print(metrics)
    writeToCSV("metrics.csv",metrics)

if __name__ == "__main__":
    main()