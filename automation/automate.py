from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime

# User Configurations
YOUR_NAME = "Bibek Pandey"  # Replace with your name
LINKEDIN_POST_LINKS = {
    11: "https://www.linkedin.com/posts/bibek-pandey-43313723b_111daysoflearningforchange-day11learningforchange-activity-7321569032220864513-d_i3",
    12: "https://www.linkedin.com/posts/bibek-pandey-43313723b_111daysoflearningforchange-day12learningforchange-activity-7321946878311383040-f9XD",
    13: "https://www.linkedin.com/posts/bibek-pandey-43313723b_111daysoflearningforchange-day13learningforchange-activity-7322291723861127168-minH",
    14: "https://www.linkedin.com/posts/bibek-pandey-43313723b_111daysoflearningforchange-day14learningforchange-activity-7322686841755713536-BxJ2",
    15: "https://www.linkedin.com/posts/bibek-pandey-43313723b_111daysoflearningforchange-day15learningforchange-activity-7323053575171989505-33It"
}

QUERY_TEXT = "nothing"  # Replace with your query

# Google Form URL
FORM_URL = "https://docs.google.com/forms/d/1iTdki5iaBHOnrFQrn_GyKdaSLoJUkMKnWNsuQ6gNaIw/viewform?edit_requested=true"

# Setting up WebDriver (Chrome)
driver = webdriver.Chrome()
driver.get(FORM_URL)
driver.maximize_window()

try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    print("Form loaded successfully.")

    # Switching to nested iframes if any
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        driver.switch_to.frame(iframe)

    print("Switched to iframe successfully (if any).")

    # Using JavaScript to directly access and fill fields with fallback
    try:
        driver.execute_script("document.querySelector('input[aria-label*=\"Name\"], input[type=text]').value = arguments[0];", YOUR_NAME)
    except:
        print("Failed to set Name field using JS. Trying another method.")
        name_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Name') or @type='text']"))
        )
        name_field.send_keys(YOUR_NAME)

    # Selecting Stack (Data Science) using JavaScript
    driver.execute_script("document.querySelector('[data-value=\"Data Science\"]')?.click();")

    # Choosing LinkedIn for posting
    driver.execute_script("document.querySelector('[data-value=\"LinkedIn\"]')?.click();")

    # Day and Link
    day_count = int(input("Enter the day count (e.g., 11, 12, 13): "))
    link = LINKEDIN_POST_LINKS.get(day_count, "")

    # Setting Link using JavaScript
    driver.execute_script("document.querySelector('input[aria-label*=\"Link to your post\"]')?.value = arguments[0];", link)

    # Selecting Date (Today's Date)
    today_date = datetime.now().strftime("%Y-%m-%d")
    driver.execute_script("document.querySelector('input[type=date]')?.value = arguments[0];", today_date)

    # Day Count Selection
    driver.execute_script(f"document.querySelector('[data-value=\"{day_count}\"]')?.click();")

    # Entering Queries
    driver.execute_script("document.querySelector('input[aria-label*=\"Any Queries\"]')?.value = arguments[0];", QUERY_TEXT)

    # Submitting the form
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()

    print("Form submitted successfully!")
    time.sleep(5)

except TimeoutException:
    print("Form loading took too much time. Please check your internet connection or form link.")

except Exception as e:
    print("An unexpected error occurred:", str(e))

finally:
    driver.quit()
