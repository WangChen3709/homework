import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

dataset=pd.read_csv('./MarketBasket/Market_Basket_Optimisation.csv',header=None)
print(dataset.shape)

#数据整理
temp_list=[]
for i in range(0,dataset.shape[0]):
	temp_str=''
	for j in range(0,20):
		if str(dataset.values[i,j])!='nan':
			temp_str+=str(dataset.values[i,j])+'|'
	temp_list.append(temp_str)
dataset_new=pd.DataFrame(data=temp_list)
dataset_new.columns=['MarketBasket']
#dataset_new.to_csv('temp_data.csv',index=True)

#对数据进行one-hot编码
dataset_new_hot_encoded = dataset_new.drop('MarketBasket',1).join(dataset_new.MarketBasket.str.get_dummies('|'))
dataset_new_hot_encoded=dataset_new_hot_encoded.dropna(axis=1)
#dataset_new_hot_encoded.to_csv('temp_data.csv',index=True)
#print(dataset_new_hot_encoded.shape)

# 挖掘频繁项集
itemsets = apriori(dataset_new_hot_encoded,use_colnames=True, min_support=0.05)
itemsets = itemsets.sort_values(by="support" , ascending=False) 
print('-'*20, '频繁项集', '-'*20)
print(itemsets)

# 根据频繁项集计算关联规则
rules =  association_rules(itemsets, metric='lift', min_threshold=1)
rules = rules.sort_values(by="lift" , ascending=False) 
print('-'*20, '关联规则', '-'*20)
print(rules)