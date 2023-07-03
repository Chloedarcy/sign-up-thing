from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from message import *
from selenium.webdriver.common.keys import Keys
import schedule

signUp = True

driver = webdriver.Chrome()
driver.get("https://www.mindbodyonline.com/explore/")


def login():
    # Open login screen
    time.sleep(2)
    classes_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    classes_button.click()
    time.sleep(1)

    # Enter username and password
    username = driver.find_element(By.CLASS_NAME, "Input_input__3rPb3")
    username.send_keys("chloe_darcy@icloud.com")
    password = driver.find_element(By.XPATH, "//input[@type='password']")
    password.send_keys("Flower2020")
    time.sleep(1)

    # Submit Login
    loginButton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    loginButton.click()
    print("You are logged in")
    time.sleep(1)

    # Exit login screen
    xOut = driver.find_element(
        By.CSS_SELECTOR, "i[data-testid='fontIcon']")
    xOut.click()
    time.sleep(1)

    # Type Drive gym
    activeElement = driver.switch_to.active_element
    activeElement.send_keys("drive custom fit")

    # Enter Location
    location = driver.find_element(
        By.CSS_SELECTOR, "input[value='Seattle, WA, US']")
    for i in range(15):
        location.send_keys(Keys.BACK_SPACE)
    time.sleep(2)
    location.send_keys("Windham, NH, US")
    time.sleep(2)
    location.send_keys(Keys.ENTER)
    time.sleep(3)

    # Search
    search = driver.find_element(
        By.CSS_SELECTOR, "div.column.is-narrow i.FontIcon_icon__1e0G9.FontIcon_sm__1mEsg")
    search.click()
    print("Drive's near Windham, NH succesfully searched")
    time.sleep(3)

    drivePage = driver.find_element(
        By.CSS_SELECTOR, "h3.is-header-5.StudioDetails_title__1JpTe")
    drivePage.click()
    time.sleep(3)


def register(_class, hour, day):
    classes_button = driver.find_element(
        By.XPATH, "//button[text()='Classes']")
    classes_button.click()
    print("You've navigated to Drive's classes")
    time.sleep(3)

    # if day == "sat": do some of them need to go to the next week?
    date = driver.find_element(
        By.XPATH, "//div[@class='Day_uppercase__A-4T9' and text()='Thu']")
    scrollScript = f"window.scrollBy(0, {800});"
    driver.execute_script(scrollScript)
    time.sleep(1)
    date.click()
    time.sleep(5)

    findClass = driver.find_element(
        By.CSS_SELECTOR, "h5.is-marginless.ClassTimeScheduleItemDetails_truncate__3zJqg a.ClassTimeScheduleItemDetails_classLink__1tyYz")
    findClass.click()
    time.sleep(2)

    dropDown = driver.find_element(
        By.XPATH, "//span[@id='button--listbox-input--116']//span[contains(@class, 'pr-2')]//i[contains(@class, 'FontIcon_icon__1e0G9')][contains(@class, 'FontIcon_sm__1mEsg')][contains(@class, 'FontIcon_secondary__CZEhx')][contains(@class, 'ss-icon')][contains(@class, 'ss-navigatedown')]")
    dropDown.click()
    time.sleep(10)

    # try for element for 6:15
    # except, send a text that it erred out
    # if it works, book then approve


login()
register("PHASE16", "6:00", "thursday")
# navigate to tuesday

# step 1: switch dates
# step 2: find class
# step 3: sign up for class

# put these in if signUp is true: then execute
# If messaged received to not sign up for whatever time, make it false for that one
# when message is received it will say don't scheduale classes for this date/these dates
# Then the system will make signUp false (5 days before) until 5 days before the end date
# It knows what the date is, so use real date input from the text
if signUp == True:
    schedule.every().thursday.at("06:00:00").do(
        register, "PHASE16", "6:00", "thursday")

    schedule.every().saturday.at("06:30:00").do(login)
    schedule.every().saturday.at("06:30:00").do(
        register, "SHRED", "6:30", "saturday")

    schedule.every().sunday.at("06:15:00").do(login)
    schedule.every().sunday.at("06:15:00").do(register, "LIFT", "6:15", "sunday")

    schedule.every().monday.at("08:30:00").do(login)
    schedule.every().monday.at("08:30:00").do(register, "POWER", "8:30", "monday")

# while True:
# schedule.run_pending()
# time.sleep(1)

driver.quit()  # for now
