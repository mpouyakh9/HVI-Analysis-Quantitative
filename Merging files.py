import pandas as pd
import xlrd
import os, glob
import re


# df = pd.read_excel('Excel files/Performance/Performance.xlsx', sheet_name='E-textiles')
df = pd.read_csv("Performance/e-textiles.csv", sep=",", header=0)
#df = pd.read_csv("Performance/phone.csv", sep=",", header=0)

print(df['Participant'])
etextiles = None
phone=None

for file in glob.glob('Excel files/*/*.xlsx'):

    df = pd.read_excel(str(file))
    df.to_csv(str(file)[:-5]+".csv",
                     index=None,
                     header=True)
    if (str(file).__contains__("phone")):
        print(str(file))
        df = pd.read_csv(str(file)[:-5]+".csv", sep=";", header=0)
        df.insert(0, "Participant", True)
        df.insert(1, "Scenario", True)
        if (str(file).__contains__("urban")):
            df['Scenario'] = re.findall("urban", str(file))[0]
            df['Participant'] = str(file)[16:-17]

        else:
            df['Scenario'] = re.findall("expressway", str(file))[0]
            df['Participant'] = str(file)[16:-22]

        phone = pd.concat([phone, df], axis=0)

       # df = pd.read_csv(file+".csv", sep=",", header=0)
    else:
        df = pd.read_csv(str(file)[:-5]+".csv", sep=";", header=0)
        df.insert(0, "Participant", True)
        df.insert(1, "Scenario", True)

        if (str(file).__contains__("urban")):
            df['Scenario'] = re.findall("urban", str(file))[0]
            df['Participant'] = str(file)[16:-22]

        else:
            df['Scenario'] = re.findall("expressway", str(file))[0]
            df['Participant'] = str(file)[16:-27]


        # df = pd.read_csv(file+".csv", sep=",", header=0)
        etextiles = pd.concat([etextiles, df], axis=0)

    #print(meta.at[X,'file'])

phone.to_csv("Performance/phonemetrics2.csv",
                     index=None,
                     header=True)

etextiles.to_csv("Performance/etextilesmetrics2.csv",
                     index=None,
                     header=True)

print(phone)

print(etextiles)




