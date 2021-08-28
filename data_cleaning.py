#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:22:13 2021

@author: anupsukumaran
"""

import pandas as pd
import numpy as np

df = pd.read_csv("glassdoor_jobs.csv")
df = df[df['Salary Estimate'] != '-1']

#salary parsing cleaning
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
removeSigns = salary.apply(lambda x: x.replace('K','').replace('$',''))


min_hr = removeSigns.apply(lambda x: x.replace('per hour','').replace('employer provided salary:',''))
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#company name

#ss = np.where(df['Rating'] < 0, 1, 0)#1 if df.Rating < 0 else 1
#sss = df['Company Name'].str[:-3]
#ssss = sss.dtype
#print(f'ssss = {ssss}')

#fff = df.dtypes
#print(f'dataTypes = {fff}')
#xxx = df.apply(lambda x: np.where(x['Rating'] <0, x['Company Name'], x['Company Name'][:-3]), axis = 1)
#yyy = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)
#zzz = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)
# def func(x):
#     #return np.where(df['Rating'] < 0, df['Company Name'], df['Company Name'][:-3])
#     if x['Rating'] < 0:
#         return x['Company Name']
#     else:
#         return x['Company Name'].str[:-3]
    
# hhh = func()
                  
# df['company_txt'] = df.apply(func(), axis = 1)
#Company name text only
#df['company_txt'] = func()



#df['company txt'] = df.apply(lambda x: str(x['Company Name']) if x['Rating'] <0 else str(x['Company Name'])[:-3], axis = 1)


# location
ccc = df['Location'].apply(lambda x: str(x).split(","))

df['job_state'] = ccc.str[1]
#df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


#age
df['age'] = df.apply(lambda x: x if x.FOund)

