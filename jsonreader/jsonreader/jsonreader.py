#coding:utf-8
__author__ = 'the5fire'
__blog__ = 'http://www.the5fire.net'
__desc__ = """
    工作时需要处理ajax的json数据，浏览器无法直接打开，就顺手写了这工具，可发送get和post请求。
    有问题可到博客交流。
"""
import wx
import json
import urllib
import urllib2
import functools
import operator
import codecs

HEAD_START = 0.1 #Seconds
SECRET_LENGTH = 100
HOST_DOMAIN = 'http://m.weather.com.cn/data/'
SAMPLE_LIST = [
'101010100.html',
]
SAMPLE_LIST = map(functools.partial(operator.add, HOST_DOMAIN), SAMPLE_LIST)

class MainFrame(wx.Frame):
    def __init__(self, parent=None, title="JsonReader", size=(800, 900), pos=wx.DefaultPosition, id=-1):
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.statusBar = self.CreateStatusBar()
        self.init_get_panel()

    def init_get_panel(self):
        bkg = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        input_box = wx.BoxSizer()
        self.urlinput = urlinput = wx.TextCtrl(bkg, -1, u'点击下面url或者手动输入', size=(400, 25))
        input_box.Add(urlinput, proportion=1, flag=wx.ALL, border=10)

        get_btn = wx.Button(bkg, label="Get", size=(80, 25))
        get_btn.Bind(wx.EVT_BUTTON, self.get_handler)
        input_box.Add(get_btn, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        post_btn = wx.Button(bkg, label="Post", size=(80, 25))
        post_btn.Bind(wx.EVT_BUTTON, self.post_handler)
        input_box.Add(post_btn, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(input_box, proportion=0, flag=wx.EXPAND)

        param_box = wx.BoxSizer()
        self.url_list = url_list = wx.ListBox(bkg, -1, (80, 50), (500, 200), SAMPLE_LIST)
        self.Bind(wx.EVT_LISTBOX, self.click_list_evt, url_list)
        self.post_data = post_data = wx.TextCtrl(bkg, -1, '{\n\r}', size=(200, 200), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        param_box.Add(url_list, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        param_box.Add(post_data, proportion=1, flag=wx.ALL | wx.RIGHT, border=10)
        vbox.Add(param_box, proportion=0, flag=wx.EXPAND)

        result_box = wx.BoxSizer()
        self.tree = wx.TreeCtrl(bkg, size=(400, 400))
        result_box.Add(self.tree, proportion=1, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)

        vbox.Add(result_box, proportion=0, flag=wx.EXPAND)
        bkg.SetSizer(vbox)


    def click_list_evt(self, event):
        self.urlinput.SetValue(event.GetString())

    def get_handler(self, event):
        url = self.urlinput.GetValue()
        #添加查询url记录到下面的列表中
        if url not in self.url_list.Items:
            self.url_list.Append(url)
        try:
            self.statusBar.SetStatusText('begin fetch data from url...')
            #处理url中的中文
            url = url.encode('utf-8')
            content = urllib.urlopen(urllib.url2pathname(url)).read()
            self._parse_data(content)
        except Exception, e:
            self.statusBar.SetStatusText(str(e))
            return

    def post_handler(self, event):
        url = self.urlinput.GetValue()
        post_data = self.post_data.GetValue()
        post_data = post_data.replace('\'', '"')
        content = json.loads(post_data)
        headers =dict(Referer = 'http://m.sohu.com')
        try:
            req = urllib2.Request(
                url = url,
                data = urllib.urlencode(content),
                headers = headers,
            )
            content = urllib2.urlopen(req).read()
            self._parse_data(content)
        except ValueError:
            self.statusBar.SetStatusText('url error')
        except Exception, e:
            self.statusBar.SetStatusText(str(e))
            return

    def _parse_data(self, data):
        self.tree.DeleteAllItems()
        root = self.tree.AddRoot(u"返回数据如下：")
        self.add_tree_nodes(root, json.loads(data))
        self.tree.Expand(root)
        self.statusBar.SetStatusText('finish')

    def add_tree_nodes(self, parent_item=None, items=None):
        for item in items:
            if isinstance(item, dict):
                self.add_tree_nodes(parent_item,item)
            else:
                if not isinstance(items[item], dict) and not isinstance(items[item], type([])):
                    self.tree.AppendItem(parent_item, '%s : %s' % (item,items[item]))
                else:
                    new_parent =  self.tree.AppendItem(parent_item, item)
                    self.add_tree_nodes(new_parent,items[item])

            if isinstance(items, type([])):
                #如这组数据为列表，则每次取值都添加一个分隔符
                self.tree.AppendItem(parent_item, '-------------------')


class Client(wx.App):
    def __init__(self):
        super(Client, self).__init__()

    def OnInit(self):
        win = MainFrame(None, title="JsonReader by the5fire.net", size=(800, 900), pos=(400,0))
        win.Show()
        return True

def main():
    client = Client()
    client.MainLoop()

if __name__ == '__main__': main()
