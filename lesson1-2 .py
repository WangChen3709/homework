#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas
from pandas import DataFrame
data={'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df1=DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])

df2=df1.describe().loc[['mean','min','std','max']]
df3=df1.var(axis=0)
print(df2)
print(df3)

df1['sum']=df1.sum(axis=1)
df1['rank']=df1['sum'].rank(ascending=False)
print(df1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




