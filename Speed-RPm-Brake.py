import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dfex = pd.read_csv("Performance/e-textiles.csv", sep=",", header=0)
dfpx = pd.read_csv("Performance/phone.csv", sep=",", header=0)

dfee = pd.read_csv("Performance/etextilesmetrics2.csv", sep=",", header=0)
dfpp = pd.read_csv("Performance/phonemetrics.csv", sep=",", header=0)

for X in range(len(dfee)):
    dfee.at[X, 'System Time'] = dfee.at[X, 'System Time'][11:]

for X in range(len(dfpp)):
    dfpp.at[X, 'System Time'] = dfpp.at[X, 'System Time'][11:]

dfee["System Time"] = pd.to_numeric(dfee["System Time"], downcast="float")
dfpp["System Time"] = pd.to_numeric(dfpp["System Time"], downcast="float")

dfee = dfee[~dfee['Participant'].isin(["P23","p23", "P08"])]
dfpx = dfpx[~dfpx['Participant'].isin(["P23","p23", "P08"])]
dfpp = dfpp[~dfpp['Participant'].isin(["P23","p23", "P08"])]

#print(dfee['Participant'].unique())
#print(dfex.loc[295,'To'])


#dfex = dfex[(dfex['Scenario']=='express')& (dfex['Function'].str.contains('Vol-up/down'))]
#print(dfex.loc[2,'To'])
#print((dfex.loc[2,'To']+dfex.loc[2,'From'])/2)

#print(round((dfex.loc[295,'To']+dfex.loc[295,'From'])/2,1))
rrr = dfpp.loc[(dfpp['Participant'] == dfpx.loc[296,'Participant']) & (dfpp['Scenario'] == dfpx.loc[296,'Scenario'])  & (dfpp['Scenario'] == dfpx.loc[296,'Scenario']) & (round(dfpp['System Time'],1) ==round((dfpx.loc[296,'To']+dfpx.loc[296,'From'])/2,1)),"RPM"]
print(rrr.to_frame())
print(len(dfpx))
for X in range(len(dfpx)):
    dfpx.loc[X, 'Speed'] = dfpp.loc[(dfpp['Participant'] == dfpx.loc[X,'Participant']) & (dfpp['Scenario'] == dfpx.loc[X,'Scenario']) & (round(dfpp['System Time'],1) ==round((dfpx.loc[X,'To']+dfpx.loc[X,'From'])/2,1)),'Speed'].to_frame().mean()[0]

for X in range(len(dfpx)):
    dfpx.loc[X, 'RPM'] = dfpp.loc[(dfpp['Participant'] == dfpx.loc[X,'Participant']) & (dfpp['Scenario'] == dfpx.loc[X,'Scenario']) & (round(dfpp['System Time'],1) ==round((dfpx.loc[X,'To']+dfpx.loc[X,'From'])/2,1)),'RPM'].to_frame().mean()[0]

for X in range(len(dfpx)):
    dfpx.loc[X, 'Brake'] = dfpp.loc[(dfpp['Participant'] == dfpx.loc[X,'Participant']) & (dfpp['Scenario'] == dfpx.loc[X,'Scenario']) & (round(dfpp['System Time'],1) ==round((dfpx.loc[X,'To']+dfpx.loc[X,'From'])/2,1)),'BrakePedalPosition'].to_frame().mean()[0]

#print(dfpx.loc[:,'Speed'])

#print(dfex.groupby(['Function', 'Scenario'])['Speed'].count())
#dfee.drop(['Unnamed: 7'])
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
#print(dfee.loc[:,'Participant':'RPM'])
print(dfpx.loc[:,['Participant','Scenario','From','To','Duration','Function','Speed','Brake','RPM']])