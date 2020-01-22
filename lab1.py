# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:47:54 2020

@author: Karthikeyan S
"""
import collections
import random
import sys
from random import seed
from random import randint
import math
import statistics
import matplotlib.pyplot as plt;plt.rcdefaults()
import numpy as np
import pandas

def CountFrequency(arr): 
    return collections.Counter(arr)

#Q1
print("\nQuestion1")
excel_data_df = pandas.read_excel('Q1.xlsx')
print(excel_data_df)
count = excel_data_df['Pokemon'].value_counts() 
print(count)
    
#Q2
Roll = []
Marks = []

for i in range (18):
    if ( i % 2 == 0):
        Marks.append(25+((i+8)%10))
    else:
        Marks.append(25+((i+7)%10))
    Roll.append(i)
print("\nQuestion2")
print("Mean of marks : ",statistics.mean(Marks))
print("Median of marks : ",statistics.median(Marks))

#Q3
Y = []
X = []
for _ in range (20):
    x = randint(5, sys.maxsize)
    y = 2*x + 3
    X.append(x)
    Y.append(y)
print("\nQuestion3")
print("Standard deviation of Y is : ",statistics.stdev(Y))
    
#Q4
dataHeight = [167.65, 167, 172, 175, 165, 167, 168, 167, 167.3, 170, 167.5, 170, 167, 169,172]

meanVal = statistics.mean(dataHeight)
medianVal = statistics.median(dataHeight)
modeVal = statistics.mode(dataHeight)
stdVal = statistics.stdev(dataHeight)
skewVal = (meanVal - modeVal)/stdVal

print("\nQuestion4")
print("Mean is : ",meanVal)
print("Median is : ",medianVal)
print("Mode is : ",modeVal)
print("Standard Deviation is : ",stdVal)
print("Skew is : ",skewVal)
if(meanVal > medianVal and medianVal > modeVal):
    print("Positive skew")
elif(meanVal < medianVal and medianVal < modeVal):
    print("Negative skew")

#Q5
print("\nQuestion5")
grades = ('S' , 'B' , 'C' , 'D')
freq = [31 , 29 , 25 , 15]

plt.bar(grades, freq, align='center', alpha=0.5)
plt.xticks(grades)
plt.ylabel('Frequency')
plt.title('Grades in Big Data course')
plt.show()

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
patches, texts = plt.pie(freq, colors=colors, shadow=True, startangle=90)
plt.legend(patches, grades, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()

#Q6
print("\nQuestion6")
activities = ('Studying' , 'Sleeping' , 'Playing' , 'Hobby Activities' , 'Friends and family')
freq1 = [33 , 30 , 18 , 5 , 14]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral' , 'red']
patches, texts = plt.pie(freq1, colors=colors, shadow=True, startangle=90)
plt.legend(patches, activities, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()

#Q7
print("\nQuestion7")
grades = []
excel_data_df = pandas.read_excel('DataSetMarks.xlsx')
print(excel_data_df)
total = excel_data_df['Mid sem(30)'] + excel_data_df['End sem(50)'] + excel_data_df['Assignments(20)']
print(total)
total_numpy = total.to_numpy()
for i in range (20):
    if(total_numpy[i] >= 90):
        grades.append('S')
    elif (total_numpy[i] >= 80 and total_numpy[i] < 90):
        grades.append('A')
    elif (total_numpy[i] >= 70 and total_numpy[i] < 80):
        grades.append('B')
    elif (total_numpy[i] >= 60 and total_numpy[i] < 70):
        grades.append('C')
    elif (total_numpy[i] >= 50 and total_numpy[i] < 60):
        grades.append('D')
    elif (total_numpy[i] >= (statistics.mean(total))/2 and total_numpy[i] < 50):
        grades.append('E')

print(grades)
freq = CountFrequency(grades) 
print("Frequency table")
for key , value in freq.items():
    print (key ,":", value)

#Q8
print("\nQuestion8")
grades = []
pass_marks = []
excel_data_df = pandas.read_excel('DataSetMarks.xlsx')
print(excel_data_df)
total = excel_data_df['Mid sem(30)'] + excel_data_df['End sem(50)'] + excel_data_df['Assignments(20)']
print(total)
total_numpy = total.to_numpy()
PassMark = (statistics.mean(total))/2
if(total_numpy[i] >= PassMark):
    pass_marks.append(total_numpy[i])
pass_average = statistics.mean(pass_marks)
SCutoff = max(total) - 0.1*(max(total) - pass_average)
Y = SCutoff - pass_average
ACutoff = pass_average + Y*5/8
BCutoff = pass_average + Y*2/8
X = pass_average - min(pass_marks)
CCutoff = pass_average - X*2/8
DCutoff = pass_average - X*5/8
ECutoff = min(pass_marks)
for i in range (20):
    if(total_numpy[i] >= SCutoff):
        grades.append('S')
    elif (total_numpy[i] >= ACutoff and total_numpy[i] < SCutoff):
        grades.append('A')
    elif (total_numpy[i] >= BCutoff and total_numpy[i] < ACutoff):
        grades.append('B')
    elif (total_numpy[i] >= CCutoff and total_numpy[i] < BCutoff):
        grades.append('C')
    elif (total_numpy[i] >= DCutoff and total_numpy[i] < CCutoff):
        grades.append('D')
    elif (total_numpy[i] >= ECutoff and total_numpy[i] < DCutoff):
        grades.append('E')

print(grades)
freq = CountFrequency(grades) 
print("Frequency table")
for key , value in freq.items():
    print (key ,":", value)
    
#Q9
print("\nQuestion9")
x = [79 , 71 , 89 , 57 , 76 , 64 , 82 , 82 , 67 , 80 , 81 , 65 , 73 , 79 , 79 , 60 , 58 , 83 , 74 , 68 , 78 , 80 , 78 , 81 , 76 , 65 , 70 , 76 , 58 , 82 , 59 , 73 , 72 , 79 , 87 , 63 , 74 , 90 , 69 , 70 , 83 , 76 , 61 , 66 , 71 , 60 , 57 , 81 , 57 , 65 , 81 , 78 , 77 , 81 , 81 , 63 , 71 , 66 , 56 , 62 , 75 , 64 , 74 , 74 , 70 , 71 , 56 , 69 , 63 , 72 , 81 , 54 , 72 , 91 , 92]
plt.hist(x, bins = 4)
plt.show()
print("Left skewed")















