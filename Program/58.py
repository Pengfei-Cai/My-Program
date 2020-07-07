import requests
from pyquery import PyQuery as pq
import time
import re

URL = 'https://bj.58.com/chaoyang/chuzu/pn{page}/'    # 58同城租房信息的链接
t58_dict = {'龒':'0','龤':'1','驋':'2','閏':'3','餼':'4','麣':'5','鑶':'6','龥':'7','齤':'8','鸺':'9'}   # 58同城所用的加密字典

HEADERS = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
           }    # 伪装头，防止网页查出是爬虫

def get_html(url):
    """
    下载当前url的网页源码
    :param url: 当前网页链接
    :return: 网页源码
    当当前未获得源码时，暂停2s，再去请求下载
    """
    try:
        response = requests.get(url, headers = HEADERS)   # 请求url
        if response.status_code == 200:     # 请求状态码为200时表示请求成功，请求成功时，返回html
            return response.text
        else:     # 当请求失败时，暂停2s再次请求
            time.sleep(2)   # 休眠2s
            get_html(url)   # 再次请求
    except Exception as e:  # 当程序执行发生异常时，抛出异常
        print('执行下载时发生异常:', e)

def parse_page(html):
    """
    对网页进行解析，获取我们需要的信息
    :param html: 网页源码
    :yield 单个房间的信息
    """
    doc = pq(html)    # 初始化
    lis = doc('ul.house-list li')   # 选择所有租房信息的节点
    for li in lis.items():    # 遍历所有租房节点
        try:
            house = {}        # 用于存放单个租房信息的字典
            house['title'] = convert(li('div.des h2').text())   # 获取标题
            house['pic_url'] = li('div.img-list a img').attr('src')   # 获取图片url
            house['house_type'] = convert(li('div.des p.room').text())  # 获取户型，并将其使用一开始定义的加密字体进行转换
            house['price'] = convert(li('div.money').text())     # 获取价格，并将其使用一开始定义的加密字体进行转换
            if house['title'] == None or house['pic_url'] == None:  # 对于没有标题或者没有图片的信息不输出
                continue
            yield house
        except Exception as e:    # 获取相关信息抛出异常时直接跳过
            continue
       
def convert(s):
    """
    对数字文本进行相应的转换，转换为真实文本
    :param s: 待转换的文本
    :return: 转换后的文本
    """
    for key, value in t58_dict.items():   # 根据字符映射表进行替换
        if key in s:                      # 若当前字体中有加密字体则对其进行替换
            s = re.sub(key, value, s).replace(';', '')
    return s                              # 返回解密后的字体文件

def main():
    """
    爬虫入口
    """
    for page in range(1, 5):    # 抓取前5页
        url = URL.format(page = 1)   # 构造每一页的url
        response = get_html(url)     # 获取每一页的html文本
        for result in parse_page(response):   # 获取相关信息，并对其进行打印输出
            print('出租房标题: ', result['title'])
            print('出租房图片链接', result['pic_url'])
            print('出租房户型: ', result['house_type'])
            print('出租房价格: ', result['price'] + '\n')
        time.sleep(2)                # 为防止封IP，间隔2s抓取一个网页

if __name__ == '__main__':
    main()