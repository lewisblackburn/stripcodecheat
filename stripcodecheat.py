from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
from lxml import html
import json

USERNAME = ""
PASSWORD = ""

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://stripcode.dev/ranked")

username = driver.find_element_by_id("login_field")
password = driver.find_element_by_id("password")
submit = driver.find_element_by_name("commit")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
submit.send_keys(Keys.RETURN)

time.sleep(2)

while (True):
  time.sleep(5)
  count = 2 
  for x in range(0, 5):
    time.sleep(3)
    repo = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[' + str(count) + ']/button/span[1]').text
    button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[' + str(count) + ']/button')
    filename = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/h1').text
    url = "https://api.github.com/search/code?q=" + "repo:" + repo + " filename:" + filename
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    try:
        if (parsed['total_count'] < 1):
          # not found #
          count = count + 1
        else:
          time.sleep(0.5)
          button.click()
          time.sleep(0.5) 
          nextbutton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/button')
          nextbutton.click()
          break

        if (x == 4):
          time.sleep(0.5)
          button.click()
          time.sleep(0.5)
          nextbutton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/button')
          nextbutton.click()
    except:
      print("rate limit")
      pass
