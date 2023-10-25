# %%
import pandas as pd
import streamlit as st 
from datetime import datetime
#this files import xl file into panda and saves it in modified form

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
as_on=A.iloc[2][3].strftime("%Y-%m-%d")
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

# %%
equity_loc=A.index[A['C']=='EQUITY & EQUITY RELATED'].tolist()[0]
st.text(f'*equity_loc is {equity_loc}')
# %%
listed_eq_loc=A.index[A['C']=='a) Listed/awaiting listing on Stock Exchanges'].tolist()[0]
st.text(f'listed_eq_loc is {listed_eq_loc}')
# %%
unlisted_eq_loc=A.index[A['C']=='b) Unlisted'].tolist()[0]
st.text(f'unlisted_eq_loc is {unlisted_eq_loc}')
# %%
foreign_loc=A.index[A['C']=='c) Foreign Securities and /or overseas ETF'].tolist()[0]
st.text(f'foreign_loc is {foreign_loc}')

# %%
debt_loc=A.index[A['C']=='DEBT INSTRUMENTS'].tolist()[0]
st.text(f'*debt_loc is {debt_loc}')
# %%
listed_dt_loc=A.index[A['C']=='a) Listed/awaiting listing on the stock exchanges'].tolist()[0]
st.text(f'listed_dt_loc is {listed_dt_loc}')
# %%
unlisted_dt_loc=A.index[A['C']=='b) Privately Placed/Unlisted'].tolist()[0]
st.text(f'unlisted_dt_loc is {unlisted_dt_loc}')
# %%
securitised_dt_loc=A.index[A['C']=='c) Securitised Debt Instruments'].tolist()[0]
st.text(f'securitised_dt_loc is {securitised_dt_loc}')
# %%
cg_dt_loc=A.index[A['C']=='d) Central Government Securities'].tolist()[0]
st.text(f'cg_dt_loc is {cg_dt_loc}')
# %%
sg_dt_loc=A.index[A['C']=='e) State Government Securities'].tolist()[0]
st.text(f'sg_dt_loc is {sg_dt_loc}')
# %%
mn_mkt_loc=A.index[A['C']=='MONEY MARKET INSTRUMENTS'].tolist()[0]
st.text(f'*mn_mkt_loc is {mn_mkt_loc}')
# %%
cp_loc=A.index[A['C']=='a) Commercial Paper'].tolist()[0]
st.text(f'CP_loc is {cp_loc}')

# %%
cd_loc=A.index[A['C']=='b) Certificate of Deposits'].tolist()[0]
st.text(f'CD_loc is {cd_loc}')
# %%
treasury_loc=A.index[A['C']=='c) Treasury Bills'].tolist()[0]
st.text(f'treasury_loc is {treasury_loc}')
# %%
billdisc_loc=A.index[A['C']=='d) Bills Re- Discounting'].tolist()[0]
st.text(f'billdisc_loc is {billdisc_loc}')
# %%
others_loc=A.index[A['C']=='OTHERS'].tolist()[0]
st.text(f'*OTHERS_loc is {others_loc}')
# %%
mf_loc=A.index[A['C']=='a) Mutual Fund Units / Exchange Traded Funds'].tolist()[0]
st.text(f'MF_loc is {mf_loc}')
# %%
gold_loc=A.index[A['C']=='b) Gold'].tolist()[0]
st.text(f'gold_loc is {gold_loc}')
# %%
std_loc=A.index[A['C']=='c) Short Term Deposits'].tolist()[0]
st.text(f'std_loc is {std_loc}')
# %%
td_margins_loc=A.index[A['C']=='d) Term Deposits Placed as Margins'].tolist()[0]
st.text(f'td_margins_loc is {td_margins_loc}')
# %%
treps_loc=A.index[A['C']=='e) TREPS / Reverse Repo Investments'].tolist()[0]
st.text(f'treps_loc is {treps_loc}')
# %%
ca_cl_loc=A.index[A['C']=='Other Current Assets / (Liabilities)'].tolist()[0]
st.text(f'ca_cl_loc is {ca_cl_loc}')

