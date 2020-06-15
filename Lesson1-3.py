#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

data=pd.read_csv('car_complain.csv')

result=data.drop(columns='problem').join(data.problem.str.get_dummies(','))
result.to_csv('car_complain-al.csv',index=False)
result.drop(result.columns[1:7],1).to_csv('car_complain-a2.csv',index=False)
df2=pd.read_csv('car_complain-a2.csv')
df2['sum']=df2.iloc[:,1:].sum(axis=1)
df4=df2.drop(df2.columns[1:175],1)
#df4.to_csv('car_complain-a3.csv',index=False)
df5=pd.merge(result,df4,how='left')
#df5.to_csv('car_complain-a4.csv',index=False)

df=df5.groupby(['brand'])['sum'].agg(['sum']).sort_values('sum',ascending=False)
df1=df5.groupby(['car_model'])['sum'].agg(['sum']).sort_values('sum',ascending=False)
print(df,df1)


df3=df5.groupby(['brand','car_model'])['sum'].agg(['sum']).groupby(['brand']).mean().sort_values('sum',ascending=False)
print(df3)

# In[ ]:









