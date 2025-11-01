# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 18:04:26 2025

@author: lutho
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("wdi_wide.csv")

#6, a. relationship between emission by capita and internet use

Emission_per_capita = data["Emission per Capita"] = data["Greenhouse gas emissions"] / data ["Population"]

sns.relplot(data=data,x="Emission per Capita",y="Internet use")
plt.xlabel("Emission per Capita")
plt.ylabel("Internet use")
plt.title("Internet Use vs Emission per Capita")
plt.show()

#6, b. countries with high emission per capita

high_emissions = data[data["Emission per Capita"] > 0.03]
z=high_emissions[["Country Name", "Emission per Capita", "Internet use", "Region"]]
print(z)

#6, c. variation between region in respect to high emissions vs internet use

sns.relplot(data=high_emissions,x="Emission per Capita",y="Internet use",hue="Region",col="Region")
plt.xlabel("Emission per Capita")
plt.ylabel("Internet use")
plt.suptitle("High Emission Countries: Internet Use by Region")
plt.show()