import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.car.gr/classifieds/cars/?fs=1&condition=%CE%9A%CE%B1%CE%B9%CE%BD%CE%BF%CF%8D%CF%81%CE%B9%CE%BF&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&offer_type=sale")

c = r.content


soup = BeautifulSoup(c,"html.parser")


all = soup.find_all("div",{"class":"clsfd_list_row"})




all[0].find("span",{"itemprop":"brand"}).text


for i in all:
    print (i.find("span",{"itemprop":"brand"}).text)