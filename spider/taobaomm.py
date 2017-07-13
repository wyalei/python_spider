import urllib
import urllib2
import re

class Spider:
    def __init__(self):
        self.siteURL = "http://mm.taobao.com/json/request_top_list.htm"

    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode("gbk")

    def getContent(self, pageIndex):
        page = self.getPage(pageIndex)
        # print page
        pattern = re.compile('<div class="list-item".*?<div class="pic-word".*?class="lady-avater">' +
                             '<img src="(.*?)".*?<a class="lady-name".*?>(.*?)</a>.*?<em><strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            print item[0], item[1], item[2], item[3]

spider = Spider()
spider.getContent(1)




























