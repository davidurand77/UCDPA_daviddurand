import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

#import data set fro Video Games Sales and check info and shape
vgsales = pd.read_csv(r"C:\Users\david\OneDrive\Documents\Specialist Certificate in Data Analytics Essentials\Video Games Sales\vgsales.csv")

print(vgsales.info())
print(vgsales.shape)

#count N/A data in dataset
count_NA = vgsales.isnull().sum()
print(count_NA)

#change data from " " to NaN
vgsales = vgsales.replace(r'\s+', np.nan, regex=True).replace(' ', np.nan)
print(val_data.info())


# number of occurrence of 'p'
#print('Number of occurrence of N/A:', vgsales.count('N/A'))

#with open("vgsales.csv", "r") as file_input:
#    with open("vgsalesnew.csv", "w") as output:
#        for line in file_input:
#            if line.strip("\n") != "N/A":
#                output.write(line)


#change data from " " to NaN
#vgsales = vgsales.replace(r'[^\d]', np.nan, regex=True)
#print(vgsales.info())

# sort dataset by platform and years
#platforms_by_years = vgsales.sort_values(by=["Platforms"], ascending=False)

#vgsales["Year"].replace(r'[^\d]', np.nan, regex=True)

#vgsales.groupby("Year").sum()

#for row in vgsales.iterrows():
#    if not row["Year"].match(r'\D', regex=True):
#        print(row)


#print(vgsales.info())

#group_by_years = vgsales.groupby("Year").sum()

#print(group_by_years.info)


# add a total to column global sales or even to all columns
# cleaning data from ? for data grouping (pokemon only?)
# list all ? in the dataset
# identify the lines to be changed
# replace ? where necessary

# create list for fifa per platform per year and geo for visualisation

# create list for overall sales of video games per year per geo






