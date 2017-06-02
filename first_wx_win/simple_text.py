"""
#
#   AUTHOR      :   Robert James Patterson
#   DATE        :   05/29/2017
#   UPDATED     :   06/02/2017
#   FILENAME    :   simple_text.py
#   SYNOPSIS    :   A simple text editor created for the sole purpose of figuring
#                   wxPython 4.0 (Phoenix) features by constructing a simple cross
#                   platform windows application.
#
"""
# Import the needed modules
import wx
import os
import sys


class simpleTextFrame(wx.Frame):
    """ This is the Main window that is the heart of this application
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(450, 250))

        # Setup values for instance variables
        self.current_file = None
        self.current_dir = None
        self.title = title
        self.text_control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        # Setup the filemenu menu
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open",
                                   "Open a file to edit")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save",
                                   "Save changes to the current file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About",
                                    "Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit",
                                   "Terminate the program")

        # Create the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        # Add the meunbar to the frame content.
        self.SetMenuBar(menuBar)

        # Setup an event handlers for the 'onclick' event on
        # the menu items.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Use some sizers to see layout options.
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.text_control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)

        # Window frame is all set, now Show() it!
        self.Show()

    def OnAbout(self, e):
        """ Display the 'About' dialog.
        """
        dlg = wx.MessageDialog(self, "A small text editor.",
                               "About Simple Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        """ Exit the application.
        """
        self.Close(True)

    def OnOpen(self, e):
        """ Open a file.
        """
        #self.title = title + '\"' + join(self.current_dir, self.current_file) + '\"'
        dlg = wx.FileDialog(self, "Open a file", ".", "", "All Files|*.*",
                            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dlg.ShowModal() == wx.ID_CANCEL:
            return

        filehandle = open(dlg.GetPath(), 'r')
        self.text_control.SetValue(filehandle.read())
        self.current_file = dlg.Filename
        self.current_dir = dlg.Directory
        filehandle.close()
        dlg.Destroy()

    def OnSave(self, e):
        """ Save the current text loaded in
            the wxTextCtrl named 'text_control'.
        """
        dlg = wx.FileDialog(self, "Save File", self.current_dir, self.current_file,
                            "All Files|*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if dlg.ShowModal() == wx.ID_OK:
            file_contents = self.text_control.GetValue()
            self.current_file = dlg.GetFilename()
            self.current_dir = dlg.GetDirectory()
            filehandle = open(os.path.join(self.current_dir, self.current_file), 'w')
            filehandle.write(file_contents)
            filehandle.close()

        # Dispose of the dialog.
        dlg.Destroy()


def main():
    app = wx.App(False)

    frame = simpleTextFrame(None, 'Tiny Editor')
    app.MainLoop()

if __name__ == '__main__':
    main()
