from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from requests import get
import json
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#this file creates a json object with keys and values of scheme name and download url

driver = webdriver.Chrome()
r=driver.get("https://www.hdfcfund.com/statutory-disclosure/portfolio/monthly-portfolio")
time.sleep(3)
driver.implicitly_wait(20)
yearstr = '//*[@id="react-tabs-1"]/div[1]/div/div/div[1]/div/div/input'
b=driver.find_element(By.XPATH,yearstr).click()


time.sleep(1)
yearlist=[]
a=driver.find_elements(By.XPATH,'/html/body/div/div/div[2]/div/section[2]/div/div[2]/div[1]/div/div/div[1]/div/div/ul/div/div[1]/li')

for item in a:
    b=item.text
    yearlist.append(b)
noofyears=len(yearlist)+1

while("" in yearlist):
    yearlist.remove("")
print (yearlist) 
yearoptionsstr='/html/body/div/div/div[2]/div/section[2]/div/div[2]/div[1]/div/div/div[1]/div/div/ul/div/div[1]/li[1]'

#driver.find_element(By.XPATH,'//*[@id="divRemunaration"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/button').click()

#z= '{"year"=year,"month"=month,"xlnames"=xlname,"xlurl"=xlurl}'
Keyslist=[]
valuelist=[]
monthstr='//*[@id="react-tabs-1"]/div[1]/div/div/div[2]/div/div/input'
for x in range(1,noofyears-16):#noofyears 
    driver.find_element(By.XPATH,monthstr).click()
    # _______ clicks on dropdown Month to make options visible _______
    time.sleep(1) 
    monthlist=[] 
    c=driver.find_elements(By.XPATH,'/html/body/div/div/div[2]/div/section[2]/div/div[2]/div[1]/div/div/div[2]/div/div/ul/div/div[1]/li')
    month_options_str ='/html/body/div/div/div[2]/div/section[2]/div/div[2]/div[1]/div/div/div[2]/div/div/ul/div/div[1]/li[1]'
    for item in c:
        d=item.text
        monthlist.append(d)
    noofmonths=len(monthlist)+1
    mh=driver.find_element(By.XPATH,yearstr)
    mh.click()
    # _______ clicks on dropdown YEAR to make options visible _______
    time.sleep(1)
    mh.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    mh.send_keys(Keys.ENTER)
    #driver.find_element(By.XPATH,f'/html/body/div/div/div[2]/div/section[2]/div/div[2]/div[1]/div/div/div[1]/div/div/ul/div/div[1]/li[{x}]').click()
    #_______click on 2023 to load 2023 links_______
    time.sleep(1)
    for y in range(1,noofmonths):
        print(f"  THIS IS THE Y: {y}")

        ##for 2022 xpath is as follows
        #//*[@id="PSYear"]/div[2]/div[3]
        ##_______click on dropdown Month to make it visible_______
        dropd = driver.find_element(By.XPATH,monthstr).click()
        time.sleep(1)

        time.sleep(1)
        
        ##_______click on Month to load that months links_______
        mhm=driver.find_element(By.XPATH,monthstr)
        mhm.click()
        time.sleep(1)
        mhm.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        mhm.send_keys(Keys.ENTER)
        time.sleep(1)
        #selected year = //*[@id="PSYear"]/div[1]
        #selected Month =//*[@id="PSMonth"]/div[1]
        year=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/section[2]/div/div[2]/div[1]/div/div/div[1]/div/div/input').get_property('value')
        month=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/section[2]/div/div[2]/div[1]/div/div/div[2]/div/div/input').get_property('value')
        print()
        print(year,"-",month)
        print()
        xlnamelist=[]
        xlurllist=[]
        ##new attaempt to add all links to dictionary
        try:
            dropd = driver.find_elements(By.XPATH,'//*[@id="react-tabs-1"]/div[2]/div/a')

            for items in dropd:
                xlurl=items.get_attribute("href")
                print(f"xlurl-{xlurl}")
                xlurllist.append(xlurl)
            dropd2 = driver.find_elements(By.XPATH,'//*[@id="react-tabs-1"]/div[2]/div/a/div/div[1]/h2')
            for items in dropd2:
                xlname=items.text
                xlnamelist.append(xlname)
                print(f"XLNAME-{xlname}")
                myTuplelist=[]
            for items in xlnamelist:
                myTuple = (str(year),'-',month,'-',items)
                keys=''.join(myTuple)
                print(f"keys-{keys}")
                Keyslist.append(keys)
                for items in xlurllist:
                    valuelist.append(items)
        except Exception as e:
            print(f"Exception is {e}")
            pass

print(f"keylist:{Keyslist}")
print(f"valuelist:{valuelist}")


driver.close()

z=dict(zip(Keyslist,valuelist))
with open("hdfc.json", "w") as outfile:
    json.dump(z,outfile)
print ("printing urldict")
print()

print(yearlist)
print(monthlist)
