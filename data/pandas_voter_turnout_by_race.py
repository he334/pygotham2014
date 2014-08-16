
# coding: utf-8

# In[3]:

import pandas as pd
import matplotlib.pyplot as plt

votes = pd.read_csv('votes_by_assembly_district.csv')
demographics = pd.read_csv('assembly_district_demographics.csv')
df = pd.merge(votes, demographics, on='assemblydistrict')
print df

# rangel vs espaillat in majority black assembly districts
majorityBlack = df[(df.black > df.hispanic) & (df.black > df.white)][['assemblydistrict','rangel','espaillat']]
majorityBlack = majorityBlack.set_index('assemblydistrict')
majorityBlack.plot(kind='barh',title='Majority Black Districts')
plt.savefig("majorityBlackDistricts.png")

# rangel vs espaillat in majority hispanic assembly districts
majorityHispanic = df[(df.hispanic > df.black) & (df.hispanic > df.white)][['assemblydistrict','rangel','espaillat']]
majorityHispanic = majorityHispanic.set_index('assemblydistrict')
majorityHispanic.plot(kind='barh',title='Majority Hispanic Districts')
plt.savefig("majorityHispanicDistricts.png")


# In[ ]:



