import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('http://www.baidu.com')
#
# for item in cookie:
#     print 'name: ' + item.name
#     print 'vale: ' + item.value

# request = urllib2.Request("http://www.baidu.com")
# # response = urllib2.urlopen("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print(response.read())

