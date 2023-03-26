# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 08:52:56 2023

@author: Roger
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading xlsx files aka excel

data = pd.read_excel('articles.xlsx')

#summary of the data
data.describe()

#summary of the columns
data.info()

#group by - counting # of articles per source
# data.groupby(['column_to_group'])['column_to_count'].count() or .sum()

data.groupby(['source_id'])['source_id'].count()


# of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()


# dropping a column
data = data.drop('engagement_comment_plugin_count' , axis=1)


#functions in python

def thisFunction():
    print('this is my first function!')
    
thisFunction()

#this is a function with variables

def aboutMe(name, surname, location):
    print('this is ' + name+ ' My surname is '+surname+ ' i am from '+ location)
    return name, surname, location

a = aboutMe('Rog', 'bencomo', 'here')

# using for loops for functions

def favFood(someArray):
    for x in someArray:
        print('top food is ' + x)
    
    
    
fastFood = ['salad', 'pizza', 'pie']

favFood(fastFood)


#creating a keyword flag

keyword = 'crash'

#lets create a for loop to isolate each title

# length = len(data)
# keyword_flag = []

# for x in range(length):
#     heading = data['title'][x]
    
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
        
#     keyword_flag.append(flag)
    
# make into a function

def keywordFlag(keyword):
    
    length = len(data)
    keyword_flag = []
    
    for x in range(length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
                
        except:
            flag = 0
        keyword_flag.append(flag) 

    return keyword_flag


keyword_flag = keywordFlag('murder')

#creating new column in data

data['keyword_Flag'] = pd.Series(keyword_flag)




#SentimentIntensityAnalyzer

sentiment = SentimentIntensityAnalyzer()
text = data['title'][16]

sent = sentiment.polarity_scores(text)


neg = sent['neg']
pos = sent['pos']
neu = sent['neu']


#adding a for loop to extract sentiment per title

title_neg_sent = []
title_pos_sent = []
title_neu_sent = []

length = len(data)

for x in range(length):
    text = data['title'][x]
    sentiment = SentimentIntensityAnalyzer()
    
    try:
        sent = sentiment.polarity_scores(text)
        
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
        
    except:
        neg = 0
        pos = 0
        neu = 0
        
    title_neg_sent.append(neg)
    title_pos_sent.append(pos)
    title_neu_sent.append(neu)

title_neg_sent = pd.Series(title_neg_sent)
title_pos_sent = pd.Series(title_pos_sent)
title_neu_sent = pd.Series(title_neu_sent)

data['title_neg_sent'] = title_neg_sent
data['title_pos_sent'] =title_pos_sent
data['title_neu_sent'] = title_neu_sent


#writing the data

data.to_excel('blogme_clean.xlsx', sheet_name= 'blogmedata', index=(False))




    