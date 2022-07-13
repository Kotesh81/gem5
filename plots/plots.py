import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Read CSV into pandas
data = pd.read_csv(r"../se_results/res_exe_time_L3.txt", '\t')
data.head()
df = pd.DataFrame(data)
 
# print (df['simSeconds'])  
name = df['Benchmarks']
values = df['simSeconds']
 
# Figure Size
fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
plt.bar(name, df['simInsts'])
 
# Show Plot
plt.show()


# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# # set height of bar
# IT = [12, 30, 1, 8, 22]
# ECE = [28, 6, 16, 5, 10]
# CSE = [29, 3, 24, 25, 17]
 
# # Set position of bar on X axis
br1 = np.arange(len(df['simInsts']))
br2 = [x + barWidth for x in br1]

 
# Make the plot
plt.bar(br1, df['simInsts'], color ='r', width = barWidth,
        edgecolor ='grey', label ='Inst')
plt.bar(br2, df['simOps'], color ='g', width = barWidth,
        edgecolor ='grey', label ='Ops')
 
# Adding Xticks
plt.xlabel('Benchmark', fontweight ='bold', fontsize = 15)
plt.ylabel('Instructions', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(df['simInsts']))],
        name)
 
plt.legend()
plt.show()