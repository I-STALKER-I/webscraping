from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com/')

box = driver.find_element("name",'q')

box.send_keys('apple')
from selenium.webdriver.common.keys import Keys
box.send_keys(Keys.ENTER)
try :
    box_2 = driver.find_element('xpath',"/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[3]/a").click()
except Exception :
    box_2 = driver.find_element('xpath',"/html/body/div[7]/div/div[5]/div/div/div[1]/div[1]/div/a[2]").click()


driver.find_element('xpath',"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img").click()
#driver.find_element('xpath','/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[3]/div[1]/a/img').click()
#driver.save_screenshot("apple_1.jpg")
previous_height = driver.execute_script('return document.body.scrollHeight') 
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # check if it reached the end
    last_line = driver.find_element('xpath','/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[1]')
    if last_line.get_attribute('data-status') != '3':
        continue
    else:
        break