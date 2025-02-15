import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Step 1: Start Chrome in undetected mode
driver = uc.Chrome()

# Step 2: Open Aviso.bz login page
driver.get("https://aviso.bz/")

# Step 3: Log in (Replace with your credentials)
username = driver.find_element(By.NAME, "email")  # Adjust if needed
password = driver.find_element(By.NAME, "password")  # Adjust if needed

username.send_keys("alimansoor")  # Enter your email
password.send_keys("SRjj!Zrzg8VRU8m")  # Enter your password
password.send_keys(Keys.RETURN)  # Press Enter to log in

time.sleep(5)  # Wait for login to complete

# Step 4: Go to YouTube work section
driver.get("https://aviso.bz/work-youtube")
time.sleep(3)

# Step 5: Loop through available tasks
while True:
    tasks = driver.find_elements(By.CLASS_NAME, "task-button-class")  # Adjust class name

    if not tasks:
        print("No tasks available. Waiting...")
        time.sleep(60)  # Wait before checking again
        driver.refresh()
        continue

    for task in tasks:
        try:
            task.click()  # Click task
            time.sleep(5)

            # Switch to new YouTube tab
            driver.switch_to.window(driver.window_handles[1])

            print("Watching video...")
            time.sleep(30)  # Adjust time based on video duration

            # Close YouTube tab and return
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            print("Task completed! Moving to next task...")
        except Exception as e:
            print("Error:", e)
            driver.refresh()

    print("All tasks done. Checking for new tasks...")
    time.sleep(60)
    driver.refresh()

driver.quit()  # Close browser when done