import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Read CSV into pandas
colnames=['Time', 'Values']
data = pd.read_csv(r"../se_results/hist_data.txt", '    ', names=colnames)
data.head()
df = pd.DataFrame(data)

data_L3 = pd.read_csv(r"../se_results/hist_data_L3.txt", '    ', names=colnames)
data_L3.head()
df_L3 = pd.DataFrame(data)

df_new = df.groupby(df['Time'], sort=False).aggregate({'Time':'first','Values':'sum'})
df_new_L3 = df_L3.groupby(df['Time'], sort=False).aggregate({'Time':'first','Values':'sum'})
# print (df)
 
# print(df['Time'].eq('samples'))
# df_new.drop([df_new['Time'] == 'samples'].index, inplace=True)
df_new.drop(df_new[(df_new['Time'] == 'samples') ].index, inplace=True)
df_new.drop(df_new[(df_new['Time'] == 'gmean') ].index, inplace=True)
df_new.drop(df_new[(df_new['Time'] == 'mean') ].index, inplace=True)
df_new.drop(df_new[(df_new['Time'] == 'stdev') ].index, inplace=True)
df_new.drop(df_new[(df_new['Time'] == 'total') ].index, inplace=True)

df_new_L3.drop(df_new[(df_new['Time'] == 'samples') ].index, inplace=True)
df_new_L3.drop(df_new[(df_new['Time'] == 'gmean') ].index, inplace=True)
df_new_L3.drop(df_new[(df_new['Time'] == 'mean') ].index, inplace=True)
df_new_L3.drop(df_new[(df_new['Time'] == 'stdev') ].index, inplace=True)
df_new_L3.drop(df_new[(df_new['Time'] == 'total') ].index, inplace=True)

# df_new = df[df_new.Time == 'samples']
# df_new.drop(df[df['Time'] == 'gmean'].index)
# df_new.drop(df[df['Time'] == 'mean'].index)
# df_new.drop(df[df['Time'] == 'total'].index)
print(df_new)
print(df_new_L3)

names = df_new['Time']
Values = df_new['Values']

names_L3 = df_new['Time']
Values_L3 = df_new['Values']

# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# # set height of bar
# IT = [12, 30, 1, 8, 22]
# ECE = [28, 6, 16, 5, 10]
# CSE = [29, 3, 24, 25, 17]
 
# # Set position of bar on X axis
br1 = np.arange(len(names))
br2 = [x + barWidth for x in br1]
# Make the plot
plt.bar(br1, Values, color ='r', width = barWidth,
        edgecolor ='grey', label ='without L3')
plt.bar(br2, Values_L3, color ='g', width = barWidth,
        edgecolor ='grey', label ='with L3')
 
# Adding Xticks
plt.xlabel('Bins', fontweight ='bold', fontsize = 15)
plt.ylabel('Count', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(names))],
        names)
 
plt.legend()
plt.show()

# # Figure Size
# fig = plt.figure(figsize =(10, 7))
 
# # Horizontal Bar Plot
# plt.bar(names, Values)
 
# # Show Plot
# plt.show()