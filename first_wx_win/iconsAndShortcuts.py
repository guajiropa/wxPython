#! \Python36\python


import wx
import sys

APP_EXIT = 1


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUi()

    def InitUi(self):

        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        fmQuitItem = wx.MenuItem(filemenu, APP_EXIT, '&Quit\tCtrl+Q')
        fmQuitItem.SetBitmap(wx.Bitmap('exit.png'))
        filemenu.Append(fmQuitItem)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(filemenu, '&File')

        self.SetMenuBar(menubar)
        self.SetSize((550, 600))
        self.SetTitle('Icons & Shortcuts')
        self.Center()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    Example(None)
    sys.exit(app.MainLoop())

if __name__ == '__main__':
    main()
