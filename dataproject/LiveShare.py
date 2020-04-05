import os
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

#Open the data file and taking a look at it
Data = 'Data.xlsx'
pd.read_excel(Data).head(5)

#Removing the first two rows as they are useless.
empl = pd.read_excel(Data, skiprows=2)
empl.head(5)

#Removing first 2 columns
drop_these = ['Unnamed: 0', 'Unnamed: 1']
empl.drop(drop_these, axis=1, inplace=True) # axis = 1 -> columns, inplace=True -> changed, no copy made
empl.head(5)

#Renaming the columns
empl.rename(columns = {'Unnamed: 2':'Sex'}, inplace=True)
empl.rename(columns = {'Unnamed: 3':'Education'}, inplace=True)
empl.head(5)

#Renaming years because having them as numbers can cause problems
years = {}
for i in range(2005,2019+1): # range from 2008 to but not including 2018
    years[str(i)] = f'e{i}'
empl.rename(columns = years, inplace=True)
empl.head(10)

