import requests
from requests import get
import json
from bs4 import BeautifulSoup

r=requests.get("https://mf.nipponindiaim.com/investor-service/downloads/factsheet-and-other-portfolio-disclosures")
baseurl="https://mf.nipponindiaim.com"
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
scrape = soup.find_all('div', class_="contentWrap")

names=[]
url=[]
for item in scrape:
    a=item.find_all('a')
for item in a:
    link=baseurl+item['href']
    url.append(link)
    name=link.split('/')[-1]
    names.append(name)

z=dict(zip(names,url))
with open("nippon.json", "w") as outfile:
    json.dump(z,outfile)    


