from bs4 import BeautifulSoup
import requests
import json
url = 'https://simpleflying.com/category/aviation-news/'
response = requests.get(url,timeout=5)
content = BeautifulSoup(response.content,"html.parser")
news = []
for heading in content.findAll('h2',attrs={"class" : "entry-title"}) :
	headingObject = {
	 "url" : heading.find('a').encode('utf-8'),
	 "heading" : heading.text.encode('utf-8')
	}
	print(headingObject)
	news.append(headingObject)

with open('newsData.json','w') as outfile:
	json.dump(news,outfile)

# print(content)
# print(headings)