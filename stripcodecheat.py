from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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

time.sleep(5)

while (True):
  time.sleep(2)
  count = 2 
  for x in range(0, 5):
    repo = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[' + str(count) + ']/button/span[1]').text
    button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[' + str(count) + ']/button')
    filename = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/h1').text
    url = "https://github.com/search?q=" + "repo:" + repo + " filename:" + filename


    driver.execute_script("window.open('" + url + "');")
    driver.switch_to.window(driver.window_handles[1])

    found = driver.find_element_by_xpath('/html/body/div[4]/main/div/div[3]/div/div[1]/h3').text
    if (found.startswith("W")):
       # not found 
      time.sleep(1)
      driver.close()
      driver.switch_to.window(driver.window_handles[0])
      count = count + 1
    else:
      time.sleep(1)
      driver.close()
      driver.switch_to.window(driver.window_handles[0])
      button.click()
      time.sleep(0.5)
      nextbutton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/button')
      nextbutton.click()
      break

    if (x == 4):
      time.sleep(1)
      button.click()
      time.sleep(0.5)
      nextbutton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/button')
      nextbutton.click()



# 6 code results or view all results on GitHub
# We couldn’t find any code matching 'repo:keon/algorithms filename:build.py'