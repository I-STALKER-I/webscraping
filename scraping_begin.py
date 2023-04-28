import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://maktabkhooneh.org/learn/%D8%B2%D8%A8%D8%A7%D9%86%D9%87%D8%A7%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-mk76/?p=1&'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')


courses = soup.find_all('div', class_ = 'side-margin bottom-margin js-filter-item active-item')
print(courses[0].find('div',{'class' : "course-card__teacher"}))


print(courses[4]['title'])
"""
selenium
beatiful soup
extension using
adding to path 
find element xpath khode element
find elements == gesmat moshtarak
action == click
driver.screenshot
apple search konid chandta screenshot begirid ba codo file bezaridesh to ye repo
private ba man sharesh konid
tedad saat doreeee

"""


"""
maktabkhonne :
price saat class 
va comment ha
twitter :
run the code
list of folowers
scroooooolllll
code
dataframe
csv
"""



"""concurrent programiing :
multi thread
multi process
"""