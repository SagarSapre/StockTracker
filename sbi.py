from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from requests import get

driver = webdriver.Chrome()
driver.get("https://www.sbimf.com/portfolios")

driver.implicitly_wait(10)

##click on dropdown to make it visible
dropd = driver.find_element(By.XPATH,'//*[@id="PSYear"]').click()
time.sleep(1)
##click on 2023 to load 2023 links
dropd = driver.find_element(By.XPATH,'//*[@id="PSYear"]/div[2]/div[2]').click()
##for 2022 xpath is as follows
#//*[@id="PSYear"]/div[2]/div[3]

time.sleep(3)
selectdnld=driver.find_elements(By.XPATH,"//a[contains(text(),'All Schemes Monthly Portfolio')]")
urllist=[]
for items in selectdnld:
    urllist.append(items.get_attribute("href"))

#print(selectdnld)
print()
print(urllist)
print()
print(len(urllist))
#selectdnld=driver.find_element(By.XPATH,'//*[@id="tblPortfoliosheets"]/tr[1]/td[1]/a').click()

time.sleep(3)

driver.close()

def download_file(url, file_path):

    reply = get(url, stream=True)
    with open(file_path, 'wb') as file:
        for chunk in reply.iter_content(chunk_size=1024): 
            if chunk:
                file.write(chunk)

