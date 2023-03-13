# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:18:42 2023

@author: Roger
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# method 1 to read json data

json_file = open('loan_data_json.json')
data = json.load(json_file)

# method 2 to read json data

with open('loan_data_json.json') as json_file:
    data = json.load(json_file)


#tranform to dataframe
loanData = pd.DataFrame(data)

# getting the unique values for the purpose column
loanData['purpose'].unique()
 
#describe the data
# count,mean, std,min, 25%,50%,75%, max
loanData.describe()

# describe data for a specific column
loanData['int.rate'].describe()
 
# describe on fico scores
loanData['fico'].describe()

#debt to income ratio
loanData['dti'].describe()


# numpy
#using exp to get the annual income
income = np.exp( loanData['log.annual.inc'])
loanData['annualIncome'] = income

# working with arrays (1D array)
arr = np.array([1, 2, 3, 4])

# 0D array
arr= np.array(43)

# 2D array dimmensional

arr = np.array([[1,2,3], [4,5,6]])


# working with if statements

a = 40
b = 500

if  b > a:
    print('b is greater than a')
    
c = 1000

if b > a and b<c:
    print('b is greater than a but less than c')

# what if condition isnt met

c = 20

if b > a and b < c:
    print('b is greater than a but less than c')

else:
    print('no Conditions met')

# other scenario AND
c = 30

if b > a and b<c:
    print('b is greater than a but less than c')

elif b > a and b > c:
    print('b is greater than a and c')
    
else:
    print('no conditions met')

# other scenario OR

c = 30

if b > a or b<c:
    print('b is greater than a or less than c')
  
else:
    print('no conditions met')

# fico score

fico = 250

# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
    
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
    
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'

elif fico >= 660 and fico < 780:
    ficocat = 'Good'

elif fico >= 780:
    ficocat = 'Excellent'
    
else:
    ficocat = 'unknown'
    
print(ficocat)


# python for looooooops

fruits = ['apple', 'pear', 'banana', 'cherry']

for x in fruits:
    print(x)
    y = x + ' fruit'
    print(y)

for x in range(4):
    y = fruits[x] + ' for sale'
    print(y)

# applying for looooops to load data

# using first 10

length = len(loanData)
ficoCat = []

for x in range (length):
    fico = loanData['fico'][x]
    
    try:
        if fico >= 300 and fico < 400:
            ficocat = 'Very Poor'
            
        elif fico >= 400 and fico < 600:
            ficocat = 'Poor'
            
        elif fico >= 601 and fico < 660:
            ficocat = 'Fair'
        
        elif fico >= 660 and fico < 780:
            ficocat = 'Good'
        
        elif fico >= 780:
            ficocat = 'Excellent'
            
        else:
            ficocat = 'unknown'
    
    except:
        ficocat = 'unknown'
        
    ficoCat.append(ficocat)

# make fico cat a series

ficoCat = pd.Series(ficoCat)

loanData['fico.Catergory']= ficoCat

# dataframe.loc as conditional statements
#df.loc[dataframe[columnName] condition, newColumnName] = 'value if the condition is met'

# for interest rates, a new column is wanted.
# if rate is > 0.12 high, else low


loanData.loc[loanData['int.rate'] >0.12, 'int.rate.type' ] = 'High'

loanData.loc[loanData['int.rate'] <=0.12, 'int.rate.type' ] = 'Low'


# matplot lib stuff
# number of loans/rows by fico.category

catPlot = loanData.groupby(['fico.Catergory']).size()
catPlot.plot.bar(color = 'green', width = 0.1)
plt.show()


purposeCount = loanData.groupby(['purpose']).size()
purposeCount.plot.bar(color = 'red')
plt.show()


#scatter plots

ypoint = loanData['annualIncome']
xpoint = loanData['dti']

plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#writing to csv

loanData.to_csv('loan_cleaned.csv', index = True)







