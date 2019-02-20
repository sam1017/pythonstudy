import urllib
import urllib2
import re

page = 1
url = 'https://www.qiushibaike.com/text/'
url_page = 'https://www.qiushibaike.com/text/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    filename = 'pachong.txt'
    with open(filename,"w") as file_object:
        file_object.write(content.encode())
    #print(content)
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    print("item.size = " + str(len(items)))
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            filename = 'laugh.txt'
            with open(filename,"w") as file_object:
                file_object.write(item[0])
                file_object.write(item[1])
                file_object.write(item[2])
                file_object.write(item[4])
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason