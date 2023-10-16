from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from requests import get
import json
import datetime

#this file creates a json object with keys and values of scheme name and download url

driver = webdriver.Chrome()
r=driver.get("https://www.sbimf.com/portfolios")
time.sleep(3)
driver.implicitly_wait(20)

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(current_time)

driver.find_element(By.XPATH,'//*[@id="PSYear"]').click()
time.sleep(1)
yearlist=[]
a=driver.find_elements(By.XPATH,'//*[@id="PSYear"]/div[2]/div')
for item in a:
    b=item.text
    yearlist.append(b)
noofyears=len(yearlist)+1
driver.find_element(By.XPATH,'//*[@id="PSYear"]').click()

#z= '{"year"=year,"month"=month,"xlnames"=xlname,"xlurl"=xlurl}'
Keyslist=[]
valuelist=[]

for x in range(2,noofyears):
    driver.find_element(By.XPATH,'//*[@id="PSMonth"]').click()
    time.sleep(1) 
    monthlist=[]
    c=driver.find_elements(By.XPATH,'//*[@id="PSMonth"]/div[2]/div')
    for item in c:
        d=item.text
        monthlist.append(d)
    noofmonths=len(monthlist)+1
    driver.find_element(By.XPATH,'//*[@id="PSYear"]').click()# _______ clicks on dropdown YEAR to make options visible _______
    time.sleep(1)

    time.sleep(1)
    driver.find_element(By.XPATH,f'//*[@id="PSYear"]/div[2]/div[{x}]').click()#_______click on 2023 to load 2023 links_______
    time.sleep(3)
    for y in range(2,noofmonths):

        ##for 2022 xpath is as follows
        #//*[@id="PSYear"]/div[2]/div[3]
        ##_______click on dropdown Month to make it visible_______
        dropd = driver.find_element(By.XPATH,'//*[@id="PSMonth"]').click()
        time.sleep(1)

        time.sleep(3)
        ##_______click on Month to load that months links_______
        dropd = driver.find_element(By.XPATH,f'//*[@id="PSMonth"]/div[2]/div[{y}]').click()
        time.sleep(3)
        #selected year = //*[@id="PSYear"]/div[1]
        #selected Month =//*[@id="PSMonth"]/div[1]
        year=driver.find_element(By.XPATH,'//*[@id="PSYear"]/div[1]').text
        month=driver.find_element(By.XPATH,'//*[@id="PSMonth"]/div[1]').text
        print()
        print(year,"-",month)
        print()
        ##new attaempt to add all links to dictionary
        dropd = driver.find_elements(By.XPATH,'//*[@id="tblPortfoliosheets"]/tr/td[1]/a')
        for items in dropd:
            xlurl=items.get_attribute("href")
            xlname=items.get_attribute("text")
            myTuple = (str(year),'-',month,'-',xlname)
            keys=''.join(myTuple)
            Keyslist.append(keys)
            valuelist.append(xlurl)

            

driver.close()
'''
#time.sleep(3)
#selectdnld=driver.find_elements(By.XPATH,"//a[contains(text(),'All Schemes Monthly Portfolio')]")
for items in selectdnld:
    urllist.append(items.get_attribute("href"))
    monthtext.append(items.get_attribute("text").split("- ")[1])
'''
z=dict(zip(Keyslist,valuelist))
with open("sbi2.json", "w") as outfile:
    json.dump(z,outfile)
print ("printing urldict")
print()
#print(urldict)
#print(selectdnld)
'''
print()
print("printing urllist" +'/n')
print(urllist)
print()
print("printing len of urllist" +'/n')
print(len(urllist))
print("printing monthtext" +'/n')
print(monthtext)
'''
#selectdnld=driver.find_element(By.XPATH,'//*[@id="tblPortfoliosheets"]/tr[1]/td[1]/a').click()
#time.sleep(3)

'''
def download_file(url, file_path):

    reply = get(url, stream=True)
    with open(file_path, 'wb') as file:
        for chunk in reply.iter_content(chunk_size=1024): 
            if chunk:
                file.write(chunk)
'''
