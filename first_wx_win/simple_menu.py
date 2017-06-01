#! \Python36\python
#
# simple_menu_py

import wx
import sys


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.initUi()

    def initUi(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fQuitItem = fileMenu.Append(wx.ID_EXIT, '&Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fQuitItem)

        self.SetSize(450, 300)
        self.SetTitle('Simple Menu')
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    Example(None)
    sys.exit(app.MainLoop())

if __name__ == '__main__':
    main()