# %%
total_locs=A.index[A['C']=='Total'].tolist()
st.text(f'__Total_locs is {total_locs}')
# %%
total_empty_locs=A.index[A['C'].isnull()].tolist()
st.text(f'__total_Empty_locs is {total_empty_locs}')
# %%
fno_loc=A.index[A['C']=='DERIVATIVES'].tolist()[0]
st.text(f'fno_loc is {fno_loc}')
# %%
try:
    idx_fut_loc=A.index[A['C']=='Index Futures'].tolist()[0]
    st.text(f'idx_fut_loc is {idx_fut_loc}')
except:
    st.text(f'idx_fut is not in portfolio')
# %%
try:
    stk_fut_loc=A.index[A['C']=='Stock Futures'].tolist()[0]
    st.text(f'stk_fut_loc is {stk_fut_loc}')
except:
    st.text(f'stk_fut is not in portfolio')
# %%
try:
    fno_total_loc=A.index[A['C']=='Derivatives Total'].tolist()[0]
    st.text(f'fno_total_loc is {fno_total_loc}')
except:
    st.text('No Derivatives in Portfolio')
# %%
treasury_loc=A.index[A['C']=='e) STRIPS']
AAAA=len(treasury_loc)
#.tolist()[0]
if AAAA>=1:
    treasury_loc=A.index[A['C']=='e) STRIPS'].tolist()[0]
    st.text(f'treasury_loc is {treasury_loc}')
else:
    st.text('No STRIPS in Portfolio')
AAAA
# %%
total_n_empty_locs =total_locs+total_empty_locs
# %%
try:
    idx_Opt_loc=A.index[A['C']=='Index Options'].tolist()[0]
    st.text(f'Index Options loc is {idx_Opt_loc}')
except:
    st.text('Index Options is not in portfolio')
# %%
try:
    stk_Opt_loc=A.index[A['C']=='Stock Options'].tolist()[0]
    st.text(f'stk_Opt_loc is {stk_Opt_loc}')
except:
    st.text('Stock Options is not in portfolio')
#%%
instrument_name=[A.iloc[0][0],A.iloc[0][1],A.iloc[0][2],A.iloc[0][3],A.iloc[0][4],A.iloc[0][5],A.iloc[0][6],A.iloc[0][7]]
instrument_name
# %%
print(type(instrument_name))
# %%
A.insert(0, 'as_on', as_on)
# %%
A.insert(0, 'SCHEME NAME', scheme_name)
# %%
A.insert(0, 'AMC Name', amc_name)
# %%
A.insert(4, 'Type',None)
# %%
A.insert(5, 'Subtype',None)
# %%
A.loc[equity_loc+2:debt_loc-1, 'Type'] = 'EQUITY & EQUITY RELATED'
# %%
A.loc[debt_loc+2:mn_mkt_loc-1, 'Type'] = 'DEBT INSTRUMENTS'
# %%
A.loc[mn_mkt_loc+2:others_loc-1, 'Type'] = 'MONEY MARKET INSTRUMENTS'
# %%
A.loc[others_loc+2:total_locs[-1], 'Type'] = 'OTHERS'
# %%
A.loc[fno_loc+3:fno_total_loc-1, 'Type'] = 'DERIVATIVES'
# %%
cols = ['AMC Name','SCHEME NAME','as_on',instrument_name[0],'Type','Subtype',instrument_name[1],instrument_name[2],instrument_name[3],instrument_name[4],instrument_name[5],instrument_name[6],instrument_name[7]]
A.columns = cols
print(A.columns)
# %%
A.loc[listed_eq_loc+1:unlisted_eq_loc-2, 'Subtype'] = 'Listed/awaiting listing'
# %%
A.loc[listed_eq_loc+1:unlisted_eq_loc-2, 'Subtype'] = 'Listed/awaiting listing'
# %%
A