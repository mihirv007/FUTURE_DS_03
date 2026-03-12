import pandas as pd
import numpy as np


#load the dataset
dataset=pd.read_csv('/Users/mihirverma/Marketing_Funnel_And_Conversion_Performance_Analysis/bank+marketing/bank-additional/bank-additional-full.csv',sep=";")

#data cleaning ,data preprocessing and data feature extraction

dataset=dataset.dropna()
#print((dataset=="unknown").sum())

'''

#unknown values

job             330  :  categorical
marital          80     :  categorical
education      1731     :  categorical
default        8597     :  categorical //yes and no drop this column because too many unknown values(21%) meaning the 1 out of 5 is unknown
housing         990     :  categorical //yes and no
loan            990     :  categorical //yes and no
'''

for feature in dataset.select_dtypes(include='object').columns:
    empty_count=dataset[feature].str.strip().eq("").sum()

dataset=dataset.drop(columns=['default'])

unknown_data_list=["job","marital","education","housing","loan"]


for unknown_value in unknown_data_list:
    dataset[unknown_value]=dataset[unknown_value].replace('unknown',np.nan)
    dataset[unknown_value]=dataset[unknown_value].fillna(dataset[unknown_value].mode()[0])

'''print((dataset=="unknown").sum())
print(dataset['duration'].value_counts().head(50))'''

#feature engineering

#lead to customer conversion
dataset['customer_conversion']=dataset['y'].map({'no':'Lead','yes':'Customer'})

#contacted
dataset['contacted']=1

#Campaign Intensity

dataset['campaign_group']=pd.cut(
    dataset['campaign'],
    bins=[0,1,3,5,10,100],
    labels=[
        '1 contacts',
        '2-3 contacts',
        '4-5 contacts',
        '5-10 contacts',
        '10+ contacts'
    ]
)

dataset['duration_group']=pd.cut(dataset['duration'],bins=[0,60,120,300,1000],labels=[
    'Under 1 min ',
    '1-2 min',
    '2-5 min',
    '5+ min'
])

#print(dataset['duration_group'].value_counts())

dataset.to_csv("Marketing_Funnel_And_Conversion_Performance_Analysis.csv",index=False)

#dataset Analysis
"""

#features in the dataset

back_additional_full:['age;"job";"marital";"education";"default";"housing";"loan";"contact";"month";"day_of_week";"duration";"campaign";"pdays";"previous";"poutcome";"emp.var.rate";"cons.price.idx";"cons.conf.idx";"euribor3m";"nr.employed";"y"']

rows_bank_additional_full=41188

features=21

#data cleaning :Removing any empty string and nan values from the dataset

feature: job ,empty_count: 0
feature: marital ,empty_count: 0
feature: education ,empty_count: 0
feature: default ,empty_count: 0
feature: housing ,empty_count: 0
feature: loan ,empty_count: 0
feature: contact ,empty_count: 0
feature: month ,empty_count: 0
feature: day_of_week ,empty_count: 0
feature: poutcome ,empty_count: 0
feature: y ,empty_count: 0
age               0
job               0
marital           0
education         0
default           0
housing           0
loan              0
contact           0
month             0
day_of_week       0
duration          0
campaign          0
pdays             0
previous          0
poutcome          0
emp.var.rate      0
cons.price.idx    0
cons.conf.idx     0
euribor3m         0
nr.employed       0
y                 0

"""
