#Defining what to show in table very likely there is an easier method, this was hell.
def filters(year, age, sex, education):
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

#Defining functions looking for changes.
def dropdown_year_eventhandler(change):
    filters(change.new, dropdown_age.value, dropdown_sex.value, dropdown_education.value)
def dropdown_age_eventhandler(change):
    filters(dropdown_year.value, change.new, dropdown_sex.value, dropdown_education.value)
def dropdown_sex_eventhandler(change):
    filters(dropdown_year.value, dropdown_age.value, change.new, dropdown_education.value)
def dropdown_education_eventhandler(change):
    filters(dropdown_year.value, dropdown_age.value, dropdown_sex.value, change.new)