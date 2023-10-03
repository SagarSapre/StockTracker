import os

root='E:\\sagar\\2 sagar ORDER\\ORDER\\Prgramming\\python\\projects\\stocktracker\\mutual fund data\\sbi'

years = ['2017','2018','2019','2020','2021','2022','2023']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']


for year in years:
    ypath = os.path.join(root, year)
    os.mkdir(ypath)	
    for month in months:
        mpath = os.path.join(root,year,month)
        os.mkdir(mpath)




