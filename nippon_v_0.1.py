from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from requests import get
import json

driver = webdriver.Chrome()
driver.get("https://mf.nipponindiaim.com/investor-service/downloads/factsheet-and-other-portfolio-disclosures")

driver.close()