# %%
import requests
from bs4 import BeautifulSoup
from lxml import etree



# %%
import csv
import pandas as pd

# %%
url="https://www.moneycontrol.com/mutual-funds/find-fund/returns?&amc=BIRMUTF,AXMF,ANZGRMUTF,BAXMF,BOBMUF,CANMUTF,DSPMLMF,EDELWMF,TEMMUFT,HDFCMUTF,HSBCMUTF,PRUICM,IDBIMF,IDFMF,IIFLMF,ILFSMF,INDIABMF,LIMF,ITIMF,JMMTFN,KMFLAMC,LICAMCL,MAHMF,MIRAEMF,MOMF,PEERMF,RELCAPM,NJMF,PMF,PPFMF,ESCOMUF,QMF,SAMCOMF,SBIMUTF,SHMF,SUNMUTF,TATMUTF,TAUMUTF,TMF,UKBCMF,UTIMUTFD,YESMF&invtype=Equity&category=Equity%20-%20ETF%2FIndex,Multi%20Cap%20Fund,Large%20Cap%20Fund,Large%20%26%20Mid%20Cap%20Fund,Mid%20Cap%20Fund,Small%20Cap%20Fund,ELSS,Dividend%20Yield%20Fund,Sectoral%2FThematic,Contra%20Fund,Focused%20Fund,Value%20Fund,Flexi%20Cap%20Fund&rank=1,2,3,4,5,0"


# %%
def send_request():
    r = requests.get(url)
    return r

r=send_request()

# %%
soup = BeautifulSoup(r.text, "html.parser")
dom = etree.HTML(str(soup))
firstfund=dom.xpath('//*[@id="dataTableId"]/tbody/tr[1]/td[1]/a')
firstfundlink=dom.xpath('//*[@id="dataTableId"]/tbody/tr[1]/td[1]/a/@href')

# %%
print(firstfund[0].text)
print(firstfundlink[0])

# %%
fundname_list=[]
fund_nav_url_list=[]

# %%
for i in range(277):
    i=i+1
    xpathcodetext=f'//*[@id="dataTableId"]/tbody/tr[{i}]/td[1]/a'
    xpathcodeurl=f'//*[@id="dataTableId"]/tbody/tr[{i}]/td[1]/a/@href'
    fundname=dom.xpath(xpathcodetext)
    fundname=fundname[0].text
    fundname_list.append(fundname)
    fund_nav_url=dom.xpath(xpathcodeurl)[0]
    fund_nav_url_list.append(fund_nav_url)


# %%
print(fundname_list[276])
print(fund_nav_url_list[276])

# %%
print(len(fundname_list))
print(len(fund_nav_url_list))

# %%
fund_dict = dict(zip(fundname_list,fund_nav_url_list))


# %%
df = pd.DataFrame.from_dict(fund_dict,orient='index')
df

# %%
df.to_excel("navlist.xlsx")


