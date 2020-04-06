import os
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

#Open the data file and taking a look at it
Data = 'Data.xlsx'
pd.read_excel(Data).head(5)

#Removing the first two rows as they are useless.
df = pd.read_excel(Data, skiprows=2)


#Removing first 2 columns
drop_these = ['Unnamed: 0', 'Unnamed: 1']
df.drop(drop_these, axis=1, inplace=True) # axis = 1 -> columns, inplace=True -> changed, no copy made


#Renaming the columns
df.rename(columns = {'Unnamed: 2':'Sex'}, inplace=True)
df.rename(columns = {'Unnamed: 3':'Education'}, inplace=True)
df.rename(columns = {'Unnamed: 4':'Age'}, inplace=True)


#Renaming years because having them as numbers can cause problems
years = {}
for i in range(2005,2019+1): # range from 2008 to but not including 2018
    years[str(i)] = f'year{i}'
df.rename(columns = years, inplace=True)


#find index of sex
total = df.loc[df["Sex"]=="Mænd og kvinder i alt"].index
male = df.loc[df["Sex"]=="Mænd"].index
female = df.loc[df["Sex"]=="Kvinder"].index
#rename sec to total, male, and female
df["Sex"][total] = "total"
df["Sex"][male] = "male"
df["Sex"][female] = "female"


#rename nan in sex to floats.
for i in range(0,len(df)):
    if type(df["Sex"][i]) == str:
        x = df["Sex"][i]
    else:
        df["Sex"][i] = x

#rename nan in Education to floats
for i in range(0,len(df)):
    if type(df["Education"][i]) == str:
        x = df["Education"][i]
    else:
        df["Education"][i] = x
df.head(5)

#Define unique values
ALL = 'ALL'

def unique_sorted_values_pluss_all(array):
    unique = array.unique().tolist
    unique.sort()
    unique.insert(0,ALL)
    return unique

#creating drop downs
dropdown_year = widgets.Dropdown(options=unique_sorted_values_pluss_all(df.Sex))

















#REEEEEEEEEEEEEEEEEEEEEEEEEEEE

df.head(5)
#Define long dataset for sex
df_long = pd.melt(df,id_vars=["Sex","Education","Age"])
df_long

#Define plot axes
def plot_s(df, Sex):
    I = df["Sex"] == Sex
    ax=df.loc[I,:].plot(x="variable", y='value', style='-o', legend=False)


widgets.interact(plot_s, 
    df = widgets.fixed(df_long),
    Sex = widgets.Dropdown(description='Sex', 
                                    options=df.Sex.unique(), 
                                    value='total'))