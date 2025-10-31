# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 22:34:58 2025

@author: lutho
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("wdi_wide.csv")


#3, list of the size and datatype
a = data.info()


#4, number of unique values for each column
b = data.nunique()


#5, gives important statistical values (mean, median etc.)
c = data.describe()

# 6. Adding a GNI per Capita column and using round function to round it to nearest cent
d = data["GNI per Capita"] = data["GNI"] / data ["Population"]
e = round(d,1)

# 7. a) how many countries are there in each region
f = data.value_counts("Region")


# 8. Where are the high income economies?” (per region)
h = pd.crosstab(data['Region'],data['High Income Economy'])


d = data["GNI per Capita"] = data["GNI"] / data ["Population"]
e = round(d,1)
f = data.value_counts("Region")
g = data.value_counts("High Income Economy")
h = pd.crosstab(data['Region'],data['High Income Economy'])


#9, loop for female life expectancy

data[["Life expectancy, female"]]
countries = []
for i in range(len(data)):
    if data["Life expectancy, female"][i] > 80:
        countries.append(data["Country Name"][i])

i= ("Number of Countries:", len(countries))
j= ("countries:", countries)


#Part 4

#1, plots to see association between GNA per capita and life expectancy

#female
sns.relplot(data=data, x="GNI per Capita", y="Life expectancy, female")
plt.xlabel("GNI per capita")
plt.ylabel("Female Life Expectancy (years)")
plt.title("GNI per capita vs Female Life Expectancy")
plt.show()


#male
sns.relplot(data=data, x="GNI per Capita", y="Life expectancy, male")
plt.xlabel("GNI per capita")
plt.ylabel("Male Life Expectancy (years)")
plt.title("GNI per capita vs Male Life Expectancy")
plt.show()


#2, plots to see if the association between GNA per capita and life expectancy
#varies by region

#female
sns.relplot(data=data, x="GNI per Capita", y="Life expectancy, female",hue="Region")
plt.xlabel("GNI per capita")
plt.ylabel("Female Life Expectancy (years)")
plt.title("GNI per capita vs Female Life Expectancy")
plt.show()

#male
sns.relplot(data=data, x="GNI per Capita", y="Life expectancy, male",hue="Region")
plt.xlabel("GNI per capita")
plt.ylabel("Male Life Expectancy (years)")
plt.title("GNI per capita vs Male Life Expectancy")
plt.show()


#3, standard deviation for previous plots


#female
sns.relplot(data=data, x="GNI per Capita", y="Life expectancy, female",hue="Region"
,kind="line",errorbar="sd")
plt.xlabel("GNI per capita")
plt.ylabel("Female Life Expectancy (years)")
plt.title("GNI per capita vs Female Life Expectancy")
plt.show()



#male
sns.relplot(data=data, x="GNI per Capita", y="Life expectancy, male",hue="Region",
kind="line",errorbar="sd")
plt.xlabel("GNI per capita")
plt.ylabel("Male Life Expectancy (years)")
plt.title("GNI per capita vs Male Life Expectancy")
plt.show()


#4, linear regression for previous plots


#female 
sns.lmplot(data=data,x="GNI per Capita", y="Life expectancy, female", hue="Region")
plt.title("Linear Regression: Female Life Expectancy vs GNI per capita")
plt.xlabel("GNI per capita")
plt.ylabel("Female Life Expectancy (years)")
plt.show()



#male
sns.lmplot(data=data,x="GNI per Capita", y="Life expectancy, male",hue="Region")
plt.title("Linear Regression: Male Life Expectancy vs GNI per capita")
plt.xlabel("GNI per capita ")
plt.ylabel("Male Life Expectancy (years)")
plt.show()