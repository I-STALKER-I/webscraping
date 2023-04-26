import pandas as pd
import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# phase1: gathering elements by class_name
driver = webdriver.Chrome('chromedriver.exe')
main_page = driver.get('https://maktabkhooneh.org/learn/programming-languages/')
courses = driver.find_elements(By.CLASS_NAME,'active-item')


print(f"gathered elements: {len(courses)}")
print("gathering information please wait...")

#phase2 gathering wanted information
row =  []

for course in courses :
    column = []
    ActionChains(driver).move_to_element(driver.find_element('xpath','/html/body/nav/div/div[2]/a/img')).perform()
    ActionChains(driver).move_to_element(course).perform()
    #why do i hover two times?
    """because when you hover over the first element and things get poped up ,the pop up wont let you 
    to select the second element so you have to hover over another thing then hover over the element"""

    try :
        column.append(course.find_element(By.CLASS_NAME,'course-card__title').text)
    except Exception :
        column.append('نا معلوم')

    try :
        column.append(course.find_element(By.CLASS_NAME,'course-card__teacher').text)
    except Exception :

        column.append('نا معلوم')

    time.sleep(1.5)

    try :
        column.append(course.find_element(By.CLASS_NAME,'course-card-extra__header').text.split()[0])
    except Exception :

        column.append('نا معلوم')

    row.append(column)

print("Done gathering")
print("making the data frame...")

headers = ['درس','استاد','ساعت تدریس']
df = pd.DataFrame(row,columns=headers)

df.to_excel('maktabkhoone.xlsx')
df.to_csv('maktabkhone.csv')


print("phase2 completed")

print("gathering comments please wait")
#phase3: getting the comments
import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://maktabkhooneh.org/learn/programming-languages/')
soup = BeautifulSoup(page.text,'lxml')
courses = soup.find_all('div', class_ = 'side-margin bottom-margin js-filter-item active-item')

column = []
row = []
for course in courses :
    lst = []
    course_url = "https://maktabkhooneh.org" + course.find('a',class_ = 'course-card__wrapper')['href']
    try :
        title = course.find('div',class_ = 'course-card__title')
    except AttributeError :
        title = "نا معلوم"
        
    column.append(title)
    course_page = requests.get(course_url)
    course_page_soup = BeautifulSoup(course_page.text,'lxml')

    all_comments = course_page_soup.find_all('div',class_ = 'comments__desc-user top-margin')
    for comment in all_comments :
        if len(all_comments) > 0 :
            lst.append(comment.text)
        else :
            lst.append("No comment")
    
    row.append(lst)


for i,titles in enumerate(column) :

    print(titles)
    for comment in row[i] :
        print('comment: ',comment)
#done