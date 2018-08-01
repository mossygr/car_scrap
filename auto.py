import requests
from bs4 import BeautifulSoup
import pandas 

r = requests.get("https://www.car.gr/classifieds/cars/?fs=1&condition=%CE%9A%CE%B1%CE%B9%CE%BD%CE%BF%CF%8D%CF%81%CE%B9%CE%BF&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&offer_type=sale")

c = r.content


soup = BeautifulSoup(c,"html.parser")

all = soup.find_all("div",{"class":"clsfd_list_row"})
#fuel = soup.find_all("span",{"class":"fueltype colorize"})[1].text
#print (data)
#print (all[1].find_all("span",{"class":"fueltype colorize"})[1].text)
len(all)
len(all[1].find_all('span',{"class":"fueltype colorize"}))


l = []
#print ( all.find_all("i",{"class":"icon-fuel"})[1].text )

for i in all:
    d = {}
    d["Fuel"] = i.find_all('span',{"class":"fueltype colorize"})[0].text.replace('\n', '')
    d["price"] = i.find_all("span",{"itemprop":"price"})[0].text.replace(u'\xa0', ' ')
    d["brand"] = i.find_all("span",{"itemprop":"brand"})[1].text
    print (" ")
    l.append(d)


df = pandas.DataFrame(l)

df.to_csv('~/Downloads/data.csv')


