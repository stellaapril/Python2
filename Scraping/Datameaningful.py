import requests
from bs4 import BeautifulSoup
url='https://www.yogaflowpittsburgh.com/studio/shadyside-studio'
response=requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
l=soup.findAll(class_='portfolio center')
num=0
for item in l:
    num=num+1
    print(item.text)
print('There are ',num,' instructors from yoga flow')