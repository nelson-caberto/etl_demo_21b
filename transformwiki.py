from lxml import html
import pymongo
import pickle

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.etlDEMO
collection = db.htmls

data = []
for page in collection.find():
    page_html = html.fromstring(page['html'])
    if (
        (page_html.xpath("//*[contains(text(),'programming language')]")) and
        (page_html.xpath("//*[contains(text(),'First')]")) and
        (page_html.xpath("//*[contains(text(),'appeared')]")) and
        (n := page_html.xpath('//*[@id="firstHeading"]/text()')) and 
        (d := page_html.xpath('//th[contains(text(),"First")]/following-sibling::td/text()'))
        ):
        name = n[0].split('(')[0].strip()
        try:
            date = int(d[0])
        except:
            continue
        data.append({'name':name,'date':date})

with open('data.pickle','wb') as filehandle:
    pickle.dump(data, filehandle)