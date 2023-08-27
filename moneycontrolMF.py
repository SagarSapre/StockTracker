import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
#import openpyxl as xl
#from openpyxl.utils import get_column_letter
#from openpyxl import load_workbook
from datetime import *
#import logging
#import time
#from time import perf_counter
################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
url = 'https://www.moneycontrol.com/mutual-funds/nav/parag-parikh-tax-saver-fund-direct-plan-growth/MPP013'
MF_code = url.split("/")[-1]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}


df = pd.DataFrame(columns=['url',
                            'MF_code',
                            'name',
                            'NAV',
                            'navdate',
                            'AMC',
                            'category',
                            'fundsize',
                            'fundcatmshare',
                            'expense_ratio',
                            'avg_exp_ratio_of_cat',
                            'portfolio_turnover',
                            'cat_avg_turnover',
                            'std_dev',
                            'cat_std_dev',
                            'beta',
                            'cat_beta',
                            'sharperatio',
                            'cat_sharperatio',
                            'treynors_ratio',
                            'cat_treynors_ratio',
                            'jensens_alpha',
                            'cat_jensens_alpha',
                            'fundmanager'
                            ])
errordf = pd.DataFrame(columns=['url', 'row', 'error_type', 'error_message'])

with requests.Session() as s:
    resp =s.get(url,headers=headers)
    htmlContent = resp.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    #  Scheme Name
    try:
        name = soup.find("h1", class_="page_heading navdetails_heading").text
    except Exception as error_message:
        name = "not Found"
        error_type = "Name not Found"
    #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]

    #  Scheme Category
    try:
        category = soup.find("span", class_="sub_category_text").string

    except Exception as error_message:
        category = "not Found"
        error_type = "category not Found"
        #    errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]
    # print(category)
    # AMC
    try:
        AMC = soup.find_all("span", class_="sub_category_text")[1].text
    except Exception as error_message:
        AMC = "not Found"
        error_type = "AMC not Found"
        #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]
    # print(AMC)
    try:
        NAV = soup.find("span", class_="amt").string.strip(" ₹")
    except Exception as error_message:
        NAV = 0
        error_type = "NAV not Found"
        #  errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]
        # print(NAV)

    # fund size in Crore
    try:
        fundsize = soup.find_all("span", class_="amt")[1].text.strip(" ₹").split()[0]
    except Exception as error_message:
        fundsize = 0
        error_type = "fundsize not Found"
        #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]
    # print(fundsize)

    # expense ratio in percent
    try:
        expense_ratio = soup.find_all("span", class_="amt")[2].text.replace('%', '')
    except Exception as error_message:
        expense_ratio = 0
        error_type = "expratio not Found"
        #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]
    # print(expense_ratio)

    # text data
    textlist = []
    try:
        stringstext = soup.find_all("div", class_="grayvalue")
        for items in stringstext:
            textlist.append(items.text)
    except Exception as error_message:
        textlist = textlist.append('not Found').append('not Found').append('not Found')
        navdate = fundcatmshare = avg_exp_ratio_of_cat = 0
        error_type = "stringstext not Found"
        #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]
    # print(textlist)

    # nav date
    try:
        navdate = textlist[0]
        navdate = navdate.replace('(', '').replace(')', '').replace('as on ', '')
        navdate = navdate.replace(', ', '-').replace('st', '').replace('th', '').replace('rd', '').replace(' ', '-')
        navdate = navdate.replace('Apr', '04').replace('May', '05').replace('June', '06').replace('Jul','07').replace('October', '10')
        navdate = datetime.strptime(navdate, '%d-%m-%Y').date()
    except Exception as error_message:
        navdate = "not Found"
        error_type = "NavDate not Found"

    try:
        fundcatmshare = textlist[1].split()[0].replace(' ', '').replace('(', '').replace('%', '')
        avg_exp_ratio_of_cat = textlist[2].split()[0].replace('(', '').replace('%', '')
    except Exception as error_message:
        fundcatmshare = avg_exp_ratio_of_cat = 0
        error_type = "catogory exp_ratio & Mkt Share not Found"
        #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]

    # portfolio turnover ratio
    try:
        portfolio_turnover = soup.find_all("div", class_="subheading")[0].contents[1].text.replace('%', '')
        cat_avg_turnover = soup.find_all("div", class_="subheading")[0].contents[3].text.replace('%', '')

    except Exception as error_message:

        portfolio_turnover = 0
        cat_avg_turnover = 0
        error_type = "portfolio turnover& cat_avg_turnover not Found"
        #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]

    # print(portfolio_turnover)

    # cat_avg turnover
    # print(cat_avg_turnover)

    # ratios
    
    stringslist = []
    try:
        ratios = soup.find("ul", class_="risk_ratios clearfix")

        std_dev = ratios("li")[0]("div", class_="percentage")[0]("span")[0].text
        cat_std_dev = ratios("li")[0]("div", class_="percentage")[0]("span")[2].text

        beta = ratios("li")[1]("div", class_="percentage")[0]("span")[0].text
        cat_beta = ratios("li")[1]("div", class_="percentage")[0]("span")[2].text

        sharperatio = ratios("li")[2]("div", class_="percentage")[0]("span")[0].text
        cat_sharperatio = ratios("li")[2]("div", class_="percentage")[0]("span")[2].text

        treynors_ratio = ratios("li")[3]("div", class_="percentage")[0]("span")[0].text
        cat_treynors_ratio = ratios("li")[3]("div", class_="percentage")[0]("span")[2].text

        jensens_alpha = ratios("li")[4]("div", class_="percentage")[0]("span")[0].text
        cat_jensens_alpha = ratios("li")[4]("div", class_="percentage")[0]("span")[2].text
    except Exception as error_message:
        std_dev = cat_std_dev = beta = cat_beta = sharperatio = cat_sharperatio = treynors_ratio = cat_treynors_ratio = jensens_alpha = cat_jensens_alpha = 0
        error_type = "ratios not Found"
        #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]

    # schemedetailurl scraped is stored in url2
    try:
        url2 = soup('div', class_='forbgmax clearfix')[0]('li', class_="main_sticky_menu")[6]('a')[0].get('href')
        r2 = requests.get(url2)
        htmlContent2 = r2.text
        soup2 = BeautifulSoup(htmlContent2, 'html.parser')
        # fundmanager
        fundmanagerscrap = soup2('ul', class_='schemedetails_list')[0]('li')[0]('a')
        fundmanagerlist = []
        for items in fundmanagerscrap:
            a = items.text
            fundmanagerlist.append(a)

        fundmanager = '-'.join(map(str, fundmanagerlist))
    except Exception as error_message:
        fundmanager = "not Found"
        error_type = "fundmanagers url not found"
        #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]

    try:
        NAV = float(NAV)
        fundsize = float(fundsize)
        fundcatmshare = float(fundcatmshare)
        expense_ratio = float(expense_ratio)
        avg_exp_ratio_of_cat = float(avg_exp_ratio_of_cat)
        portfolio_turnover = float(portfolio_turnover)
        cat_avg_turnover = float(cat_avg_turnover)
        std_dev = float(std_dev)
        cat_std_dev = float(cat_std_dev)
        beta = float(beta)
        cat_beta = float(cat_beta)
        sharperatio = float(sharperatio)
        cat_sharperatio = float(cat_sharperatio)
        treynors_ratio = float(treynors_ratio)
        cat_treynors_ratio = float(cat_treynors_ratio)
        jensens_alpha = float(jensens_alpha)
        cat_jensens_alpha = float(cat_jensens_alpha)
    except Exception as error_message:
        error_type = "float operation failed"
        #errordf.loc[len(errordf.index)] = [url, row, error_type, error_message]

    df.loc[len(df.index)] = [url,
                                    MF_code,
                                    name,
                                    NAV,
                                    navdate,
                                    AMC,
                                    category,
                                    fundsize,
                                    fundcatmshare,
                                    expense_ratio,
                                    avg_exp_ratio_of_cat,
                                    portfolio_turnover,
                                    cat_avg_turnover,
                                    std_dev,
                                    cat_std_dev,
                                    beta,
                                    cat_beta,
                                    sharperatio,
                                    cat_sharperatio,
                                    treynors_ratio,
                                    cat_treynors_ratio,
                                    jensens_alpha,
                                    cat_jensens_alpha,
                                    fundmanager]
#        idx += 1

    print("printing df")
    #errordf.to_excel('NAVerror.xlsx')
    df.to_excel('NAVPAGEDATA.xlsx')

url3 = soup('div', class_='forbgmax clearfix')[0]('li', class_="main_sticky_menu")[4]('a')[0].get('href')

####### end of  NAV PAGE #######



################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
