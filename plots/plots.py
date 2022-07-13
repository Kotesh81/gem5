import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Read CSV into pandas
data = pd.read_csv(r"../se_results/res_exe_time.txt", '\t')
data.head()
df = pd.DataFrame(data)
 
data_L3 = pd.read_csv(r"../se_results/res_exe_time_L3.txt", '\t')
data_L3.head()
df_L3 = pd.DataFrame(data_L3)

# print (df['simSeconds'])  
name = df['Benchmarks']
names_L3 = df_L3['Benchmarks']

# Figure Size
fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
# print(df_L3['simSeconds'], df['simSeconds'])
plt.plot(name, df['simSeconds'])
plt.plot(name,df_L3['simSeconds'])
# plt.plot(name,df_L3['simSeconds'] - df['simSeconds'])
plt.legend(["wo_L3", "w_L3"], loc ="lower right")
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
# print(df['l2.ReadExReq.missLatency::total'], df_L3['l2.overallAvgMissLatency::total'])
plt.bar(br1, df['l2.ReadExReq.missLatency::total'] + df['l2.ReadSharedReq.missLatency::total'], color ='r', width = barWidth,
        edgecolor ='grey', label ='wo_L3')
plt.bar(br2, df_L3['l2.ReadExReq.missLatency::total'] + df_L3['l2.ReadSharedReq.missLatency::total'], color ='g', width = barWidth,
        edgecolor ='grey', label ='w_L3')
 
# Adding Xticks
plt.xlabel('Benchmarks', fontweight ='bold', fontsize = 15)
plt.ylabel('Miss Latency', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(name))],
        name)
 
plt.legend()
plt.show()