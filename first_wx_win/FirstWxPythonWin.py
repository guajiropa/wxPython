import wx

# Create a new app and do not redirect the
#    stdout/stderr to a window
app = wx.App(False)

# Create the frame which is a top level window.
frame = wx.Frame(None, wx.ID_ANY, "Hello wxPython")
frame.Show(True)
app.MainLoop()
