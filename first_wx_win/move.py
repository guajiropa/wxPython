#! \Python36\python
# -*- coding: utf-8 -*-

# move.py

import wx
import sys


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(450, 400))

        self.Move((600, 250))
        self.Show()


def main():
    app = wx.App()
    Example(None, title='Move')
    sys.exit(app.MainLoop())

if __name__ == '__main__':
    main()