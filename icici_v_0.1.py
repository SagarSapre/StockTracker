from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from requests import get
import json
import datetime

#this file creates a json object with keys and values of scheme name and download url

driver = webdriver.Chrome()
r=driver.get("https://www.icicipruamc.com/downloads/others/monthly-portfolio-disclosures")
time.sleep(3)
driver.implicitly_wait(20)
b=driver.find_element(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/button').click()
print(b)
time.sleep(1)
yearlist=[]
a=driver.find_elements(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/ul/li/a/span[1]')

for item in a:
    b=item.text
    yearlist.append(b)
noofyears=len(yearlist)+1
print (yearlist)

#driver.find_element(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/button').click()

#z= '{"year"=year,"month"=month,"xlnames"=xlname,"xlurl"=xlurl}'
Keyslist=[]
valuelist=[]

for x in range(2,noofyears-11):#noofyears
    driver.find_element(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/button').click()# _______ clicks on dropdown Month to make options visible _______
    time.sleep(1) 
    monthlist=[]
    c=driver.find_elements(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/ul/li/a/span[1]')
    for item in c:
        d=item.text
        monthlist.append(d)
    noofmonths=len(monthlist)+1
    driver.find_element(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/button').click()# _______ clicks on dropdown YEAR to make options visible _______
    time.sleep(1)

    time.sleep(1)
    driver.find_element(By.XPATH,f'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/ul/li[{x}]/a/span[1]').click()#_______click on 2023 to load 2023 links_______
    time.sleep(1)
    for y in range(2,noofmonths):

        ##for 2022 xpath is as follows
        #//*[@id="PSYear"]/div[2]/div[3]
        ##_______click on dropdown Month to make it visible_______
        dropd = driver.find_element(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/button').click()
        time.sleep(1)

        time.sleep(1)
        ##_______click on Month to load that months links_______
        dropd = driver.find_element(By.XPATH,f'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/ul/li[{y}]/a/span[1]').click()
        time.sleep(1)
        #selected year = //*[@id="PSYear"]/div[1]
        #selected Month =//*[@id="PSMonth"]/div[1]
        year=driver.find_element(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/button/span[1]').text
        month=driver.find_element(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/button/span[1]').text
        print()
        print(year,"-",month)
        print()
        ##new attaempt to add all links to dictionary
        try:
            dropd = driver.find_element(By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p[1]/a[1]')
            xlurl=dropd.get_attribute("href")
            xlname=dropd.get_attribute("text")
            myTuple = (str(year),'-',month,'-',xlname)
            keys=''.join(myTuple)
            Keyslist.append(keys)
            valuelist.append(xlurl)
        except:
            pass


driver.close()
'''
#time.sleep(3)
#selectdnld=driver.find_elements(By.XPATH,"//a[contains(text(),'All Schemes Monthly Portfolio')]")
for items in selectdnld:
    urllist.append(items.get_attribute("href"))
    monthtext.append(items.get_attribute("text").split("- ")[1])
'''
z=dict(zip(Keyslist,valuelist))
with open("icici.json", "w") as outfile:
    json.dump(z,outfile)
print ("printing urldict")
print()

print(yearlist)
print(monthlist)