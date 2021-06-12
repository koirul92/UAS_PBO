from login import LoginFrame
import wx

app = wx.App()
frameLogin = LoginFrame()
frameLogin.Show(True)
app.MainLoop()