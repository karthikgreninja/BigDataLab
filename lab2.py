# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:27:18 2020

@author: Karthikeyan S
"""
import matplotlib.pyplot as plt
import stemgraphic
import seaborn as sns
import numpy as np
import pandas as pd
from random import seed
from random import gauss
from plotly import graph_objects as go
import math

#Q1
print("\nQuestion1")
x = [7, 9, 27, 28, 55, 45, 34, 65, 54, 67, 34, 23, 24, 66, 53, 45, 44, 88, 22, 33, 55, 35, 33, 37, 47, 41, 31, 30, 29, 12]
print("Bins = 4")
plt.hist(x, bins = 4)
plt.show()

print("Bins = 6")
plt.hist(x, bins = 6)
plt.show()

print("Bins = 8")
plt.hist(x, bins = 8)
plt.show()

print("Right skewed")

#Q2
print("\nQuestion2")
x = [22, 21, 24, 19, 27, 28, 24, 25, 29, 28, 26, 31, 28, 27, 22, 39, 20, 10, 26, 24, 27, 28, 26, 28, 18, 32, 29, 25, 31, 27]
#stemgraphic.stem_graphic(x, scale = 5) 

stems = [2,
         3,3,
         4,4,4,4,4,4,4,
         5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
         6,6,6,
         7]

plt.ylabel('Data')   # for label at y-axis 
plt.xlabel('stems')   # for label at x-axis 
plt.stem(stems, x , use_line_collection = True)   # required plot
plt.show()

#Q3
print("\nQuestion3")
df = pd.read_excel('Q3_Lab2.xlsx')
ax = df['Beverages'].plot(kind='density')
# Access the child artists and calculate the mean of the resulting array
mean_val = np.mean(ax.get_children()[0]._x)
# Annotate points
ax.annotate('mean', xy=(mean_val, 0.008), xytext=(mean_val+10, 0.010),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
# vertical dotted line originating at mean value
plt.axvline(mean_val, linestyle='dashed', linewidth=2)
plt.show()
median_val = np.median(ax.get_children()[0]._x)
# Annotate points
ax.annotate('median', xy=(median_val, 0.008), xytext=(median_val+10, 0.010),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
# vertical dotted line originating at median value
plt.axvline(median_val, linestyle='dashed', linewidth=2)
plt.show()
mode_val = np.median(ax.get_children()[0]._x)
# Annotate points
ax.annotate('mode', xy=(mode_val, 0.008), xytext=(mode_val+10, 0.010),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
# vertical dotted line originating at mode value
plt.axvline(mode_val, linestyle='dashed', linewidth=2)
plt.show()

sns.rugplot(df['Beverages'])
plt.show()

#Q4
print("\nQuestion4")
x = [3.6 , 6.7 , 9.8 , 11.2 , 14.7] #Fuel
y = [0.45 , 0.91 , 1.36 , 1.81 , 2.27] #Mass
plt.scatter(x,y,marker = 'o')
plt.show()

print(np.corrcoef(x, y))
print("Positive correlation")

#Q5
print("\nQuestion5")
sns.set(style="whitegrid")
df = pd.read_excel('Q5_Lab2.xlsx')
ax = sns.boxplot(x=df["Chairs"])

ax = sns.swarmplot(x=df["Chairs"])
plt.show()

#Q6
print("\nQuestion6")

# seed random number generator
seed(1)
# generate some Gaussian values
sample_gaussian = np.random.normal(size=1000)

fig , ax = plt.subplots()

ax.violinplot(sample_gaussian)

sample_lognormal = np.random.lognormal(size=1000)

fig , ax = plt.subplots()

ax.violinplot(sample_lognormal)  
plt.show()  

#Q7
print("\nQuestion7")
df = pd.read_csv("Q7_Lab2.csv")
labels=np.array(['Q1', 'Q2', 'Q3', 'Q4'])
stats=df.loc[1,labels].values
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
# close the plot
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title([df.loc[1,"Shop"]])
ax.grid(True)
plt.show()

"""
#Needs to be run in google colab
#Q8
print("\nQuestion8")
import plotly.express as px
data = dict(
    time=[50, 110, 250, 180, 70], 
    step=["Requirement Elicitation", "Requirement Analysis", "Software Development", "Debugging & Testing", "Others"])
fig = px.funnel(data, x='time', y='step')
fig.show()
"""

#Q9
print("\nQuestion9")
Temp = [98 , 87 , 90 , 85 , 95 , 75]
Cust = [15 , 12 , 10 , 10 , 16 , 7]
print(np.corrcoef(Temp, Cust))
print("Positive correlation")

#Q10
print("\nQuestion10")
np.random.seed(1)
xData = np.random.random_integers(25, 50, 100)
yData = np.random.random_integers(10, 50, 100)
yData = np.arange(0, 100, 1)
plt.hexbin(xData, yData, gridsize=50)
plt.title('Hexagonal binning using Python Matplotlib')
plt.xlabel('XData')
plt.ylabel('YData')
plt.show()

#Q11
print("\nQuestion11")
x = np.linspace(-3, 3, 100, endpoint=True)
y = np.linspace(-3, 3, 100, endpoint=True)
X,Y = np.meshgrid(x,y)
Z1 = X**2 + Y**2
for i in range(100):
    for j in range(100):        
            Z[i][j] = math.sqrt(Z1[i][j])

fig, ax = plt.subplots(figsize=(6,6))

ax.contour(X,Y,Z)
plt.show()

    



















