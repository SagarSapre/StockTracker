from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.sbimf.com/portfolios")

driver.implicitly_wait(10)

##click on dropdown to make it visible
dropd = driver.find_element(By.XPATH,'//*[@id="PSYear"]').click()
time.sleep(3)
##click on 2023
dropd = driver.find_element(By.XPATH,'//*[@id="PSYear"]/div[2]/div[2]').click()
##for 2022 xpath is as follows
#//*[@id="PSYear"]/div[2]/div[3]

time.sleep(3)

selectdnld=driver.find_element(By.XPATH,'//*[@id="tblPortfoliosheets"]/tr[1]/td[1]/a').click()

time.sleep(3)

driver.close()