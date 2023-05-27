import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
#object of Options class
op = Options()
#set .crx file path of extension

op.add_extension('H:\AP projects\scraping\scraping_twitter\Chrome-SetupVPN-3.12.16.crx')
#set geckodriver.exe path
driver = webdriver.Chrome('chromedriver.exe',options=op)
driver.maximize_window()
#launch browser

while True :
    if pyautogui.pixel(829,247)[1] == 174 :
        break
     
pyautogui.click(585,19)
time.sleep(2)
pyautogui.click(1772,64)
time.sleep(0.3)
pyautogui.click(1656,240)
while not pyautogui.pixel(1740,219)[0] == 193 :
    pass

pyautogui.click(1611,194)
while not pyautogui.pixel(1411,304)[0] == 0 :
    pass
pyautogui.click(1528,297)
time.sleep(1)
pyautogui.write("stalkerkhadang@gmail.com")
pyautogui.click(1563,350)
pyautogui.write("S44249032s")
pyautogui.click(1551,473)
while not pyautogui.pixel(1407,414)[1] == 28 :
    pass
pyautogui.moveTo(1550,443)
pyautogui.click(1550,443)
time.sleep(1)
while  pyautogui.pixel(1449,201)[0] == 255 :
    pass
driver.get("https://www.twitter.com")
while True :
    try :
        driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]').click()
        break
    except Exception :
        pass
time.sleep(1)
driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a').click()
time.sleep(0.6)

while True :
    try :
        driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div/h1/span/span')
        break
    except Exception :
        pass
driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]').click()
signin_box = driver.find_element('xpath','//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

gmail = 'stalkerkhadang@gmail.com'

for i in range(7) :
    signin_box.send_keys(gmail[i])

for i in range(7,14) :
    time.sleep(0.1)
    signin_box.send_keys(gmail[i]) 

time.sleep(0.5)
signin_box.send_keys(gmail[14])
for i in range(15,20) :
    signin_box.send_keys(gmail[i])

time.sleep(0.7)
signin_box.send_keys(gmail[20])
for i in range(21,24) : #24 for khadang 23 for sina
    signin_box.send_keys(gmail[i])

signin_box.send_keys(Keys.ENTER)



try :
    while True :
        try :
            driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/h1/span/span')
            break
        except Exception :
            try :
                driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                break
            except Exception :
                pass
    try :
        password_box = driver.find_element('xpath','//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password = "S44249032s"
        password_box.click()
        password_box.send_keys(password[0])
        for word in password_box[1:9] :
            password_box.send_keys(word)
    except Exception :
        pass


    time.sleep(1)
    password_box.send_keys(password[9]) 
    password_box.send_keys(Keys.ENTER)
except Exception :
    username_box = driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    username = 'stalkerkha90093'
    for word in username[0:4] :
        username_box.send_keys(word)
    time.sleep(0.1)
    username_box.send_keys(username[4])
    for word in username[5:] :
        username_box.send_keys(word)
    time.sleep(0.1)
    username_box.send_keys(Keys.ENTER)
    while True :
        try :
            password_box = driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            break
        except Exception :
            pass

    password = "S44249032s"
    password_box.send_keys(password[0])
    for word in password[1:9] :
        time.sleep(0.05)
        password_box.send_keys(word)
    time.sleep(1)
    password_box.send_keys(password[9])
    time.sleep(1)
    driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
while True :
    try :
        driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input').click()
        break
    except Exception :
        pass

search_box = driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search_box.click()
lockheed = 'lockheed martin'
for word in lockheed[0:8] :
    time.sleep(0.08)
    search_box.send_keys(word)

search_box.send_keys(lockheed[8])
time.sleep(0.2)

for word in lockheed[9:] :
    time.sleep(0.1)
    search_box.send_keys(word)

search_box.send_keys(Keys.ENTER)
time.sleep(0.45)
while True :
    try :
        driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]/div/div/div').click()
        break
    except Exception :
        pass
time.sleep(0.5)
while True :
    try :
        driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a').click()
        break
    except Exception :
        pass


count = 0
usernames = []
while True :
    try :
        driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]')
        break
    except Exception :
        pass

while True:


    for i in range(1,100) :
        #/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]
        #/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]
        #/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]
        try :
            username = driver.find_element('xpath',f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]').text
            user_link = driver.find_element('xpath',f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/a/div/div/span').text
            whole_user = [username,user_link]
            usernames.append(whole_user)
        except Exception :
            pass
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    current_height = driver.execute_script('return document.body.scrollHeight') 
    if count == 20:
        break
    count += 1

print(usernames)
heads = ["username","user id"]
df = pd.DataFrame(usernames,columns=heads)
df.to_excel('twitter_scraping.xlsx')
df.to_csv('twitter_scraping.csv')