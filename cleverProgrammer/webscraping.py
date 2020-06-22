import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://forecast.weather.gov/MapClick.php?CityName=Los+Angeles&state=CA&site=LOX&lat=34.1006&lon=-118.327#.Xu_MJs8zZN4")
soup = BeautifulSoup(page.content, "html.parser")

week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_='tombstone-container')

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_="temp").get_text() for item in items]

print(period_names)
print(short_desc)
print(temperatures)

weatherStuff = pd.DataFrame({
    'period': period_names,
    'shortDescription': short_desc,
    'temperatures': temperatures
})

print(weatherStuff)

weatherStuff.to_csv('weather.csv')
