from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.google.com/")
try :
    search_box = driver.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
except Exception :
    search_box = driver.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys('apple')
search_box.send_keys(Keys.ENTER)
try :
    driver.find_element('xpath','/html/body/div[7]/div/div[5]/div/div/div[1]/div[1]/div/a[2]').click()
except Exception :
    driver.find_element('xpath','/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[3]/a').click()

driver.find_element('xpath','/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[4]/a[1]/div[1]/img').click()
driver.save_screenshot('apple_1.jpg')
driver.find_element('xpath','/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[2]/div/div[2]/div[3]/a').click()
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(5)
driver.find_element('xpath','/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[42]/a[1]/div[1]/img').click()
driver.save_screenshot('apple_2.jpg')
driver.find_element('xpath','/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[2]/div/div[2]/div[3]/a').click()
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
driver.find_element('xpath','/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[51]/div[46]/a[1]/div[1]/img').click()
driver.save_screenshot('apple_3.jpg')