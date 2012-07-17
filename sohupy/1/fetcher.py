#coding=utf-8
'''
    author:huyang
    blog:http://www.the5fire.net
    date:2012-07-10
    function:
        根据获取某一url内的所有链接
        获取某url的页面内容，标题
'''

from BeautifulSoup import BeautifulSoup as bs
import urllib
import urllib2
import re
import socket

class Fetch(object):

    def __init__(self, url, from_encoding = 'utf-8'):
        self.html = urllib2.urlopen(url).read()
        self.html = self.html.decode('gb18030','ignore')
        re_domain = '(http\w{0,1}://(\w+?\.?)+?)[\/|\?]'
        try:
            self.domain = re.search(re_domain, url + '/').group(1)
        except Exception,e:
            print 'in self.domain:%s, at url:%s' % (str(e),url)
        self.soup = bs(self.html, fromEncoding = from_encoding)

    def get_content(self):
        return self.soup

    def get_title(self):
        if self.soup:
            return self.soup.title
        else:
            return None

    def get_all_link(self):
        if self.soup:
            for a_dom in self.soup.findAll('a'):
                href = a_dom.get('href')
                if not href:
                    continue
                #过滤没有意义的链接
                if '#' in href or 'javascript' in href:
                    continue
                yield href
        else:
            return


if __name__ == '__main__':
    fetch = Fetch('http://www.sohu.com/', from_encoding="GBK")
    fetch.get_all_link()
    #for link in fetch.get_all_link():
    #    print link
