#coding:utf-8

import urllib2

def get_content_by_proxy(url, proxy=None):
    if proxy:
        opener = urllib2.build_opener(urllib2.ProxyHandler({'http':proxy}), urllib2.HTTPHandler(debuglevel=1))
        urllib2.install_opener(opener)

    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5", \
					"Referer": 'http://www.baidu.com'}

    req = urllib2.Request(url, headers=i_headers)
    content = urllib2.urlopen(req).read()
    return content
    


url = 'http://www.facebook.com/'
url = 'http://www.youtube.com/'
#url = 'http://www.baidu.com/'
proxy = 'http://127.0.0.1:1998'
proxy = 'http://109.87.114.119:3128'
proxy = 'http://206.17.82.114:80'
print get_content_by_proxy(url, proxy)


