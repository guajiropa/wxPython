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
# Import the needed modules.
import wx
import os
import sys


class simpleTextFrame(wx.Frame):
    """ This is the Main window that is the main
        GUI widget of this application.
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
        # Setup th wx.FileDialog widget.
        dlg = wx.FileDialog(self, "Open a file", ".", "", "All Files|*.*",
                            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        # Show the current dialog as Modal and handle the
        # event if the user presses the cancel button.
        if dlg.ShowModal() == wx.ID_CANCEL:
            return
        else:
            # Open the file to be read.
            filehandle = open(dlg.GetPath(), 'r')
            # Load the text from the file into the wx.TextCtrl.
            self.text_control.SetValue(filehandle.read())
            # Save the current filename and location.
            self.current_file = dlg.Filename
            self.current_dir = dlg.Directory
            # Close the file.
            filehandle.close()
            # Destroy the dialog box.
            dlg.Destroy()

    def OnSave(self, e):
        """ Save the current text loaded in the wxTextCtrl
             named 'text_control'. Check to see if exists
             and prompt for the ok to overwrite the exsisting
             file.
        """
        # Setup th wx.FileDialog widget.
        dlg = wx.FileDialog(self, "Save File", self.current_dir, self.current_file,
                            "All Files|*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        # Show the fileDialog in modal and let the user decide
        # what to do with the file contets loaded in the wxFileCtrl
        if dlg.ShowModal() == wx.ID_OK:
            # If the user presses the OK button, then get the
            # contents from the wx.TextCtrl.
            file_contents = self.text_control.GetValue()
            # Get the current file name and store it int the
            # instance variable.
            self.current_file = dlg.GetFilename()
            # Get the current directory and store it int the
            # instance variable.
            self.current_dir = dlg.GetDirectory()
            # Open the file to write the contents to.
            filehandle = open(os.path.join(self.current_dir, self.current_file), 'w')
            # Write the contents to the file.
            filehandle.write(file_contents)
            # Close the file.
            filehandle.close()
        else:
            # If the end user selects the 'Cancel'
            # button, then return without saving
            return
        # Dispose of the dialog.
        dlg.Destroy()


def main():
    # Create an instance of the application.
    app = wx.App(False)
    # Create an instance of the window and pass in
    # the title to display in the caption bar.
    frame = simpleTextFrame(None, 'Tiny Editor')
    # Start the mainloop that drives the application
    sys.exit(app.MainLoop())

if __name__ == '__main__':
    main()
