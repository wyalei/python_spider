import urllib
import urllib2
import re

class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')
    def replace(self, x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()

class BDTB:
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = 'see_lz=' + str(seeLZ)
        self.tool = Tool()
    def getPage(self, pageNum):
        try:
            url = self.baseURL + "?" + self.seeLZ + "&pn=" + str(pageNum)
            print url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"connect failed", e.reason
                return None

    def getTite(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        # print page
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getContent(self):
        page = self.getPage(1)
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        # for item in items:
        #     print item
        print self.tool.replace(items[1])

baseURL = "https://tieba.baidu.com/p/3138733512"
bdtb = BDTB(baseURL, 1)
# bdtb.getPage(1)
# title = bdtb.getTite()
# print title
# pageCount = bdtb.getPageNum()
# print pageCount
bdtb.getContent()
# print content
















