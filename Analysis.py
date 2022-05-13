import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dfex = pd.read_csv("Performance/e-textiles.csv", sep=",", header=0)
dfpx = pd.read_csv("Performance/phone.csv", sep=",", header=0)
#print(dfp)
#dfp = dfp[~dfp['Participant'].isin(["P23","p23", "P08"])]
#print(dfp['Function'].unique())
#sns.set_style('darkgrid')
#sns.set_palette('Set2')

#sns.boxplot(data=dfp[dfp['Scenario']=='express'], x='Function', y='Duration', order= ["Vol-up/down", "next/previous" ,"pause/play","others"])
#sns.swarmplot(data=dfp[dfp['Scenario']=='express'], x='Function', y='Duration',color=".4", order= ["Vol-up/down", "next/previous" ,"pause/play","others"])
#plt.title('Phone-Expressway')
#plt.show()
#=================================================================================

dfee = pd.read_csv("Performance/etextilesmetrics.csv", sep=",", header=0)
dfpp = pd.read_csv("Performance/phonemetrics.csv", sep=",", header=0)
#for X in range(len(dfee)):
#    dfee.at[X, 'System Time'] = dfee.at[X, 'System Time'][9:]

#for X in range(len(dfpp)):
#    dfpp.at[X, 'System Time'] = dfpp.at[X, 'System Time'][9:]


#fig, ax = plt.subplots(figsize=(20,7))
# use unstack()

#print(type(dfpp['Speed'][100]))

#dfpp["Speed"] = pd.to_numeric(dfpp["Speed"], downcast="float")
#print(type(dfpp['Speed'][2000]))

dfpp.insert(10, "mavg", True)
for X in dfpp['Participant'].unique():
    for Y in dfpp['Scenario'].unique():
        dfpp.loc[((dfpp['Participant'] == X) & (dfpp['Scenario'] == Y)), 'mavg']=dfpp[((dfpp['Participant'] == X) & (dfpp['Scenario'] == Y))]['BrakePedalPosition'].rolling(150).mean()

dfee.insert(10, "mavg", True)
for X in dfee['Participant'].unique():
    for Y in dfee['Scenario'].unique():
        dfee.loc[((dfee['Participant'] == X) & (dfee['Scenario'] == Y)), 'mavg']=dfee[((dfee['Participant'] == X) & (dfee['Scenario'] == Y))]['BrakePedalPosition'].rolling(150).mean()

#mmavg = dfpp.groupby(['Participant', 'Scenario'])['Speed'].rolling(100).mean().reset_index()
#mmavg = mmavg.sort_values(by=['level_2'], ascending=True)
#print(mmavg)

#dfpp['mavg'] = mmavg['Speed']
#mmavg = mmavg.dropna()

dfpp = dfpp.dropna(subset = ["mavg"])
dfpp["mavg"] = pd.to_numeric(dfpp["mavg"], downcast="float")

dfee = dfee.dropna(subset = ["mavg"])
dfee["mavg"] = pd.to_numeric(dfee["mavg"], downcast="float")
print(dfpp['mavg'])

#dfpp.set_index('Total Milliseconds')
#dfpp[dfpp['Scenario'] == 'express'].groupby('Participant')['mavg'].plot(legend=True)


#fig, ax = plt.subplots(figsize=(15,7))
#dfpp[dfpp['Scenario'] == 'express'].groupby(['Total Milliseconds','Participant'])['mavg'].plot(ax=ax)
#plt.show()
#print(dfpp[dfpp['Scenario'] =='expressway'])

#print(dfpp[((dfpp['Participant'] == 'P02') & (dfpp['Scenario'] =='expressway') & (dfpp['Total Milliseconds'].between(0, 350000)))])
#print(dfpp.loc[((dfpp['Participant'] == 'P23') & (dfpp['Scenario'] =='expressway')),'Total Milliseconds'])
#print(dfpp.loc[dfpp['Participant'] == 'P02',['Participant','Total Milliseconds','mavg']])

#dfpp[((dfpp['Participant'] == 'P23') & (dfpp['Scenario'] =='expressway'))]['Total Milliseconds'] = dfpp.loc[((dfpp['Participant'] == 'P23') & (dfpp['Scenario'] =='expressway')),'Total Milliseconds'].between(50000, 350000)



#dfpp[(dfpp['Participant'] == 'P20') & (dfpp['Scenario'] =='expressway')].plot(x='Total Milliseconds', y='mavg',figsize=(20,7), grid=True, color='blue')
sns.relplot(data= dfpp[(dfpp['Scenario'] =='expressway' )& (dfpp['Total Milliseconds'].between(0, 350000))], x="Total Milliseconds", y="mavg", hue="Participant", kind="line",height = 7,  aspect = 4)
sns.relplot(data= dfee[(dfee['Scenario'] =='expressway' )& (dfee['Total Milliseconds'].between(0, 350000))], x="Total Milliseconds", y="mavg", hue="Participant", kind="line",height = 7,  aspect = 4)

plt.show()