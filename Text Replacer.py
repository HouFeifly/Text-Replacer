import wx
import os
import re

app = wx.App()
win = wx.Frame(None, title="Text Replacer", size=(800, 600))
bkg = wx.Panel(win)


def opendir(event):
    open_dlg = wx.DirDialog(bkg, message="选择需要替换的文件夹", defaultPath=os.getcwd(),
                            style=wx.DD_DEFAULT_STYLE)
    if open_dlg.ShowModal() == wx.ID_OK:
        path = open_dlg.GetPath()
        filePath.SetValue(path)

    open_dlg.Destroy()


def cleartext(event):
    contents1.Clear()
    contents2.Clear()


def replacetext(event):
    text1 = contents1.GetValue()
    text2 = contents2.GetValue()
    if text1 == '':
        wx.MessageBox('欲替换内容不能为空', '提示')
    elif text2 == '':
        wx.MessageBox('替换内容不能为空', '提示')
    else:
        i = 0
        j = 0
        for file in os.listdir(filePath.GetValue()):
            f = open(filePath.GetValue() + '\\' + file, 'r')
            tmptext = f.read()
            f.close()
            i+=tmptext.count(text1)
            tmptext1 = re.sub(text1, text2, tmptext)
            f = open(filePath.GetValue() + '\\' + file, 'w')
            f.write(tmptext1)
            f.close()
            j+=1
            # contents1.SetValue(f.read())
            # file = open(path, 'r')
            # contents1.SetValue(file.read())
            # file.close()
        wx.MessageBox('替换成功，共替换了' + repr(j) + '个文件，替换了' + repr(i) + '次', '提示')

openButton = wx.Button(bkg, label="选择文件夹")
openButton.Bind(wx.EVT_BUTTON, opendir)

filePath = wx.TextCtrl(bkg, style=wx.TE_READONLY)
label1 = wx.StaticText(bkg, label='输入欲替换内容：')
label2 = wx.StaticText(bkg, label='输入替换内容：    ')
contents1 = wx.TextCtrl(bkg, style=wx.TE_MULTILINE)
contents2 = wx.TextCtrl(bkg, style=wx.TE_MULTILINE)

clearButton = wx.Button(bkg, label="清空输入")
clearButton.Bind(wx.EVT_BUTTON, cleartext)

replaceButton = wx.Button(bkg, label="开始替换")
replaceButton.Bind(wx.EVT_BUTTON, replacetext)

hbox1 = wx.BoxSizer()
hbox1.Add(filePath, proportion=1, flag=wx.EXPAND)
hbox1.Add(openButton, proportion=0, flag=wx.LEFT, border=5)

hbox2 = wx.BoxSizer()
hbox2.Add(label1, proportion=0, flag=wx.LEFT)
hbox2.Add(contents1, proportion=1, flag=wx.EXPAND | wx.LEFT, border=5)

hbox3 = wx.BoxSizer()
hbox3.Add(label2, proportion=0, flag=wx.LEFT)
hbox3.Add(contents2, proportion=1, flag=wx.EXPAND | wx.LEFT, border=5)

hbox4 = wx.BoxSizer()
hbox4.Add(clearButton, proportion=0, flag=wx.LEFT, border=180)
hbox4.Add(replaceButton, proportion=0, flag=wx.LEFT, border=180)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox1, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox2, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox3, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox4, proportion=0, flag=wx.EXPAND | wx.ALL | wx.BOTTOM, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()
