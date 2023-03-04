# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:41:22 2023

@author: Roger
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') format of read_csv

data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv', sep=';')

#summary of the data

data.info()


# working with calculations



# Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
sellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#cost Per Transaction calculation

# costPerTransaction = costPerItem * NumberofItemsPurchased
# variable = dataframe['columnName']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding New column to Dataframe

data['CostPerTransaction'] = CostPerTransaction

# sales per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# profit = sales - cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# mark up = (sales- cost)/cost

data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']


# Rounding Markup

roundmarkup = round(data['Markup'],2)

data['Markup'] =roundmarkup

#combining data fields

my_name = 'Dee' + 'Naidoo'


#checking columns data type

print(data['Day'].dtype)

#change columns type

day = data['Day'].astype(str)


my_date = day + '-' + data['Month'] +'-' + data['Year'].astype(str)


data['Date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] # views the row with index = 0

data.iloc[0:3] #first 3 rows

data.iloc[-5:] # last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] # brings in all rows on column 3 (0,1,2)

data.iloc[4,2] #brings 5th row 3rd column

# using split to split the client keywords field
# new_var = column.str.split('the seperator', expand = True)


split_col = data['ClientKeywords'].str.split(',' , expand =True)

#creating new columns for the split columns in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] =split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function


data['ClientAge']= data['ClientAge'].str.replace('[','')
data['LengthOfContract']= data['LengthOfContract'].str.replace(']','')

#using the lower function to  change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()


# how to merge files
# Bringing in a new data set

seasons = pd.read_csv('value_inc_seasons.csv',sep = ';')

# merging files : merge_dataframe = pd.merge(old_data, new_data, on = 'key(commonfield)')

data = pd.merge(data, seasons, on ='Month' )


#dropping columns
# dataframe = dataframe.drop('columnname', axis = 1) axis 1= column, axis 0 = row

data = data.drop('ClientKeywords', axis =1)

data = data.drop('Day', axis =1)

#multiple columns

data = data.drop(['Year', 'Month'], axis = 1)

#export into csv

data.to_csv('ValueInc_Cleaned.csv', index = False)






