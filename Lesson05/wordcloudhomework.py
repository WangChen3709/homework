from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from nltk.tokenize import word_tokenize

file='./Market_Basket_Optimisation.csv'

# 去掉停用词
def remove_stop_words(f):
	stop_words = ['a','the','that','this']
	for stop_word in stop_words:
		f = f.replace(stop_word, '')
	return f

# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

def main():
	# 加载数据
	dataset = pd.read_csv(file, header=None)
	print(dataset.shape)

	#数据处理
	transacations = []
	for i in range(dataset.shape[0]):
		temp = []
		for j in range(0,20):
			if str(dataset.values[i,j]) != 'nan':
				temp.append(str(dataset.values[i,j]))
		transacations.append(temp)

	#生成词云
	all_word = ' '.join('%s' %item for item in transacations)
	create_word_cloud(all_word)

if __name__ == '__main__':
	main()
