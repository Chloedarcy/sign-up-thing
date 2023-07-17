from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from message import *
from selenium.webdriver.common.keys import Keys
import schedule
from sendEmails import *

# double check all of the dates, make sure search bar goes all places
signUp = True


def loginAndRegister(_class, hour, day):  # put the whole thing in a try loop? also,
    done = False
    while done == False:
        try:
            location = " "
            driver = webdriver.Chrome()
            driver.get("https://www.mindbodyonline.com/explore/")
            time.sleep(7)

            # Open login screen
            time.sleep(2)
            classes_button = driver.find_element(
                By.XPATH, "//button[text()='Login']")
            classes_button.click()
            time.sleep(1)

            # Enter username and password
            username = driver.find_element(By.CLASS_NAME, "Input_input__3rPb3")
            username.send_keys("chloe_darcy@icloud.com")
            password = driver.find_element(
                By.XPATH, "//input[@type='password']")
            password.send_keys("Flower2020")
            time.sleep(1)

            # Submit Login
            loginButton = driver.find_element(
                By.CSS_SELECTOR, "button[type='submit']")
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
            print(location)

            done = True
        except:
            print("trying login again")

        try:
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

            classes_button = driver.find_element(
                By.XPATH, "//button[text()='Classes']")
            classes_button.click()
            print("You've navigated to Drive's classes")
            time.sleep(3)

            date = driver.find_element(
                By.XPATH, "//div[@class='Day_uppercase__A-4T9' and text()='" + day + "']")
            scrollScript = f"window.scrollBy(0, {800});"
            driver.execute_script(scrollScript)
            time.sleep(1)
            date.click()
            time.sleep(5)

            date = driver.find_element(
                By.XPATH, "//div[@class='Day_uppercase__A-4T9' and text()='" + day + "']")

            findClass = driver.find_element(
                By.XPATH, "//a[@class='ClassTimeScheduleItemDetails_classLink__1tyYz' and text()='" + _class + "']")
            findClass.click()
            time.sleep(2)

            print("You've found the correct class")
            dropDown = driver.find_element(
                By.XPATH, "//span[@id='button--listbox-input--1']")
            dropDown.click()
            time.sleep(1)

            if day != "Sat":  # test sat
                dropDown.send_keys(hour)
                dropDown.send_keys(Keys.RETURN)
                time.sleep(2)

            bookNow = driver.find_element(
                By.XPATH, "//div[@class='CourseHeaderForm_gridBookNow__1BgWE']//button")
            driver.execute_script("arguments[0].click();", bookNow)
            time.sleep(8)
            print("You're signed up!")

            sendEmail("DRIVE Class Sign Up", "You have succesfully been signed up for class " +
                      _class + " at " + hour + ' on ' + day + ".")
        except:
            print("there was an error signing up")

# loginAndRegister("PHASE16", "8:45 - 9:40", "Tue")
# login()
# register("POWER", "8:30 - 9:45", "Sat")
# navigate to tuesday

# step 1: switch dates
# step 2: find class
# step 3: sign up for class

# put these in if signUp is true: then execute
# If messaged received to not sign up for whatever time, make it false for that one
# when message is received it will say don't scheduale classes for this date/these dates
# Then the system will make signUp false (5 days before) until 5 days before the end date
# It knows what the date is, so use real date input from the text
# while signUp == True:
# try:


current_date = time.strftime("%Y-%m-%d", time.localtime())
print("Current Date:", current_date)
# date 5 days before skip date

schedule.every().sunday.at("22:45:00").do(
    loginAndRegister, "PHASE16", "6:00 - 6:55", "Tue")

schedule.every().thursday.at("06:00:00").do(
    loginAndRegister, "PHASE16", "6:00 - 6:55", "Tue")

schedule.every().saturday.at("06:30:00").do(
    loginAndRegister, "SHRED", "6:30 - 7:25", "Thu")

schedule.every().sunday.at("06:15:00").do(
    loginAndRegister, "LIFT", "6:15 - 7:10", "Fri")

schedule.every().monday.at("08:30:00").do(
    loginAndRegister, "POWER", "8:30 - 9:45", "Sat")

readEmail()
print(dontSignUpTime)
print(current_date)

while True:
    if dontSignUpTime == None:
        schedule.run_pending()
        readEmail()
        time.sleep(1)
        print(dontSignUpTime)
        print(current_date)
    else:
        print("you are in don't sign up for classes mode")
        print(dontSignUpTime)
        print(current_date)
        while dontSignUpTime == current_date:
            print('NO')
            readEmail()
        # dontSignUpTime = None


# receive email
# take the date 5 days before as doNotRunDate
# If day == doNotRunDate, don't call any functions
# else call as normal
# updatable based on email input

# driver.quit()  # for now
