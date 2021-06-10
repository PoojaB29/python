import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://mausam.imd.gov.in/')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id ='today')
#print(week)

test = week.find_all(class_ = 'capital')
#print(len(test))

#print(test[0].find('h3').get_text())
#print(test[0].find(class_ = 'val').get_text())
#print(test[0].find(class_ = 'wind').get_text())
#print(test[0].find(class_ = 'max').get_text())

names = [i.find('h3').get_text() for i in test]
temperature = [i.find(class_ ='val').get_text() for i in test]
wind_speed = [i.find(class_ = 'wind').get_text() for i in test]
max_percent = [i.find(class_ = 'max').get_text() for i in test]

print(names)
print(temperature)
print(wind_speed)
print(max_percent)

weather_stuff = pd.DataFrame(
    {
       'Names' : names,
       'Temperature' : temperature,
       'Wind_Speed' : wind_speed,
       'Maximum_Percentage' : max_percent,
    }
)

print(weather_stuff)

weather_stuff.to_csv('Weather.csv')