from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from message import *
from selenium.webdriver.common.keys import Keys
import schedule
from sendEmails import *
from selenium import webdriver
from selenium.webdriver.common.by import By

# double check all of the dates, make sure search bar goes all places
signUp = True


def loginAndRegister(_class, hour, day):  # put the whole thing in a try loop? also,
    done = False
    while done == False:
        try:
            location = " "

            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome("path/to/chromedriver.exe",
                                      options=options)
            driver.get("https://www.mindbodyonline.com/explore/")

            # driver = webdriver.Chrome()
            # driver.get("https://www.mindbodyonline.com/explore/")
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
            print("trying login again")  # this doesnt actually run it again
            time.sleep(2)

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
            time.sleep(2)


current_date = time.strftime("%Y-%m-%d", time.localtime())

schedule.every().thursday.at("06:00:00").do(
    loginAndRegister, "PHASE16", "6:00 - 6:55", "Tue")

schedule.every().saturday.at("06:30:00").do(
    loginAndRegister, "SHRED", "6:30 - 7:25", "Thu")

schedule.every().sunday.at("06:15:00").do(
    loginAndRegister, "LIFT", "6:15 - 7:10", "Fri")

schedule.every().monday.at("08:30:00").do(
    loginAndRegister, "POWER", "8:30 - 9:45", "Sat")

while True:  # make sure if emial is sent no overlap
    if dontSignUpTime == []:
        schedule.run_pending()
        dontSignUpTime = readEmail()
        time.sleep(1)
    else:
        print("you are in dont sign up time mode")
        time.sleep(1)

        for day in range(len(dontSignUpTime)):
            print(dontSignUpTime[day])
            # this works, make sure dontsignuptime is correct
            while dontSignUpTime[day] == current_date:
                readEmail()
                time.sleep(1)
        dontSignUpTime = []


# driver.quit()
