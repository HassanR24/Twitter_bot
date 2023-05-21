import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from twitter_bot import TwitterBot

TWITTER_ID = ""  # insert your Twitter ID
TWITTER_PSWD = ""  # insert your Twitter Password
SPEED_TEST_URL = "https://www.speedtest.net/"
PROMISED_SPEED = 80
IP_HANDLE = "@"  # insert your internet provider @ of twitter.

exe_path = "/Users/macintosh/Development/chromedriver"   # replace it with your own path to chrome driver
SER = Service(executable_path=exe_path)
driver = selenium.webdriver.Chrome(service=SER)


driver.get(SPEED_TEST_URL)
time.sleep(8)
close_button = driver.find_element(By.CLASS_NAME, "banner-close-button")
close_button.click()
go_button = driver.find_element(By.CLASS_NAME, "start-text")
go_button.click()
time.sleep(60)
result_id = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                          '3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a').text
print(result_id)
down_speed = float(driver.find_element(By.CLASS_NAME, "download-speed").text)
print(down_speed)
up_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text
print(up_speed)


if down_speed < PROMISED_SPEED:
    tweet_bot = TwitterBot()
    tweet_bot.login(TWITTER_ID, TWITTER_PSWD)
    time.sleep(5)
    tweet_bot.tweet(downspeed=down_speed, upspeed=up_speed, iphandle=IP_HANDLE, resultid=result_id)
