
import os
import jieba
import pickle
import seaborn
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"simkai.ttf", size=12)
seaborn.set(font=font.get_name())


'''画柱状图'''
def drawBar(data, x_label, y_label, title, savepath='results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	ax = seaborn.barplot(x=x_label, y=y_label, palette="RdBu_r", data=data)
	ax.set_title(title)
	plt.show()
	fig = ax.get_figure()
	fig.savefig(os.path.join(savepath, title+'.png'))


# 词云
def DrawWordCloud(words, title, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	wc = WordCloud(font_path='simkai.ttf', background_color='white', max_words=2000, width=1920, height=1080, margin=5)
	wc.generate_from_frequencies(words)
	wc.to_file(os.path.join(savepath, title+'.png'))


# 统计词频
def statistics(texts, stopwords):
	words_dict = {}
	for text in texts:
		temp = jieba.cut(text)
		for t in temp:
			if t in stopwords:
				continue
			if t in words_dict.keys():
				words_dict[t] += 1
			else:
				words_dict[t] = 1
	return words_dict


if __name__ == '__main__':
	f = open('data.pkl', 'rb')
	data = pickle.load(f)
	stopwords = open('./stopwords.txt', 'r', encoding='utf-8').read().split('\n')[:-1]
	texts = [d[1][-1] for d in data.items()]
	words_dict = statistics(texts, stopwords)
	DrawWordCloud(words_dict, '商家描述词云', savepath='./results')
	texts = [d[0] for d in data.items()]
	words_dict = statistics(texts, stopwords)
	DrawWordCloud(words_dict, '商家名词云', savepath='./results')