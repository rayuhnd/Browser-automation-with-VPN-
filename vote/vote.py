#

"""from selenium import webdriver

browser = webdriver.Firefox()
url = 'https://sveriges-storsta.miljonlotteriet.se/competition/sveriges-storsta-kattfantast?nominee=660aa39bef8504bffa7c0ec2'

browser.get(url)


XPATH_X = '/html/body/main/section/div/section/div/div[1]/div/div/div/div[2]/div[194]/div[2]/div[2]/div/div/div/button/div'

next_button = browser.find_element_by_xpath(XPATH_X)
print("Trying to click the button to vote.")
next_button.click()
print("Button clicked.")

folder = driver.find_element_by_xpath("//html/body/main/section/div/section/div/div[1]/div/div/div/div[2]/div[210]/div[2]/div[2]/div/div/div/button/")

folder.click()

exit() 

from selenium import webdriver

browser = webdriver.Firefox()
url = 'https://sveriges-storsta.miljonlotteriet.se/competition/sveriges-storsta-kattfantast?nominee=660aa39bef8504bffa7c0ec2'

browser.get(url)

wait = WebDriverWait(browser, 12)

vote_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/div/section/div/div[1]/div/div/div/div[2]/div[194]/div[2]/div[2]/div/div/div/button')))

XPATH_VOTE_BUTTON = '/html/body/main/section/div/section/div/div[1]/div/div/div/div[2]/div[194]/div[2]/div[2]/div/div/div/button'
vote_button = browser.find_element_by_xpath(XPATH_VOTE_BUTTON)
print("Trying to click the button to vote.")
vote_button.click()
print("Button clicked.")

XPATH_FOLDER_BUTTON = '/html/body/main/section/div/section/div/div[1]/div/div/div/div[2]/div[194]/div[2]/div[2]/div/div/div/button'
folder_button = browser.find_element_by_xpath(XPATH_FOLDER_BUTTON)
folder_button.click()
print("Folder button clicked.")


print("An error occurred:", e)

browser.quit()"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Number of times to run the script
num_iterations = 5000

for _ in range(num_iterations):
    # Set up the Firefox driver
    driver = webdriver.Firefox()

    # URL of the website to visit
    url = 'https://sveriges-storsta.miljonlotteriet.se/competition/sveriges-storsta-kattfantast?nominee=660aa39bef8504bffa7c0ec2'

    # Open the website
    driver.get(url)

    try:
        # Wait for the vote button to be visible
        vote_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/section/div/section/div/div[1]/div/div/div/div[2]/div[194]/div[2]/div[2]/div/div/div/button')))
        
        # Click on the vote button
        vote_button.click()
        print("Button clicked.")

    except Exception as e:
        print("An error occurred:", e)

    # Close the browser
    driver.quit()

    # Wait for some time before the next iteration
    time.sleep(3)  # Change the sleep time as needed
