#coding=utf-8
'''
    author:huyang
    date:2012-7-10
    blog:http://www.the5fire.net
'''

from optparse import OptionParser
from fetcher import Fetch
import sys
reload(sys) 
sys.setdefaultencoding("utf-8") 

def main(url, data, obj):
    '''
    主函数，在该函数中，完成以下功能：
        1、获取给定url页面中的所有链接
        2、判断链接的url，并添加参数
        3、将转换完成的url存入文件爱呢。
    '''
    print '====BEGIN======'
    try: 
        fetcher = Fetch(url = url, from_encoding = 'GBK')
        content = fetcher.get_content().renderContents()
        for link in fetcher.get_all_link():
            params = data.split(',')
            #处理如果存在参数
            for param in params:
                if param in link:
                   params.remove(param)
            newlink = '%s?%s' % (link,'&'.join(params))
            #链接替换
            content = content.replace('href="%s"' % link, 'href="%s"' % newlink)
        obj_file = open(obj, 'w')
        obj_file.write(content)
        obj_file.close()
        print '====OVER======='
    except Exception,e:
        print 'an exception occur:%s' % str(e)

if __name__ == '__main__':
    #定义命令行参数
    usage = "usage: %prog  -u http://www.sohu.com -d 'a=1,b=2,c=3' -o /tmp/index.html"

    parser = OptionParser(usage=usage)

    parser.add_option("-u", "--url", dest="url",
                        help="the webpage url you want to fetch.eg:-u http://www.baidu.com")
    
    parser.add_option("-d", "--data", dest="data", 
                        help="the params you want to add to the link in the page you give")
    
    parser.add_option("-o", "--obj", dest="obj", default="/tmp/default.html",
                        help="local file to store all links you got")

    (options, args) = parser.parse_args()
    
    #url为必填项
    if not options.url or not options.data:
        parser.print_help()
    else:
        main(url = options.url, data = options.data, obj = options.obj)
