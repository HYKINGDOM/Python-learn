import wx

app = wx.App()
frame = wx.Frame(None, title="wxPython App", size=(300, 200))
panel = wx.Panel(frame)
button = wx.Button(panel, label="Click Me", pos=(100, 100))

frame.Show()
app.MainLoop()