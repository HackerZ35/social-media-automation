from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver
CHROME_DRIVER_PATH = "./chromedriver"

def post_to_twitter(username, password, content):
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get("https://twitter.com/login")

    # Log in to Twitter
    time.sleep(2)
    username_input = driver.find_element(By.NAME, "session[username_or_email]")
    password_input = driver.find_element(By.NAME, "session[password]")
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    # Post to Twitter
    time.sleep(2)
    tweet_input = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tweet text']")
    tweet_input.send_keys(content)
    tweet_input.send_keys(Keys.CONTROL, Keys.RETURN)

    time.sleep(5)
    driver.quit()

def post_to_facebook(username, password, content):
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get("https://www.facebook.com/login")

    # Log in to Facebook
    time.sleep(2)
    username_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    # Post to Facebook
    time.sleep(2)
    status_input = driver.find_element(By.CSS_SELECTOR, "textarea[aria-label='Write a post']")
    status_input.send_keys(content)
    status_input.send_keys(Keys.CONTROL, Keys.RETURN)

    time.sleep(5)
    driver.quit()
