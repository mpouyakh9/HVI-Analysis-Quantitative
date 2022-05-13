import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


dfee = pd.read_csv("Performance/etextilesmetrics.csv", sep=",", header=0)
dfpp = pd.read_csv("Performance/phonemetrics.csv", sep=",", header=0)
#dfpp = dfpp[((dfpp['Participant'] == 'P02') & (dfpp['Scenario'] =='expressway') & (dfpp['Total Milliseconds'].between(50000, 1000000000)))]
#print(dfpp[(dfpp['Participant'] == 'P02') & (dfpp['Scenario'] =='expressway')]['Total Milliseconds'])
ttt = dfpp[((dfpp['Participant'] == 'P20') & (dfpp['Scenario'] =='expressway'))][['Total Milliseconds', 'Speed']]

ttt['mavg'] = dfpp[((dfpp['Participant'] =='P20') & (dfpp['Scenario'] =='expressway'))]['Speed'].rolling(100).mean()
print(ttt)
ttt.dropna(inplace=True)
ttt.plot(x='Total Milliseconds', y='mavg',figsize=(20,7), grid=True, color='green')

plt.show()