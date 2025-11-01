# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 22:34:58 2025

@author: Danial Hakimikhiabani, Jacob Mockler
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


#7, number of Regions and High Income Economies
f = data.value_counts("Region")
g = data.value_counts("High Income Economy")
print (f,g)

# 8. Where are the high income economies?” (per region)
h = pd.crosstab(data['Region'],data['High Income Economy'])

print (h)

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


#5, creating a new gender column for faceting.

female = data.copy()
female["Gender"] = "Female"
female["Life expectancy"] = female["Life expectancy, female"]

male = data.copy()
male["Gender"] = "Male"
male["Life expectancy"] = male["Life expectancy, male"]


data_for_each_gender = pd.concat([female, male], ignore_index=True)



#5, a. relationship between life expectancy and internet use

sns.relplot(data=data_for_each_gender, x="Life expectancy",y="Internet use",col="Gender",)
plt.suptitle("% of Internet Use vs Life Expectancy")
plt.xlabel("Life expectancy (years)")
plt.ylabel("Internet use (%)")
plt.show()


#5, b. relationship between number of physicians and life expectancy

sns.relplot(data=data_for_each_gender,x="Physicians",y="Life expectancy",col="Gender",hue="High Income Economy")   
plt.suptitle("Physicians vs Life expectancy")
plt.xlabel("Physicians")
plt.ylabel("Life expectancy")
plt.show()

#5, c. relationship between Greenhouse gas emissions and life expectancy

sns.relplot(data=data_for_each_gender,x="Greenhouse gas emissions",y="Life expectancy",col="Gender")
plt.suptitle("Emissions vs Life expectancy")
plt.xlabel("Greenhouse gas emissions")
plt.xscale('log')   #my data was squeezed between 0 and 0.2 because the scale was big, i used log scale to make it spread out
plt.ylabel("Life expectancy")
plt.show()

#5, d. relationship between the total population and life expectancy

sns.relplot(data=data_for_each_gender, x="Population", y="Life expectancy", col="Gender",hue="Region")
plt.suptitle("Population vs Life expectancy")
plt.xlabel("Population")
plt.xscale('log') #I used it here for the same reason as before
plt.ylabel("Life xpectancy ")
plt.show()

#5, e. relationship between the number of women with tertiary education and life expectancy

sns.relplot(data=data_for_each_gender, x="Tertiary education, female", y="Life expectancy", col="Gender")
plt.suptitle("Tertiary education (female) vs Life expectancy")
plt.xlabel("Tertiary education (female)")
plt.ylabel("Life xpectancy ")
plt.show()


#6, a. relationship between emission by capita and internet use

Emission_per_capita = data["Emission per Capita"] = data["Greenhouse gas emissions"] / data ["Population"]

sns.relplot(data=data,x="Emission per Capita",y="Internet use")
plt.xlabel("Emission per Capita")
plt.ylabel("Internet use")
plt.title("Internet Use vs Emission per Capita")
plt.show()

#6, b. countries with high emission per capita

high_emissions = data[data["Emission per Capita"] > 0.003]
z=high_emissions[["Country Name", "Emission per Capita", "Internet use", "Region"]]
print(z)

#6, c. variation between region in respect to high emissions vs internet use

sns.relplot(data=high_emissions,x="Internet use",y="Emission per Capita",hue="Region",col="Region")
plt.xlabel("Internet Use")
plt.ylabel("High emissions")
plt.suptitle("High Emission: Internet Use by Region")
plt.show()

#6, d. relationship between high emission countries and high economies 

sns.relplot(data=high_emissions,x="High Income Economy",y="Emission per Capita")
plt.xlabel("High Income Economy")
plt.ylabel("High emissions")
plt.suptitle("High Emission vs High Income Economy")
plt.show()