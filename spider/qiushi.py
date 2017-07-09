import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# url = "https://www.qiushibaike.com/hot"
# url = "https://www.baidu.com"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers ={'User-Agent' : user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # print response.read()
    content = response.read().decode('utf-8')
    # print content
    # pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
    #                      'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
    # patternValue = '<div.*?author clearfix">.*?<a.*?<h2>(.*?)</h2>.*?<div.*?' + 'content">.*?<span>(.*?)</span>.*?</div>.*?<div class="stats.*?class="number">(.*?)</i>';
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<h2>(.*?)</h2>.*?<div.*?' +
                         'content">.*?<span>(.*?)</span>.*?</div>.*?<div class="stats.*?class="number">(.*?)</i>', re.S)
    # pattern = re.compile(patternValue, re.S)
    items = re.findall(pattern, content)
    for item in items:
        print
        print item[0]
        print item[1]
        print item[2]
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason