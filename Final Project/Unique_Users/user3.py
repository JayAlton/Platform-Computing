# user1.py (similar modification for other user files)

from selenium.webdriver.common.by import By
import time
import re

def userAction(driver, base_url):
    driver.get(base_url)
    total_reward_time = 0
    reward_time = 10
    keywords = ["CSUSB", "student", "Soccer"]
    img_tag = "img"
    link_tag = "a"

    # Perform actions based on keywords
    total_reward_time += userActions("KEYWORD", driver, reward_time, keywords)

    # Perform actions based on images
    total_reward_time += userActions("IMAGE", driver, reward_time, img_tag)

    # Perform actions based on links
    total_reward_time += userActions("LINK", driver, reward_time, link_tag)

    # Sleep for total reward time
    time.sleep(total_reward_time)

def userActions(action, driver, reward_time, req_list):
    total_reward_time = 0

    if action.upper() == "KEYWORD":
        for keyword in req_list:
            num_occurrences = findKeyword(driver, keyword)
            total_reward_time += reward_time * num_occurrences
    elif action.upper() == "IMAGE":
        num_images = countElem(driver, req_list)
        total_reward_time += reward_time * num_images
    elif action.upper() == "LINK":
        num_links = countElem(driver, req_list)
        total_reward_time += reward_time * num_links

    return total_reward_time

def findKeyword(driver, keyword):
    # Find all paragraph elements on the page
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')

    # Get the text from each paragraph
    visible_text = [p.text.lower() for p in paragraphs]

    # Create a regular expression pattern to match whole words
    pattern = r'\b{}\b'.format(keyword.lower())

    # Count the keyword in visible text
    num_occurrences = sum(len(re.findall(pattern, text)) for text in visible_text)

    return num_occurrences

def countElem(driver, tag_name):
    # Get all elements for the specified tag_name
    elements = driver.find_elements(By.TAG_NAME, tag_name)

    # Total number of elements
    total_length = len(elements)

    return total_length
