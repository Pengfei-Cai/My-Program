#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
import jieba
import wordcloud
import matplotlib
f = open("阿丽塔：战斗天使.csv",'rb')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc",\
                        width=1000,height=700,background_color="white",\
                        max_words=15
                        )
w.generate(txt)
w.to_file("grwordcloud.png")


