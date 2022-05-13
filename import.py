import pandas as pd
import re

import xlrd
import os, glob
df = pd.read_excel('Performance/Performance2.xlsx', sheet_name='Phone')

df.to_csv("Performance/phone.csv",
                     index=None,
                     header=True)

df = pd.read_csv("Performance/e-textiles.csv", sep=",", header=0)
dfp = pd.read_csv("Performance/phone.csv", sep=",", header=0)
#print(dfp)
dfp = dfp[dfp['Participant'].isin(["P23","p23", "P08"])]
print(dfp)

dfp = dfp[((dfp.iloc[:,6]=='express') | (dfp.iloc[:,6]=='Express'))]

#print(dfp[(dfp.iloc[:,5]=='others') | (dfp.iloc[:,5]=='Others')]["Duration(sec)"].mean())

str2 = "P02-phone-expressway.xlsx"
str = re.findall("expressway", str2)[0]
#print(str2.__contains__("exffffpressway"))
print(str2[:6])
