import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:

    def __init__(self):
        self.TWITTER_URL = None
        self.driver = None
        self.tweet_button = None
        self.tweet_box = None
        self.password_field = None
        self.username_field = None

    def login(self, loginid, loginpaswrd):
        """this is to log in to your Twitter account. It needs your loginID and loginPswd"""
        
        exe_path = "/Users/macintosh/Development/chromedriver"
        ser = Service(executable_path=exe_path)
        self.driver = selenium.webdriver.Chrome(service=ser)
        self.TWITTER_URL = "https://twitter.com/i/flow/login"
        self.driver.get(self.TWITTER_URL)
        time.sleep(10)
        self.username_field = self.driver.find_element(By.NAME, "text")
        self.username_field.send_keys(loginid)
        time.sleep(2)
        self.username_field.send_keys(Keys.ENTER)
        time.sleep(20)
        self.password_field = self.driver.find_element(By.NAME, "password")
        self.password_field.send_keys(loginpaswrd)
        time.sleep(2)
        self.password_field.send_keys(Keys.ENTER)
        time.sleep(2)

    def tweet(self, downspeed, upspeed, iphandle, resultid):
        """This will create and post the tweet. It requires your current download & upload speed as well as
         your internet provider twitter handle and result ID of speedtest"""

        self.tweet_box = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        self.tweet_box.send_keys(f"{iphandle} i am paying for 100MBPS down speed and i am only getting "
                                 f"DownSpeed {downspeed}/UpSpeed {upspeed}. Please solve this issue.\n"
                                 f"Result ID: {resultid}")
        time.sleep(3)
        self.tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                               '2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div['
                                                               '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div['
                                                               '3]/div/span/span')
        self.tweet_button.click()
        time.sleep(10)
