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


#tranform to dataframe
loanData = pd.DataFrame(data)

 
#describe the data
# count,mean, std,min, 25%,50%,75%, max
loanData.describe()


# numpy
#using exp to get the annual income
income = np.exp( loanData['log.annual.inc'])
loanData['annualIncome'] = income



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


# for interest rates, a new column is wanted.
# if rate is > 0.12 high, else low


loanData.loc[loanData['int.rate'] >0.12, 'int.rate.type' ] = 'High'

loanData.loc[loanData['int.rate'] <=0.12, 'int.rate.type' ] = 'Low'



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







