#!usr/bin/pthon3
# -*- coding: UTF-8 -*-


'''
f= open('latex.log','r')
i= 0
chars = 0
for line in f.readlines():
    if not (len(line) == 1  and line[-1]=='\n') :
        i +=1
        chars += len(line)-1

avg = round(chars/i,0)
avg = int(avg)
print(avg)
'''
import matplotlib
import  numpy

# -*- coding:utf-8 -*-  # 解决python不兼容中文

# 加载requests库
import requests
# 加载正则表达式模块
import re


# 爬取网页内容模块
def get_html_text(url):  # 获取要访问的网址
    try:
        r = requests.get(url, timeout=30)  # 把爬取后的内容赋给r，等待时间对多30秒
        r.raise_for_status()  # 爬取网页时返回的状态码
        r.encoding = r.apparent_encoding  # 把从内容中分析的编码方式赋给从HTTP header中猜测的编码方式
        return r.text  # 返回爬取网页后的文本
    except RuntimeError:  # 一般超时错误
        return ""  # 函数结束返回


# 从爬取网页的文本内容中提取有价值信息
def parse_page(self, html):  # 接收
    try:
        find_price = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        find_title = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(find_price)):
            price = eval(find_price[i].split(':')[1])
            title = eval(find_title[i].split(':')[1])
            self.append([price, title])
    except RuntimeError:  # 一般超时错误
        print()


# 打印提取后的数据
def print_goods_list(data):
    headline = "{:4}\t{:8}\t{:16}"
    print(headline.format("序号", "价格", "商品名称"))
    count = 0
    for i in data:
        count = count + 1
        print(headline.format(count, i[0], i[1]))


# 主函数
def main():
    search_text = '鞋'  # 设置在淘宝搜索的内容
    depth = 3   # 设置爬取深度为3页
    start_url = 'https://ai.taobao.com/search?q=' + search_text
    information_list = []
    for i in range(depth):
        try:
            url = start_url + '$s=' + str(44*i)
            html = get_html_text(url)
            parse_page(information_list, html)
        except RuntimeError:  # 一般超时错误
            continue
    print_goods_list(information_list)


main()