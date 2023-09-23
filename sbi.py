from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from requests import get
import json

driver = webdriver.Chrome()
driver.get("https://www.sbimf.com/portfolios")

driver.implicitly_wait(10)

##click on dropdown to make it visible
dropd = driver.find_element(By.XPATH,'//*[@id="PSYear"]').click()
time.sleep(3)
##click on 2023 to load 2023 links

dropd = driver.find_element(By.XPATH,'//*[@id="PSYear"]/div[2]/div[2]').click()
##for 2022 xpath is as follows
#//*[@id="PSYear"]/div[2]/div[3]
time.sleep(3)
##new attaempt to add all links to dictionary
dropd = driver.find_elements(By.XPATH,'//*[@id="tblPortfoliosheets"]/tr/td[1]/a')
print(len(dropd))

urllist=[]
monthtext=[]

for items in dropd:
    urllist.append(items.get_attribute("href"))
    monthtext.append(items.get_attribute("text"))
driver.close()
#time.sleep(3)
#selectdnld=driver.find_elements(By.XPATH,"//a[contains(text(),'All Schemes Monthly Portfolio')]")

'''
for items in selectdnld:
    urllist.append(items.get_attribute("href"))
    monthtext.append(items.get_attribute("text").split("- ")[1])
'''
urldict=dict(zip(monthtext,urllist))
with open("sbi.json", "w") as outfile:
    json.dump(urldict, outfile)
print ("printing urldict" +'/n')
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
