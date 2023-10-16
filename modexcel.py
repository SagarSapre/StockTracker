# %%
import pandas as pd
import streamlit as st

# %%
path ='E:\\sagar\\2 sagar ORDER\\ORDER\\Prgramming\\python\\projects\\stocktracker\\mutual fund data\\sbi\\2021-January-SBI EQUITY HYBRID FUND PORTFOLIO.xlsx'

# %%
A=pd.read_excel(path)

# %%
cols = ['A','B','C','D','E','F','G','H','I','J']
A.columns = cols
print(A.columns)

# %%
A

# %%
#B=A.drop([0])

# %%
amc_name=A.iloc[0][2]
amc_name

# %%
as_on=A.iloc[2][3]
as_on

# %%
scheme_name=A.iloc[1][3]
scheme_name

# %%
b=A.axes
b
#172*9

# %%
b=A.drop([0,1,2,3],inplace=True)
b

# %%
b=A.drop(['A','B'] ,axis=1,inplace=True)
A

# %%
A.columns

'''

EQUITY & EQUITY RELATED
a) Listed/awaiting listing on Stock Exchanges
Total
b) Unlisted
c) Foreign Securities and /or overseas ETF
DEBT INSTRUMENTS
b) Privately Placed/Unlisted
c) Securitised Debt Instruments
d) Central Government Securities
e) State Government Securities
MONEY MARKET INSTRUMENTS
a) Commercial Paper
b) Certificate of Deposits
c) Treasury Bills
d) Bills Re- Discounting
OTHERS
a) Mutual Fund Units / Exchange Traded Funds
b) Gold
c) Short Term Deposits
d) Term Deposits Placed as Margins
e) TREPS / Reverse Repo Investments
Other Current Assets / (Liabilities)
DERIVATIVES
Stock Futures
Index Futures
Derivatives Total
3. Security is in default beyond its maturity date :

'''
