import requests
from bs4 import BeautifulSoup
import re
import json

url="https://www.moneycontrol.com/mutual-funds/find-fund/"

r=requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

data1=soup.find_all('ul',class_ = "common_checkbox_list")[0].text
data1=data1.replace('\n','').replace('\t','')

re_outer = re.compile(r'([^A-Z ])([A-Z])')
re_inner = re.compile(r'(?<!^)([A-Z])([^A-Z])')
re_data=re_outer.sub(r'\1\2', re_inner.sub(r'\1\2',data1))


fundlist=re_data.split('Fund')
fundlist=fundlist[:-1]
amc_no =len(fundlist)



with open('data.json', 'w') as f:
    json.dump(fundlist, f)

print()
print(F"AMC NO IS ___{amc_no}___")
print()
if amc_no == 42:
    print('AMC NO has  NOT CHANGED')
else:print('AMC NO has  CHANGED')
print()

