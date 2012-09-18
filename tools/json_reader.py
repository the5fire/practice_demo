#coding:utf-8

import wx
import json


HEAD_START = 0.1 #Seconds
SECRET_LENGTH = 100
SAMPLE_LIST = [
    'http://m.weather.com.cn/data/101010100.html',
]

class Client(wx.App):
    def __init__(self):
        super(Client, self).__init__()

    def OnInit(self):
        win = wx.Frame(None, title="Json Reader", size=(800, 900))
        bkg = wx.Panel(win)
        self.statusBar = win.CreateStatusBar()

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox = wx.BoxSizer()

        self.urlinput = urlinput = wx.TextCtrl(bkg, -1, u'点击下面url或者手动输入', size=(400, 25))
        hbox.Add(urlinput, proportion=1, flag=wx.ALL, border=10)

        submit = wx.Button(bkg, label="Fetch", size=(80, 25))
        submit.Bind(wx.EVT_BUTTON, self.fetchHandler)
        hbox.Add(submit, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND)

        hbox2 = wx.BoxSizer()
        self.url_list = url_list = wx.CheckListBox(bkg, -1, (80, 50), wx.DefaultSize, SAMPLE_LIST)
        self.Bind(wx.EVT_LISTBOX, self.EvtListBox, url_list)
        hbox2.Add(url_list, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(hbox2, proportion=0, flag=wx.EXPAND)

        hbox3 = wx.BoxSizer()
        self.output = output = wx.TextCtrl(bkg, -1, '', size=(400, 600), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        hbox3.Add(output, proportion=1, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)


        vbox.Add(hbox3, proportion=0, flag=wx.EXPAND)
        bkg.SetSizer(vbox)
        win.Show()

        return True

    def EvtListBox(self, event):
        self.urlinput.SetValue(event.GetString())

    def fetchHandler(self, event):
        url = self.urlinput.GetValue()
        import urllib
        try:
            content = urllib.urlopen(url).read()
        except Exception, e:
            self.statusBar.SetStatusText(str(e))
            return
        result = self.parse_json(content)

        self.output.SetValue(result)
        self.statusBar.SetStatusText('finish')

    def parse_json(self, content):
        _content = json.loads(content)
        result = []
        def traversal_json(json_data, sep, step = 2):
            temp = ''
            try:
                #print 'json_data', json_data
                for _ in json_data:
                    temp = _
                    if isinstance(json_data, type([])):
                        result.append('%s%s' % (sep, '*********'))
                    if isinstance(_, dict):
                        traversal_json(_, sep * step)
                    else:
                        if not isinstance(json_data[_], dict) and not isinstance(json_data[_], type([])):
                            key_value = '%s:%s' % (_, json_data[_])
                            result.append('%s%s' % (sep, key_value))
                        else:
                            result.append('%s%s:' % (sep, _))
                        traversal_json(json_data[_], sep * step)
            except Exception, e:
                self.statusBar.SetStatusText('parse data:%s' % temp)

        traversal_json(_content, '--')

        return '\n'.join(result)




def main():
    client = Client()
    client.MainLoop()

if __name__ == '__main__': main()
