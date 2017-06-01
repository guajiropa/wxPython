#!\Python36\python

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(450, 400))

        self.Show()


def main():

    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()

if __name__ == '__main__':
    main()
