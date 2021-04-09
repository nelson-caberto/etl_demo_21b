from lxml import html
import requests
import pymongo
import time

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.etlDEMO
collection = db.htmls

baseurl = "https://en.wikipedia.org"
url = baseurl+"/wiki/List_of_programming_languages"

def getPage(url):
    print(url)
    if (someHTML := collection.find_one({"url":url})):
        page = someHTML['html']
        print('retrieved')
    else:
        page = requests.get(url)
        collection.insert_one({"url":url,"html":page.content})
        print('downloaded')
        time.sleep(1)
    return page

page_html = html.fromstring(getPage(url))
hrefs = page_html.xpath('//a/@href')

for href in hrefs:
    try:
        page = getPage(baseurl+href)
    except:
        continue
    
