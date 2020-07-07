
import time
import pickle
import requests
from urllib.parse import quote


HEADERS = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
URL = 'https://ai.taobao.com/search/getItem.htm'
PARMAS = {'key': None}


'''主函数'''
def main(keyword, num_pages=20):
	data = {}
	PARMAS['key'] = quote(keyword)
	for page in range(0, num_pages):
		print('[INFO]: Starting get the data of page.<%d>...' % page)
		PARMAS['page'] = str(page)
		res = requests.get(URL, headers=HEADERS, params=PARMAS)
		res_json = res.json()
		print(res_json)
		items = res_json['result']['auction']
		for item in items:
			description = item.get('description')
			price = item.get('price')
			real_price = item.get('realPrice')
			sale_count = item.get('count')
			item_id = item.get('itemId')
			item_location = item.get('itemLocation')
			nick = item.get('nick')
			data[nick] = [price, real_price, sale_count, item_id, item_location, description]
		time.sleep(2)
	with open('data.pkl', 'wb') as f:
		pickle.dump(data, f)


if __name__ == '__main__':
	keyword = input('请输入关键词:')
	print()
	num_pages = int(input('请输入爬取的页数:'))
	print()
	main(keyword, num_pages)
