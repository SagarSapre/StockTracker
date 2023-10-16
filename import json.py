
# this file download and save as xlsx based on json file contents
#%%
import time
import json
import os
import requests
from requests import get
with open('sbi2.json', 'r') as f:
        data = json.load(f)
#%%
file_path='E:\\sagar\\2 sagar ORDER\\ORDER\\Prgramming\\python\\projects\\stocktracker\\mutual fund data\\sbi\\'
url='https://www.sbimf.com/docs/default-source/scheme-portfolios/sbi-tax-advantage-fund---series-iii-87447420-7a95-4c47-a1df-dd000323b12f.xls?sfvrsn=7ebb1185_2'


#%%
for key, value in data.items():
    time.sleep(1)
    url =  value
    path = os.path.join(file_path,key+".xlsx")
    reply = get(url, stream=True)
    with open(path, 'wb') as file:
        for chunk in reply.iter_content(chunk_size=1024): 
            if chunk:
                file.write(chunk)




# %%
