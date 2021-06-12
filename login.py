from database import Database
from noname import login
from home import HomeFrame
from homeA import HomeFrame2
import wx

class LoginFrame(login):
    def __init__(self, parent=None):
        super(LoginFrame, self).__init__(parent)
        self.db = Database()

    def exit(self, event):
        self.Close(True)
        exit("Program berhenti")

    def masuk(self, event):
        if self.input_username.GetValue() == "" or self.input_password.GetValue() == "":
            wx.MessageDialog(self, "Harap isi dengan benar", "Error login").ShowModal()

        self.dataValidation()

    def dataValidation(self):
        username = self.input_username.GetValue()
        password = self.input_password.GetValue()

        self.db.query("SELECT username, password FROM user WHERE username=? and password=?", (username, password))
        dataUser = self.db.resultOne()

        if dataUser != None:
            self.Close()
            homeFrame = HomeFrame(None)
            homeFrame.Show()
        elif username == "admin" and password == "admin":
            self.Close()
            homeFrame = HomeFrame2(None)
            homeFrame.Show()
        else:
            wx.MessageBox("Data Yang anda masukkan salah")