import numpy as np
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import tkinter as tk
import os
import ipywidgets as widgets
from IPython.display import display
import seaborn as sns

#Creating dropdown options
ALL = 'ALL'
# defning each option in the data set as unique and adding an option for all.
def unique_sorted_values_plus_all(array):
    liste = array.values.tolist()
    unique = np.unique(liste)
    unique.sort()
    unique = unique.tolist()
    unique.insert(0,ALL)
    return unique

#Defining what to show in the table, very likely that there is an easier method, this was hell.
# eg. if ALL is selected in all drop downs, it displays the full dataframe, if ALL is selected in each drop down but year then
# it displays the dataframe with the selected year from the drop down. and so on for all the different combinations.
def filters(year, age, sex, education, df_long, output, plot_output):
    output.clear_output()
    plot_output.clear_output()
    
    if (year == ALL) & (age == ALL) & (sex == ALL) & (education == ALL): # everything
        filters = df_long
    elif (age == ALL) & (sex == ALL) & (education == ALL) : # everything but year
        filters = df_long[df_long.year == year]
    elif (year == ALL) & (sex == ALL) & (education == ALL): # everything but age
        filters = df_long[df_long.age == age]
    elif (age == ALL) & (year == ALL) & (education == ALL): # everything but sex
        filters = df_long[df_long.sex == sex]
    elif (age == ALL) & (year == ALL) & (sex == ALL): # everything but education
        filters = df_long[df_long.education == education]
    elif (sex == ALL) & (education == ALL): # everything but year, age
        filters = df_long[(df_long.year == year) & (df_long.age == age)]
    elif (age == ALL) & (education == ALL): # everything but year, sex
        filters = df_long[(df_long.year == year) & (df_long.sex == sex)]
    elif (age == ALL) & (sex == ALL): # everything but year, education
        filters = df_long[(df_long.year == year) & (df_long.education == education)]
    elif (year == ALL) & (education == ALL): # everything but age sex
        filters = df_long[(df_long.age == age) & (df_long.sex == sex)]
    elif (year == ALL) & (sex == ALL): # everything but age education
        filters = df_long[(df_long.age == age) & (df_long.education == education)]
    elif (year == ALL) & (age == ALL): # everything but sex education
        filters = df_long[(df_long.sex == sex) & (df_long.education == education)]
    elif (year == ALL): # everything but age sex education
        filters = df_long[(df_long.age == age) & (df_long.sex == sex) & (df_long.education == education)]
    elif (age == ALL): # everything but year sex education
        filters = df_long[(df_long.year == year) & (df_long.sex == sex) & (df_long.education == education)]
    elif (sex == ALL): # everything but year age education
        filters = df_long[(df_long.year == year) & (df_long.age == age) & (df_long.education == education)]
    elif (education == ALL): # everything but year age sex
        filters = df_long[(df_long.year == year) & (df_long.age == age) & (df_long.sex == sex)]
    else:
        filters = df_long[(df_long.year == year) & (df_long.age == age) & (df_long.sex == sex) & (df_long.education == education)]
    
    with output:
        display(filters)
    with plot_output:
        sns.kdeplot(filters['uddannelsesaktivitet'], shade=True)
        plt.show()
